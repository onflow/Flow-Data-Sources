# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/User/liquidate.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import LendingConfig from "../../contracts/LendingConfig.cdc"
import LendingComptroller from "../../contracts/LendingComptroller.cdc"
//import SwapRouter from 0xa6850776a94e6551
import SwapRouter from 0x2f8af5ed05bbde0d


// Liquidation Inform:
//
// Liquidated Address: BORROWER
// Repaied LIQUIDATEAMOUNT LIQUIDATETOKEN on your behalf
//
transaction(repayPoolAddr: Address, seizePoolAddr: Address, amountLiquidate: UFix64, borrower: Address) {
    prepare(signer: auth(Storage, StorageCapabilities) &Account) {
        let poolRepayRef = getAccount(repayPoolAddr).capabilities.borrow<&{LendingInterfaces.PoolPublic}>(LendingConfig.PoolPublicPublicPath)!
        let poolSeizeRef = getAccount(seizePoolAddr).capabilities.borrow<&{LendingInterfaces.PoolPublic}>(LendingConfig.PoolPublicPublicPath)!

        let repayTokenStr = poolRepayRef.getUnderlyingTypeString()
        let seizeTokenStr = poolSeizeRef.getUnderlyingTypeString()
        let repayTokenTypeStr = getTokenTypeStr(poolRepayRef.getUnderlyingAssetType())
        let seizeTokenTypeStr = getTokenTypeStr(poolSeizeRef.getUnderlyingAssetType())
        
        var repayVaultPath = getTokenVaultPath(repayTokenStr)
        var seizeVaultPath = getTokenVaultPath(seizeTokenStr)

        var repayWallet = signer.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: repayVaultPath)
            ?? panic("cannot borrow auth(FT.Withdraw) reference to repaid FT.Vault")
        var seizeWallet = signer.storage.borrow<&{FungibleToken.Vault}>(from: seizeVaultPath)
            ?? panic("cannot borrow reference to seized FT.Vault")

        var liquidateInAmount = repayWallet.balance
        let repayVault <- repayWallet.withdraw(amount: amountLiquidate)

        // liquidate
        let leftVault <- poolRepayRef.liquidate(
            liquidator: signer.address,
            borrower: borrower,
            poolCollateralizedToSeize: seizePoolAddr,
            repayUnderlyingVault: <-repayVault
        )
        if leftVault != nil {
            repayWallet.deposit(from: <-leftVault!)
        } else {
            destroy leftVault
        }
        liquidateInAmount = liquidateInAmount - repayWallet.balance

        // redeem all
        if (signer.storage.borrow<&{LendingInterfaces.IdentityCertificate}>(from: LendingConfig.UserCertificateStoragePath) == nil) {
            destroy <-signer.storage.load<@AnyResource>(from: LendingConfig.UserCertificateStoragePath)
            let userCertificate <- LendingComptroller.IssueUserCertificate()
            signer.storage.save(<-userCertificate, to: LendingConfig.UserCertificateStoragePath)
        }
        let userCertificate = signer.storage.borrow<&{LendingInterfaces.IdentityCertificate}>(from: LendingConfig.UserCertificateStoragePath)
            ?? panic("cannot borrow reference to UserCertificate")
        let redeemedVault <- poolSeizeRef.redeemUnderlying(userCertificate: userCertificate, numUnderlyingToRedeem: UFix64.max)
        
        // swap or withdraw
        var swapPath: [String] = []
        if seizeTokenStr == "FiatToken" && repayTokenStr == "FlowToken" { swapPath = [seizeTokenTypeStr, repayTokenTypeStr] }
        if seizeTokenStr == "FlowToken" && repayTokenStr == "FiatToken" { swapPath = [seizeTokenTypeStr, repayTokenTypeStr] }
        if seizeTokenStr == "stFlowToken" && repayTokenStr == "FiatToken" { swapPath = [seizeTokenTypeStr, "A.1654653399040a61.FlowToken", repayTokenTypeStr] }
        if seizeTokenStr == "stFlowToken" && repayTokenStr == "FlowToken" { swapPath = [seizeTokenTypeStr, repayTokenTypeStr] }
        if seizeTokenStr == "FiatToken" && repayTokenStr == "stFlowToken" { swapPath = [seizeTokenTypeStr, "A.1654653399040a61.FlowToken", repayTokenTypeStr] }
        if seizeTokenStr == "FlowToken" && repayTokenStr == "stFlowToken" { swapPath = [seizeTokenTypeStr, repayTokenTypeStr] }
        if swapPath.length > 0 {
            let vaultOut <- SwapRouter.swapWithPath(vaultIn: <- redeemedVault, tokenKeyPath: swapPath, exactAmounts: nil)
            assert(vaultOut.balance > liquidateInAmount, message: "liquidate with no profit")
            repayWallet.deposit(from: <-vaultOut)
        } else {
            // no swap
            seizeWallet.deposit(from: <-redeemedVault)
        }        
        
        // inform
        let informVault <- signer.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: /storage/flowTokenVault)!.withdraw(amount: 0.00000001)
        let flowTokenReceiverRef = getAccount(borrower).capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!
        flowTokenReceiverRef.deposit(from: <-informVault)
    }
}

access(all) fun getTokenVaultPath(_ tokenStr: String): StoragePath {
    var vaultPath = /storage/null
    switch tokenStr {
        case "FlowToken": vaultPath = /storage/flowTokenVault
        case "stFlowToken": vaultPath = /storage/stFlowTokenVault
        case "FiatToken": vaultPath = /storage/USDCVault
        case "FUSD": vaultPath = /storage/fusdVault
        case "BloctoToken": vaultPath = /storage/bloctoTokenVault
    }

    return vaultPath
}

access(all) fun getTokenTypeStr(_ vaultTypeStr: String): String {
    return vaultTypeStr.slice(from: 0, upTo: vaultTypeStr.length - 6)
}
```