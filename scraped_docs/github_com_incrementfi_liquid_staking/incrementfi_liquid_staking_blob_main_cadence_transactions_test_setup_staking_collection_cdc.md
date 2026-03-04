# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/test/setup_staking_collection.cdc

```
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"
import FlowToken from "../../contracts/standard/FlowToken.cdc"
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"
import LockedTokens from "../../contracts/standard/mainnet/LockedTokens.cdc"
import FlowStakingCollection from "../../contracts/standard/mainnet/FlowStakingCollection.cdc"

/// This transaction sets up an account to use a staking collection
/// It will work regardless of whether they have a regular account, a two-account locked tokens setup,
/// or staking objects stored in the unlocked account

transaction {
    prepare(signer: auth(Storage, Capabilities) &Account) {

        // If there isn''t already a staking collection
        if signer.storage.borrow<&FlowStakingCollection.StakingCollection>(from: FlowStakingCollection.StakingCollectionStoragePath) == nil {

            // Create private capabilities for the token holder and unlocked vault
            let lockedHolder = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw, LockedTokens.TokenOperations) &LockedTokens.TokenHolder>(LockedTokens.TokenHolderStoragePath)
            let flowToken = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &FlowToken.Vault>(/storage/flowTokenVault)

            // Create a new Staking Collection and put it in storage
            if lockedHolder.check() {
                signer.storage.save(<-FlowStakingCollection.createStakingCollection(unlockedVault: flowToken, tokenHolder: lockedHolder), to: FlowStakingCollection.StakingCollectionStoragePath)
            } else {
                signer.storage.save(<-FlowStakingCollection.createStakingCollection(unlockedVault: flowToken, tokenHolder: nil), to: FlowStakingCollection.StakingCollectionStoragePath)
            }

            // Create a public capability to the created staking collection
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FlowStakingCollection.StakingCollectionPublic}>(FlowStakingCollection.StakingCollectionStoragePath),
                at: FlowStakingCollection.StakingCollectionPublicPath
            )
        }

        // borrow a reference to the staking collection
        let collectionRef = signer.storage.borrow<&FlowStakingCollection.StakingCollection>(from: FlowStakingCollection.StakingCollectionStoragePath)
            ?? panic("Could not borrow staking collection reference")

        // If there is a node staker object in the account, put it in the staking collection
        if signer.storage.borrow<&FlowIDTableStaking.NodeStaker>(from: FlowIDTableStaking.NodeStakerStoragePath) != nil {
            let node <- signer.storage.load<@FlowIDTableStaking.NodeStaker>(from: FlowIDTableStaking.NodeStakerStoragePath)!
            collectionRef.addNodeObject(<-node, machineAccountInfo: nil)
        }

        // If there is a delegator object in the account, put it in the staking collection
        if signer.storage.borrow<&FlowIDTableStaking.NodeDelegator>(from: FlowIDTableStaking.DelegatorStoragePath) != nil {
            let delegator <- signer.storage.load<@FlowIDTableStaking.NodeDelegator>(from: FlowIDTableStaking.DelegatorStoragePath)!
            collectionRef.addDelegatorObject(<-delegator)
        }
    }
}
```