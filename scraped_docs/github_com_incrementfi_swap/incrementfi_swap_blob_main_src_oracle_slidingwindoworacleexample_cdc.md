# Source: https://github.com/IncrementFi/Swap/blob/main/src/oracle/SlidingWindowOracleExample.cdc

```
import StableSwapFactory from "../contracts/StableSwapFactory.cdc"
import SwapFactory from "../contracts/SwapFactory.cdc"
import SwapInterfaces from "../contracts/SwapInterfaces.cdc"
import SwapConfig from "../contracts/SwapConfig.cdc"

/// Sliding window oracle
///
access(all) contract SlidingWindowOracleExample {
    /// The amount of time (in seconds) the moving average should be computed, e.g. 24 hours
    access(all) let windowSize: UInt64
    /// The number of observation data stored for windowSize.
    /// As granularity increases from 2, more frequent updates are needed, but moving averages become more precise.
    /// twap data is computed over intervals with sizes in the range: [windowSize - (windowSize / granularity) * 2, windowSize]
    access(all) let granularity: UInt64
    /// The amount of time once an update() is needed, periodSize * granularity == windowSize.
    access(all) let periodSize: UInt64
    /// A.contractAddr.contractName: A.11111111.FlowToken, A.2222222.FUSD
    access(all) let token0Key: String
    access(all) let token1Key: String
    access(all) let isStableswap: Bool
    /// pair address in dex
    access(all) let pairAddr: Address
    /// An array of price observation data of the pair
    access(self) let pairObservations: [Observation]

    access(all) struct Observation {
        access(all) let timestamp: UFix64
        access(all) let price0CumulativeScaled: UInt256
        access(all) let price1CumulativeScaled: UInt256

        init(t: UFix64, p0Scaled: UInt256, p1Scaled: UInt256) {
            self.timestamp = t
            self.price0CumulativeScaled = p0Scaled
            self.price1CumulativeScaled = p1Scaled
        }
    }


    /// Returns the index of the observation corresponding to the given timestamp
    access(all) fun observationIndexOf(timestamp: UFix64): UInt64 {
        return UInt64(timestamp) / self.periodSize % self.granularity
    }

    /// Returns the index of the earliest observation of a windowSize (relative to the given timestamp)
    access(all) fun firstObservationIndexInWindow(timestamp: UFix64): UInt64 {
        let idx = self.observationIndexOf(timestamp: timestamp)
        return (idx + 1) % self.granularity
    }

    /// Update the cumulative price for the observation at the current timestamp.
    /// Each observation is updated at most once per periodSize.
    access(all) fun update() {
        let now = getCurrentBlock().timestamp
        let idx = self.observationIndexOf(timestamp: now)
        let ob = self.pairObservations[idx]
        let timeElapsed = now - ob.timestamp

        if (timeElapsed > UFix64(self.periodSize)) {
            let timeElapsedScaled = SwapConfig.UFix64ToScaledUInt256(timeElapsed)
            let res = SwapConfig.getCurrentCumulativePrices(pairAddr: self.pairAddr)
            let currentPrice0CumulativeScaled = res[0]
            let currentPrice1CumulativeScaled = res[1]
            self.pairObservations[idx] = Observation(t: now, p0Scaled: currentPrice0CumulativeScaled, p1Scaled: currentPrice1CumulativeScaled)
        }
    }

    /// Queries twap price data of the time range [now - [windowSize, windowSize - 2 * periodSize], now]
    /// Returns 0.0 for data n/a or invalid input token
    access(all) fun twap(tokenKey: String): UFix64 {
        let now = getCurrentBlock().timestamp
        let first_ob_idx = self.firstObservationIndexInWindow(timestamp: now)
        let first_ob = self.pairObservations[first_ob_idx]
        let timeElapsed = now - first_ob.timestamp

        assert(UInt64(timeElapsed) <= self.windowSize, message: "missing historical observations, more update() needed")
        assert(UInt64(timeElapsed) >= self.windowSize - self.periodSize * 2, message: "should never happen")

        let res = SwapConfig.getCurrentCumulativePrices(pairAddr: self.pairAddr)
        let currentPrice0CumulativeScaled = res[0]
        let currentPrice1CumulativeScaled = res[1]
        let timeElapsedScaled = SwapConfig.UFix64ToScaledUInt256(timeElapsed)

        if (tokenKey == self.token0Key) {
            let price0AverageScaled = SwapConfig.underflowSubtractUInt256(currentPrice0CumulativeScaled, first_ob.price0CumulativeScaled) * SwapConfig.scaleFactor / timeElapsedScaled
            return SwapConfig.ScaledUInt256ToUFix64(price0AverageScaled)
        } else if (tokenKey == self.token1Key) {
            let price1AverageScaled = SwapConfig.underflowSubtractUInt256(currentPrice1CumulativeScaled, first_ob.price1CumulativeScaled) * SwapConfig.scaleFactor / timeElapsedScaled
            return SwapConfig.ScaledUInt256ToUFix64(price1AverageScaled)
        } else {
            return 0.0
        }
    }

    /// @Param - token{A|B}Key: e.g. A.f8d6e0586b0a20c7.FUSD
    /// @Param - isStableswap: whether the twap is for stableswap pair or not
    /// @Param - windowSize: The amount of time (in seconds) the moving average should be computed, e.g.: 24 hours (86400)
    /// @Param - granularity: The number of observation data stored for windowSize, e.g.: 24. The more granularity, the more precise the moving average, but with the cost of more frequent updates are needed.
    init(tokenAKey: String, tokenBKey: String, isStableswap: Bool, windowSize: UInt64, granularity: UInt64) {
        pre {
            granularity > 1 && granularity <= windowSize: "invalid granularity"
            windowSize / granularity * granularity == windowSize: "windowSize not-divisible by granularity"
        }
        post {
            UInt64(self.pairObservations.length) == granularity: "pairObservations array not initialized"
        }

        self.windowSize = windowSize
        self.granularity = granularity
        self.periodSize = windowSize / granularity
        self.isStableswap = isStableswap
        self.pairAddr = isStableswap ?
            StableSwapFactory.getPairAddress(token0Key: tokenAKey, token1Key: tokenBKey) ?? panic("non-existent stableswap-pair") :
            SwapFactory.getPairAddress(token0Key: tokenAKey, token1Key: tokenBKey) ?? panic("non-existent pair")

        let pairPublicRef = getAccount(self.pairAddr).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)
            ?? panic("cannot borrow reference to PairPublic")
        let pairInfo = pairPublicRef.getPairInfo()
        self.token0Key = pairInfo[0] as! String
        self.token1Key = pairInfo[1] as! String
        let reserve0 = pairInfo[2] as! UFix64
        let reserve1 = pairInfo[3] as! UFix64
        assert(reserve0 * reserve1 != 0.0, message: "There's no liquidity in the pair")

        self.pairObservations = []
        var i: UInt64 = 0
        while (i < granularity) {
            self.pairObservations.append(Observation(t: 0.0, p0Scaled: 0, p1Scaled: 0))
            i = i + 1
        }
    }
}
```