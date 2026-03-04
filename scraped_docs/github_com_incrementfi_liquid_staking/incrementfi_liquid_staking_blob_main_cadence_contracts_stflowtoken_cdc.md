# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/contracts/stFlowToken.cdc

```
/**

    $stFlow is a fungible token used in the liquid staking protocol, fully backed by underlying $flow
    $stFlow is a liquid (transferrable), interest-bearing (staking rewards are restaked in each epoch, and thus auto-compounding)
    $stFlow's price grows after each flowchain's epoch advancement
    $stFlow can be redeemed back to $flow *instantly* through dex; or it can also undergo normal unstaking process but that would take several epochs
    $stFlow can be widely used in flowchain's DeFi ecosystems

    @Author: Increment Labs
*/

import Burner from  "./standard/Burner.cdc"
import FungibleToken from "./standard/FungibleToken.cdc"
import FungibleTokenMetadataViews from "./standard/FungibleTokenMetadataViews.cdc"
import MetadataViews from "./standard/MetadataViews.cdc"

access(all) contract stFlowToken: FungibleToken {

    // Total supply of Flow tokens in existence
    access(all) var totalSupply: UFix64

    // Paths
    access(all) let tokenVaultPath: StoragePath
    access(all) let tokenBalancePath: PublicPath
    access(all) let tokenReceiverPath: PublicPath

    // Event that is emitted when the contract is created
    access(all) event TokensInitialized(initialSupply: UFix64)

    // Event that is emitted when tokens are withdrawn from a Vault
    access(all) event TokensWithdrawn(amount: UFix64, from: Address?)

    // Event that is emitted when tokens are deposited to a Vault
    access(all) event TokensDeposited(amount: UFix64, to: Address?)

    // Event that is emitted when new tokens are minted
    access(all) event TokensMinted(amount: UFix64)

    // Event that is emitted when tokens are destroyed
    access(all) event TokensBurned(amount: UFix64)

    // Vault
    //
    // Each user stores an instance of only the Vault in their storage
    // The functions in the Vault and governed by the pre and post conditions
    // in FungibleToken when they are called.
    // The checks happen at runtime whenever a function is called.
    //
    // Resources can only be created in the context of the contract that they
    // are defined in, so there is no way for a malicious user to create Vaults
    // out of thin air. A special Minter resource needs to be defined to mint
    // new tokens.
    access(all) resource Vault: FungibleToken.Vault {

        // holds the balance of a users tokens
        access(all) var balance: UFix64

        // initialize the balance at resource creation time
        init(balance: UFix64) {
            self.balance = balance
        }

        /// Called when this stFlow vault is burned via the `Burner.burn()` method
        access(contract) fun burnCallback() {
            if self.balance > 0.0 {
                emit TokensBurned(amount: self.balance)
                stFlowToken.totalSupply = stFlowToken.totalSupply - self.balance
            }
            self.balance = 0.0
        }

        /// getSupportedVaultTypes optionally returns a list of vault types that this receiver accepts
        access(all) view fun getSupportedVaultTypes(): {Type: Bool} {
            return {self.getType(): true}
        }

        access(all) view fun isSupportedVaultType(type: Type): Bool {
            if (type == self.getType()) { return true } else { return false }
        }

        /// Asks if the amount can be withdrawn from this vault
        access(all) view fun isAvailableToWithdraw(amount: UFix64): Bool {
            return amount <= self.balance
        }

        /// Added to conform to the new FT-V2 interface.
        access(all) view fun getViews(): [Type] {
            return stFlowToken.getContractViews(resourceType: nil)
        }

        access(all) fun resolveView(_ view: Type): AnyStruct? {
            return stFlowToken.resolveContractView(resourceType: nil, viewType: view)
        }

        // withdraw
        //
        // Function that takes an integer amount as an argument
        // and withdraws that amount from the Vault.
        // It creates a new temporary Vault that is used to hold
        // the money that is being transferred. It returns the newly
        // created Vault to the context that called so it can be deposited
        // elsewhere.
        access(FungibleToken.Withdraw) fun withdraw(amount: UFix64): @{FungibleToken.Vault} {
            self.balance = self.balance - amount
            emit TokensWithdrawn(amount: amount, from: self.owner?.address)
            return <-create Vault(balance: amount)
        }

        // deposit
        //
        // Function that takes a Vault object as an argument and adds
        // its balance to the balance of the owners Vault.
        // It is allowed to destroy the sent Vault because the Vault
        // was a temporary holder of the tokens. The Vault's balance has
        // been consumed and therefore can be destroyed.
        access(all) fun deposit(from: @{FungibleToken.Vault}) {
            let vault <- from as! @stFlowToken.Vault
            self.balance = self.balance + vault.balance
            emit TokensDeposited(amount: vault.balance, to: self.owner?.address)
            vault.balance = 0.0
            destroy vault
        }

        access(all) fun createEmptyVault(): @{FungibleToken.Vault} {
            return <-create Vault(balance: 0.0)
        }
    }

    // createEmptyVault
    //
    // Function that creates a new Vault with a balance of zero
    // and returns it to the calling context. A user must call this function
    // and store the returned Vault in their storage in order to allow their
    // account to be able to receive deposits of this token type.
    access(all) fun createEmptyVault(vaultType: Type): @stFlowToken.Vault {
        return <-create Vault(balance: 0.0)
    }

    /// Added to conform to the new FT-V2 interface.
    access(all) view fun getContractViews(resourceType: Type?): [Type] {
        return [
            Type<FungibleTokenMetadataViews.FTView>(),
            Type<FungibleTokenMetadataViews.FTDisplay>(),
            Type<FungibleTokenMetadataViews.FTVaultData>(),
            Type<FungibleTokenMetadataViews.TotalSupply>()
        ]
    }

    access(all) fun resolveContractView(resourceType: Type?, viewType: Type): AnyStruct? {
        switch viewType {
            case Type<FungibleTokenMetadataViews.FTView>():
                return FungibleTokenMetadataViews.FTView(
                    ftDisplay: self.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTDisplay>()) as! FungibleTokenMetadataViews.FTDisplay?,
                    ftVaultData: self.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
                )
            case Type<FungibleTokenMetadataViews.FTDisplay>():
                let media = MetadataViews.Media(
                        file: MetadataViews.HTTPFile(
                        url: "https://cdn.jsdelivr.net/gh/FlowFans/flow-token-list@main/token-registry/A.d6f80565193ad727.stFlowToken/logo.svg"
                    ),
                    mediaType: "image/svg+xml"
                )
                let medias = MetadataViews.Medias([media])
                return FungibleTokenMetadataViews.FTDisplay(
                    name: "Increment Staked FLOW",
                    symbol: "stFlow",
                    description: "stFlow is a liquid staking token representing the underlying staked flow position, allowing users to earn staking rewards and enjoy unlocked liquidity to participate in Flow's DeFi ecosystem at the same time.",
                    externalURL: MetadataViews.ExternalURL("https://www.coingecko.com/en/coins/increment-staked-flow"),
                    logos: medias,
                    socials: {
                        "twitter": MetadataViews.ExternalURL("https://twitter.com/IncrementFi")
                    }
                )
            case Type<FungibleTokenMetadataViews.FTVaultData>():
                return FungibleTokenMetadataViews.FTVaultData(
                    storagePath: stFlowToken.tokenVaultPath,
                    receiverPath: stFlowToken.tokenReceiverPath,
                    metadataPath: stFlowToken.tokenBalancePath,
                    receiverLinkedType: Type<&{FungibleToken.Receiver, FungibleToken.Vault}>(),
                    metadataLinkedType: Type<&{FungibleToken.Balance, FungibleToken.Vault}>(),
                    createEmptyVaultFunction: (fun (): @{FungibleToken.Vault} {
                        let vaultRef = stFlowToken.account.storage.borrow<auth(FungibleToken.Withdraw) &stFlowToken.Vault>(from: stFlowToken.tokenVaultPath)
			                ?? panic("Could not borrow reference to the contract's Vault!")
                        return <- vaultRef.createEmptyVault()
                    })
                )
            case Type<FungibleTokenMetadataViews.TotalSupply>():
                return FungibleTokenMetadataViews.TotalSupply(totalSupply: stFlowToken.totalSupply)
        }
        return nil
    }

    // Mint tokens
    //
    // $stFlow token can only be minted when:
    //   - user stakes unlocked $flow tokens, or
    //   - user migrates existing (staked) NodeDelegator resource
    // into the liquid staking protocol
    access(account) fun mintTokens(amount: UFix64): @stFlowToken.Vault {
        pre {
            amount > 0.0: "Amount minted must be greater than zero"
        }
        stFlowToken.totalSupply = stFlowToken.totalSupply + amount
        emit TokensMinted(amount: amount)
        return <-create Vault(balance: amount)
    }

    // Burn tokens
    //
    // $stFlow token will be burned in exchange for underlying $flow when user requests unstake from the liquid staking protocol
    // Note: totalSupply decrement and event emition happen in token vault's burnCallback()
    access(all) fun burnTokens(from: @stFlowToken.Vault) {
        Burner.burn(<-from)
    }

    init() {
        self.totalSupply = 0.0

        self.tokenVaultPath = /storage/stFlowTokenVault
        self.tokenReceiverPath = /public/stFlowTokenReceiver
        self.tokenBalancePath = /public/stFlowTokenBalance
        
        // Create the Vault with the total supply of tokens and save it in storage
        let vault <- create Vault(balance: self.totalSupply)
        self.account.storage.save(<-vault, to: self.tokenVaultPath)

        // Create a public capability to the stored Vault that only exposes
        // the `deposit` method through the `Receiver` interface
        self.account.capabilities.publish(
            self.account.capabilities.storage.issue<&{FungibleToken.Receiver}>(self.tokenVaultPath),
            at: self.tokenReceiverPath
        )

        // Create a public capability to the stored Vault that only exposes
        // the `balance` field through the `Balance` interface
        self.account.capabilities.publish(
            self.account.capabilities.storage.issue<&{FungibleToken.Balance}>(self.tokenVaultPath),
            at: self.tokenBalancePath
        )

        // Emit an event that shows that the contract was initialized
        emit TokensInitialized(initialSupply: self.totalSupply)
    }
}
```