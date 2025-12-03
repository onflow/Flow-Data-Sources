# Source: https://cadence-lang.org/

Cadence - Build the Future of Consumer DeFi | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

Cadence

## Build the future of consumer applications and DeFi. The safest, most **composable** language for **onchain experiences** that reach millions.

[Get started](/docs)

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
access(all)
resource NFT {

    access(all)
    fun greet(): String {
        return "I'm NFT #"
            .concat(self.uuid.toString())
    }
}

access(all)
fun main(): String {
    let nft <- create NFT()
    let greeting = nft.greet()
    destroy nft
    return greeting
}
```

Cadence is the best language for digital assets and consumer applications, powering the next generation of Consumer applications and DeFi with institutional-grade security and consumer-friendly experiences that serve millions.

* User assets stay in user accounts, delivering better-than-fintech security without centralized risk.
* Atomic transactions create seamless, one-click experiences that feel native to everyday users.
* Always-on automation runs 24/7/365, enabling recurring payments and strategies that work while you sleep.
* Real-time settlement in seconds, not days, making onchain applications faster than traditional financial rails.
* Open and composable by design, enabling global applications that work together seamlessly.

Cadence pioneers [resource-oriented programming](https://cadence-lang.org/docs/language/resources), designed specifically to handle valuable digital assets. Unlike traditional smart contract languages where assets are piled in centralized contract storage, Cadence ensures user assets stay in their own accounts. The result is dramatically reduced attack surfaces and the elimination of entire classes of vulnerabilities.

Supported by network features like [Flow Actions](https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions) and [Scheduled Transactions](https://developers.flow.com/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction), developers can build sophisticated consumer experiences, from DeFi to digital collectibles to onchain games, that feel native to their users.

```
import "DeFiActions"
import "FlowToken"
import "FlowTransactionScheduler"
import "FlowTransactionSchedulerUtils"
import "IncrementFiStakingConnectors"
import "IncrementFiPoolLiquidityConnectors"
import "SwapConnectors"

// Schedule daily yield compounding with Flow Actions
transaction(stakingPoolId: UInt64, executionEffort: UInt64) {
    prepare(signer: auth(Storage, Capabilities) &Account) {

        // Compose DeFi actions atomically: Claim → Zap → Restake
        let operationID = DeFiActions.createUniqueIdentifier()
        
        // Source: Claim staking rewards
        let rewardsSource = IncrementFiStakingConnectors.PoolRewardsSource(
            userCertificate: signer.capabilities.storage
                .issue<&StakingPool>(/storage/userCertificate),
            pid: stakingPoolId,
            uniqueID: operationID
        )
        
        // Swapper: Convert single reward token → LP tokens
        let zapper = IncrementFiPoolLiquidityConnectors.Zapper(
            token0Type: Type<@FlowToken.Vault>(),
            token1Type: Type<@RewardToken.Vault>(),
            stableMode: false,
            uniqueID: operationID
        )
        
        // Compose: Wrap rewards source with zapper
        let lpSource = SwapConnectors.SwapSource(
            swapper: zapper,
            source: rewardsSource,
            uniqueID: operationID
        )
        
        // Sink: Restake LP tokens back into pool
        let poolSink = IncrementFiStakingConnectors.PoolSink(
            pid: stakingPoolId,
            staker: signer.address,
            uniqueID: operationID
        )

        // Setup transaction scheduler manager
        if signer.storage.borrow<&AnyResource>(
            from: FlowTransactionSchedulerUtils.managerStoragePath) == nil {
            let manager <- FlowTransactionSchedulerUtils.createManager()
            signer.storage.save(<-manager, to: FlowTransactionSchedulerUtils.managerStoragePath)
        }
        
        let manager = signer.storage.borrow<auth(FlowTransactionSchedulerUtils.Owner)
            &{FlowTransactionSchedulerUtils.Manager}>(
            from: FlowTransactionSchedulerUtils.managerStoragePath
        ) ?? panic("Could not borrow Manager")

        // Estimate and pay fees
        let estimate = FlowTransactionScheduler.estimate(
            data: nil,
            timestamp: nextExecution,
            priority: priority,
            executionEffort: executionEffort
        )
        
        let feeVault = signer.storage.borrow<auth(FungibleToken.Withdraw) 
            &FlowToken.Vault>(from: /storage/flowTokenVault)!
        let fees <- feeVault.withdraw(amount: estimate.flowFee ?? 0.0) as! @FlowToken.Vault
        
        // Get handler capability
        let handlerCap = signer.capabilities.storage
            .issue<auth(FlowTransactionScheduler.Execute) 
                &{FlowTransactionScheduler.TransactionHandler}>(/storage/RestakeHandler)
        
        // Schedule recurring execution
        manager.schedule(
            handlerCap: handlerCap,
            data: nil,
            timestamp: getCurrentBlock().timestamp + 86400.0, // 24 hours
            priority: FlowTransactionScheduler.Priority.Medium,
            executionEffort: executionEffort,
            fees: <-fees
        )
    }
}
```

Ready to build the future of on-chain applications? [Get started today](https://developers.flow.com/blockchain-development-tutorials/cadence/getting-started).

### Complex DeFi Operations, Simple User Experiences

In Cadence, transactions are first-class citizens. Write customized transactions that interact with multiple contracts atomically, either all succeed or all fail. No need for intermediary contracts or complex multi-call patterns.

Check staking positions, claim rewards, swap tokens, and restake all in one operation by writing a transaction.

Cadence scripts provide native data availability, querying on-chain data directly without external indexers. Build sophisticated analytics and experiences other chains cannot offer.

This flexibility makes Consumer DeFi possible. Complex operations feel simple while maintaining security and atomicity.

### Perfect for Consumer Apps, NFTs, and Digital Assets

Cadence's [resource-oriented programming](https://cadence-lang.org/docs/language/resources) makes it the ideal language for consumer applications, NFTs, fungible tokens, and digital collectibles. Resources ensure that digital assets are unique, cannot be duplicated, and are owned directly by users, not stored in contract accounts.

Whether you're building a marketplace for NFTs, creating a gaming ecosystem with in-game assets, or launching a new token standard, Cadence provides the security and composability you need. Resources flow naturally between contracts and users, enabling seamless experiences across the entire ecosystem.

Build consumer applications with confidence. Cadence's type system and resource guarantees make it impossible to accidentally lose or duplicate valuable digital assets, giving users and developers peace of mind.

### Built for DeFi Security

In DeFi, security isn't optional. The [resource-oriented programming paradigm](https://cadence-lang.org/docs/language/resources) in Cadence fundamentally changes how assets are stored and protected. **User assets stay in user accounts, not in contract storage.**

Resources guarantee assets can only exist in one location, cannot be copied, and cannot be accidentally lost. Combined with a strong static type system, [enforced business logic](https://cadence-lang.org/docs/language/functions#function-preconditions-and-postconditions), and [capability-based access control](https://cadence-lang.org/docs/language/capabilities), Cadence eliminates entire classes of DeFi vulnerabilities including reentrancy attacks.

Build financial applications with confidence. Cadence provides safety guarantees that let you focus on creating value, not patching vulnerabilities.

### Composable DeFi Primitives

Compose powerful primitives to build sophisticated financial products. [Resources](https://cadence-lang.org/docs/language/resources) stored in users' accounts can flow freely between contracts, which allows seamless integration of lending, swapping, and yield strategies in a single user experience.

[Flow Actions](https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions) allow you to bundle complex multi-step DeFi operations into one-click experiences. [Scheduled Transactions](https://developers.flow.com/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction) turn on native onchain automation. Recurring payments, DCA strategies, and portfolio rebalancing execute directly from user wallets, no backend servers required.

[Interfaces](https://cadence-lang.org/docs/language/interfaces) and [attachments](https://cadence-lang.org/docs/language/attachments) make protocols truly composable. Build new DeFi functionality on top of any token standard to create composable building blocks that work together seamlessly.

### Learn the Best Language for Consumer Applications and DeFi

Cadence is purpose-built for consumer applications and DeFi. Its intuitive syntax and resource-oriented design make it the ideal language for building financial products that millions of users trust.

Learn a language designed from the ground up by smart contract developers for smart contract developers. With comprehensive documentation, powerful testing frameworks, and a supportive community, you'll be building production-ready consumer DeFi apps faster than with traditional smart contract languages.