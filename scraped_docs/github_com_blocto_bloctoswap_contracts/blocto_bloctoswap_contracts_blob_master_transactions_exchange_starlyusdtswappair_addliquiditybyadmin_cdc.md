# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/transactions/exchange/StarlyUsdtSwapPair/addLiquidityByAdmin.cdc

```
import "FungibleToken"
import "StarlyToken"
import "TeleportedTetherToken"
import "StarlyUsdtSwapPair"
import "ViewResolver"
import "FungibleTokenMetadataViews"

transaction(token1Amount: UFix64, token2Amount: UFix64) {
  // The Vault references that holds the tokens that are being transferred
  let flowTokenVaultRef: auth(FungibleToken.Withdraw) &StarlyToken.Vault
  let tetherVaultRef: auth(FungibleToken.Withdraw) &TeleportedTetherToken.Vault

  // The Vault reference for liquidity tokens
  let liquidityTokenRef: &StarlyUsdtSwapPair.Vault

  // The Admin reference
  let adminRef: &StarlyUsdtSwapPair.Admin

  prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {
    let flowVaultData = StarlyToken.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
        ?? panic("ViewResolver does not resolve FTVaultData view")

    let tusdtVaultData = TeleportedTetherToken.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
        ?? panic("ViewResolver does not resolve FTVaultData view")

    let lpVaultData = StarlyUsdtSwapPair.resolveContractView(resourceType: nil, viewType: Type<FungibleTokenMetadataViews.FTVaultData>()) as! FungibleTokenMetadataViews.FTVaultData?
        ?? panic("ViewResolver does not resolve FTVaultData view")

    self.flowTokenVaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &StarlyToken.Vault>(from: flowVaultData.storagePath)
      ?? panic("Could not borrow reference to the owner's Vault!")

    self.tetherVaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &TeleportedTetherToken.Vault>(from: tusdtVaultData.storagePath)
      ?? panic("Could not borrow reference to the owner's Vault!")

    if signer.storage.borrow<&StarlyUsdtSwapPair.Vault>(from: lpVaultData.storagePath) == nil {
      let vault <- StarlyUsdtSwapPair.createEmptyVault(vaultType: Type<@StarlyUsdtSwapPair.Vault>())

      // Create a new StarlyUsdtSwapPair Vault and put it in storage
      signer.storage.save(<-vault, to: lpVaultData.storagePath)

      // Create a public capability to the Vault that exposes the Vault interfaces
      let vaultCap = signer.capabilities.storage.issue<&StarlyUsdtSwapPair.Vault>(
          lpVaultData.storagePath
      )
      signer.capabilities.publish(vaultCap, at: lpVaultData.metadataPath)

      // Create a public Capability to the Vault's Receiver functionality
      let receiverCap = signer.capabilities.storage.issue<&StarlyUsdtSwapPair.Vault>(
          lpVaultData.storagePath
      )
      signer.capabilities.publish(receiverCap, at: lpVaultData.receiverPath)
    }

    self.liquidityTokenRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &StarlyUsdtSwapPair.Vault>(from: lpVaultData.storagePath)
      ?? panic("Could not borrow reference to the owner's Vault!")

    self.adminRef = signer.storage.borrow<&StarlyUsdtSwapPair.Admin>(from: /storage/StarlyUsdtSwapAdmin)
      ?? panic("Could not borrow a reference to the admin resource")
  }

  execute {
    // Withdraw tokens
    let token1Vault <- self.flowTokenVaultRef.withdraw(amount: token1Amount) as! @StarlyToken.Vault
    let token2Vault <- self.tetherVaultRef.withdraw(amount: token2Amount) as! @TeleportedTetherToken.Vault

    // Provide liquidity and get liquidity provider tokens
    let tokenBundle <- StarlyUsdtSwapPair.createTokenBundle(fromToken1: <- token1Vault, fromToken2: <- token2Vault)
    let liquidityTokenVault <- self.adminRef.addInitialLiquidity(from: <- tokenBundle)

    // Keep the liquidity provider tokens
    self.liquidityTokenRef.deposit(from: <- liquidityTokenVault)
  }
}

```