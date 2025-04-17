# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/lostAndFound/transaction/claim_ft.cdc

```



import FlowToken from 0xFlowToken
import FungibleToken from 0xFungibleToken
import LostAndFound from 0xLostAndFound
import ViewResolver from 0xMetadataViews
import FungibleTokenMetadataViews from 0xFungibleToken
import FlowEVMBridgeUtils from 0xFlowEVMBridge

transaction(vaultIdentifier: String) {
  prepare(acct: auth(Storage, Capabilities) &Account) {
    let vaultType = CompositeType(vaultIdentifier)
      ?? panic("Could not construct Vault type from identifier: ".concat(vaultIdentifier))
    let tokenContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: vaultType)
      ?? panic("Could not get contract address from identifier: ".concat(vaultIdentifier))
    let tokenContractName = FlowEVMBridgeUtils.getContractName(fromType: vaultType)
      ?? panic("Could not get contract name from identifier: ".concat(vaultIdentifier))
    
    let viewResolver = getAccount(tokenContractAddress).contracts.borrow<&{ViewResolver}>(name: tokenContractName)
      ?? panic("Could not borrow ViewResolver from FungibleToken contract")
    let vaultData = viewResolver.resolveContractView(
        resourceType: nil,
        viewType: Type<FungibleTokenMetadataViews.FTVaultData>()
      ) as! FungibleTokenMetadataViews.FTVaultData? ?? panic("Could not resolve FTVaultData view")

    if acct.storage.borrow<&{FungibleToken.Vault}>(from: vaultData.storagePath) == nil {
      acct.storage.save(
        <- vaultData.createEmptyVault(),
        to: vaultData.storagePath
      )
    }

    acct.capabilities.unpublish(vaultData.receiverPath)
    acct.capabilities.publish(
      acct.capabilities.storage.issue<&{FungibleToken.Receiver, FungibleToken.Balance}>(vaultData.storagePath),
      at: vaultData.receiverPath
    )
            
    let cap = acct.capabilities.get<&{FungibleToken.Receiver}>(vaultData.receiverPath)

    LostAndFound.redeemAll(type: vaultType, max: nil, receiver: cap)
    acct.capabilities.storage.getController(byCapabilityID: cap.id)!.delete()
  }
}
```