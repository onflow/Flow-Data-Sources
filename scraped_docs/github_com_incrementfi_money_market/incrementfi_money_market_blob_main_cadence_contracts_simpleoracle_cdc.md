# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/contracts/SimpleOracle.cdc

```
/**

# A simple centralized oracle maintained by the team. Admin can grant updateData role to other managed accounts.

# Author: Increment Labs

Only used on testnet.

*/
import LendingInterfaces from "./LendingInterfaces.cdc"
access(all) contract SimpleOracle {
    /// The storage path for the Admin resource
    access(all) let OracleAdminStoragePath: StoragePath
    /// The storage path for the Oracle resource
    access(all) let OracleStoragePath: StoragePath
    /// The public path for the capability to restricted to &{LendingInterfaces.OraclePublic}
    access(all) let OraclePublicPath: PublicPath

    /// The storage path for updater's OracleUpdateProxy resource
    access(all) let UpdaterStoragePath: StoragePath
    /// The public path for updater's OracleUpdateProxy capability
    access(all) let UpdaterPublicPath: PublicPath

    access(all) event PriceFeedAdded(poolAddr: Address, maxCapacity: Int)
    access(all) event PriceFeedRemoved(poolAddr: Address)
    access(all) event DataUpdated(poolAddr: Address, timestamp: UFix64, data: UFix64)

    /// A single data point the off-chain oracle node reports.
    access(all) struct Observation {
        access(all) let timestamp: UFix64
        access(all) let priceData: UFix64

        init(timestamp: UFix64, data: UFix64) {
            self.timestamp = timestamp
            self.priceData = data
        }
    }

    /// Use RingBuffer to store reported data points (i.e. the Observation).
    /// We don't want to store infinity data on-chain since storing data on flow consumes account storage.
    access(all) resource RingBuffer {
        /// Points to the next enqueue position
        access(self) var tail: Int
        access(all) let capacity: Int
        access(all) let dataType: Type
        access(self) let data: [AnyStruct]
        
        init(capacity: Int, dataType: Type) {
            self.capacity = capacity
            self.tail = 0
            self.dataType = dataType
            self.data = []
        }

        access(all) view fun isEmpty(): Bool {
            return self.data.length == 0
        }

        access(all) view fun isFull(): Bool {
            return self.data.length == self.capacity
        }

        /// Return the last enqueued item.
        /// Note: Caller ensures that the buffer is not empty.
        access(all) view fun peek(): AnyStruct {
            let index = self.tail == 0 ? self.capacity - 1 : self.tail - 1
            return self.data[index]
        }

        /// Insert data into tail then update pointers
        access(all) fun enqueue(_ item: AnyStruct) {
            if (item.isInstance(self.dataType)) {
                if (self.isFull()) {
                    self.data[self.tail] = item
                } else {
                    self.data.append(item)
                }
                self.tail = (self.tail + 1) % self.capacity
            } else {
                panic("Data type mismatch, expected: "
                    .concat(self.dataType.identifier)
                    .concat(", given: ")
                    .concat(item.getType().identifier)
                )
            }
        }
    }

    access(all) resource interface DataUpdater {
        access(contract) fun updatePrice(pool: Address, data: UFix64)
    }

    access(all) resource Oracle: LendingInterfaces.OraclePublic, DataUpdater {
        access(self) let feeds: [Address]
        /// { poolAddress : Oracle data for pool }
        access(self) let observations: @{Address: RingBuffer}

        /// Return underlying asset price of the pool, denominated in USD.
        /// Return 0.0 means price feed for the given pool is not available.  
        access(all) view fun getUnderlyingPrice(pool: Address): UFix64 {
            if (!self.feeds.contains(pool)) {
                return 0.0
            }
            return self.latestResult(pool: pool)[1]
        }

        /// Return pool's latest data point in form of (timestamp, data)
        access(all) view fun latestResult(pool: Address): [UFix64; 2] {
            let dataRef = (&self.observations[pool] as &RingBuffer?)!
            if (dataRef == nil || dataRef.isEmpty()) {
                return [0.0, 0.0]
            }
            let latestData = dataRef.peek() as! Observation
            return [
                latestData.timestamp,
                latestData.priceData
            ]
        }

        access(all) view fun getSupportedFeeds(): [Address] {
            return self.feeds
        }

        access(contract) fun addPriceFeed(pool: Address, maxCapacity: Int) {
            if (!self.feeds.contains(pool)) {
                // 1. Append new feed
                self.feeds.append(pool)
                // 2. Create RingBuffer resource to hold new feed's data
                let oldData <- self.observations[pool] <- create RingBuffer(capacity: maxCapacity, dataType: Type<Observation>())
                destroy oldData
                emit PriceFeedAdded(poolAddr: pool, maxCapacity: maxCapacity)
            }

        }

        access(contract) fun removePriceFeed(pool: Address) {
            if (self.feeds.contains(pool)) {
                // 1. Remove pool from data feeds
                var idx = 0
                while idx < self.feeds.length {
                    if (self.feeds[idx] == pool) {
                        break
                    }
                    idx = idx + 1
                }
                let lastToken = self.feeds.removeLast()
                if (lastToken != pool) {
                    self.feeds[idx] = lastToken
                }
                // 2. Remove pool's associated data
                let oldData <- self.observations.remove(key: pool)
                destroy oldData
                emit PriceFeedRemoved(poolAddr: pool)
            }
        }

        access(contract) fun updatePrice(pool: Address, data: UFix64) {
            if (self.feeds.contains(pool)) {
                let dataRef = (&self.observations[pool] as &RingBuffer?)!
                let now = getCurrentBlock().timestamp
                dataRef.enqueue(Observation(timestamp: now, data: data))
                emit DataUpdated(poolAddr: pool, timestamp: now, data: data)
            }
        }

        init () {
            self.feeds = []
            self.observations <- {}
        }
    }

    access(all) resource interface OracleUpdateProxyPublic {
        access(all) fun isUpdaterCapabilityGranted(): Bool
        access(all) fun setUpdaterCapability(cap: Capability<&{DataUpdater}>)
    }

    /// Other accounts holding OracleUpdateProxy resource can be granted with oracle DataUpdater Capability by Admin.
    access(all) resource OracleUpdateProxy: OracleUpdateProxyPublic {
        /// Nobody else can copy the capability and use it.
        access(self) var updateCapability: Capability<&{DataUpdater}>?

        access(all) fun isUpdaterCapabilityGranted(): Bool {
            return self.updateCapability != nil && self.updateCapability!.check() == true
        }

        /// Only Admin can grant oracle DataUpdater capability so the type system guarantees it to be called only by Admin.
        access(all) fun setUpdaterCapability(cap: Capability<&{DataUpdater}>) {
            self.updateCapability = cap
        }

        access(all) fun update(pool: Address, data: UFix64) {
            self.updateCapability!.borrow()!.updatePrice(pool: pool, data: data)
        }

        init() {
            self.updateCapability = nil
        }
    }

    /// Anyone can call this, but OracleUpdateProxy cannot update oracle without Oracle capability,
    /// which can only be given by Admin.
    access(all) fun createUpdateProxy(): @OracleUpdateProxy {
        return <- create OracleUpdateProxy()
    }

    access(all) resource Admin {
        /// Creating an Oracle resource which holds @maxCapacity data points at most.
        access(all) fun createOracleResource(): @Oracle {
            return <- create Oracle()
        }
        /// Admin can update data points directly, however, we also want to grant update rights to specific accounts
        /// (i.e. off-chain oracle clients), so as not to expose admin private key in any condition.
        access(all) fun update(oracleRef: &Oracle, pool: Address, data: UFix64) {
            oracleRef.updatePrice(pool: pool, data: data)
        }
        access(all) fun addPriceFeed(oracleRef: &Oracle, pool: Address, capacity: Int) {
            oracleRef.addPriceFeed(pool: pool, maxCapacity: capacity)
        }
        access(all) fun removePriceFeed(oracleRef: &Oracle, pool: Address) {
            oracleRef.removePriceFeed(pool: pool)
        }
    }

    init() {
        self.OracleAdminStoragePath = /storage/oracleAdmin
        self.OracleStoragePath = /storage/oracleModule
        self.OraclePublicPath = /public/oracleModule
        self.UpdaterStoragePath = /storage/oracleUpdaterProxy
        self.UpdaterPublicPath = /public/oracleUpdaterProxy

        destroy <-self.account.storage.load<@AnyResource>(from: self.OracleAdminStoragePath)
        self.account.storage.save(<-create Admin(), to: self.OracleAdminStoragePath)
    }
}
```