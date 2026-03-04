# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/test/mint_all_tokens.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"

import BUSD from "../../contracts/tokens/BUSD.cdc"
import FUSD from "../../contracts/tokens/FUSD.cdc"
import USDC from "../../contracts/tokens/USDC.cdc"
import USDT from "../../contracts/tokens/USDT.cdc"
import wFlow from "../../contracts/tokens/wFlow.cdc"
import BLT from "../../contracts/tokens/BLT.cdc"
import TestTokenA from "../../contracts/tokens/TestTokenA.cdc"
import TestTokenB from "../../contracts/tokens/TestTokenB.cdc"
import TestTokenC from "../../contracts/tokens/TestTokenC.cdc"

transaction(mintAmount: UFix64) {

    prepare(signer: auth(Storage, Capabilities) &Account) {
        log("Transaction Start --------------- mint all tokens")
        
        var vaultStoragePath = /storage/test_busdVault
        var vaultReceiverPath = /public/test_busdReceiver
        var vaultBalancePath = /public/test_busdBalance
        var busdVaultRef = signer.storage.borrow<&BUSD.Vault>(from: vaultStoragePath)
        if busdVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-BUSD.createEmptyVault(vaultType: Type<@BUSD.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        busdVaultRef = signer.storage.borrow<&BUSD.Vault>(from: vaultStoragePath)
        busdVaultRef!.deposit(from: <-BUSD.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(busdVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/test_fusdVault
        vaultReceiverPath = /public/test_fusdReceiver
        vaultBalancePath = /public/test_fusdBalance
        var fusdVaultRef = signer.storage.borrow<&FUSD.Vault>(from: vaultStoragePath)
        if fusdVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-FUSD.createEmptyVault(vaultType: Type<@FUSD.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        fusdVaultRef = signer.storage.borrow<&FUSD.Vault>(from: vaultStoragePath)
        fusdVaultRef!.deposit(from: <-FUSD.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(fusdVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/test_usdcVault
        vaultReceiverPath = /public/test_usdcReceiver
        vaultBalancePath = /public/test_usdcBalance
        var usdcVaultRef = signer.storage.borrow<&USDC.Vault>(from: vaultStoragePath)
        if usdcVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-USDC.createEmptyVault(vaultType: Type<@USDC.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        usdcVaultRef = signer.storage.borrow<&USDC.Vault>(from: vaultStoragePath)
        usdcVaultRef!.deposit(from: <-USDC.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(usdcVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/test_usdtVault
        vaultReceiverPath = /public/test_usdtReceiver
        vaultBalancePath = /public/test_usdtBalance
        var usdtVaultRef = signer.storage.borrow<&USDT.Vault>(from: vaultStoragePath)
        if usdtVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-USDT.createEmptyVault(vaultType: Type<@USDT.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        usdtVaultRef = signer.storage.borrow<&USDT.Vault>(from: vaultStoragePath)
        usdtVaultRef!.deposit(from: <-USDT.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(usdtVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/test_wflowVault
        vaultReceiverPath = /public/test_wflowReceiver
        vaultBalancePath = /public/test_wflowBalance
        var wflowVaultRef = signer.storage.borrow<&wFlow.Vault>(from: vaultStoragePath)
        if wflowVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-wFlow.createEmptyVault(vaultType: Type<@wFlow.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        wflowVaultRef = signer.storage.borrow<&wFlow.Vault>(from: vaultStoragePath)
        wflowVaultRef!.deposit(from: <-wFlow.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(wflowVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/test_bltVault
        vaultReceiverPath = /public/test_bltReceiver
        vaultBalancePath = /public/test_bltBalance
        var bLTVaultRef = signer.storage.borrow<&BLT.Vault>(from: vaultStoragePath)
        if bLTVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-BLT.createEmptyVault(vaultType: Type<@BLT.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        bLTVaultRef = signer.storage.borrow<&BLT.Vault>(from: vaultStoragePath)
        bLTVaultRef!.deposit(from: <-BLT.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(bLTVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/testTokenAVault
        vaultReceiverPath = /public/testTokenAReceiver
        vaultBalancePath = /public/testTokenABalance
        var testTokenAVaultRef = signer.storage.borrow<&TestTokenA.Vault>(from: vaultStoragePath)
        if testTokenAVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-TestTokenA.createEmptyVault(vaultType: Type<@TestTokenA.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        testTokenAVaultRef = signer.storage.borrow<&TestTokenA.Vault>(from: vaultStoragePath)
        testTokenAVaultRef!.deposit(from: <-TestTokenA.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(testTokenAVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/testTokenBVault
        vaultReceiverPath = /public/testTokenBReceiver
        vaultBalancePath = /public/testTokenBBalance
        var testTokenBVaultRef = signer.storage.borrow<&TestTokenB.Vault>(from: vaultStoragePath)
        if testTokenBVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-TestTokenB.createEmptyVault(vaultType: Type<@TestTokenB.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        testTokenBVaultRef = signer.storage.borrow<&TestTokenB.Vault>(from: vaultStoragePath)
        testTokenBVaultRef!.deposit(from: <-TestTokenB.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(testTokenBVaultRef!.balance.toString()))
        /////////////////
        vaultStoragePath = /storage/testTokenCVault
        vaultReceiverPath = /public/testTokenCReceiver
        vaultBalancePath = /public/testTokenCBalance
        var testTokenCVaultRef = signer.storage.borrow<&TestTokenC.Vault>(from: vaultStoragePath)
        if testTokenCVaultRef == nil {
            destroy <- signer.storage.load<@AnyResource>(from: vaultStoragePath)

            signer.storage.save(<-TestTokenC.createEmptyVault(vaultType: Type<@TestTokenC.Vault>()), to: vaultStoragePath)
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Receiver}>(vaultStoragePath),
                at: vaultReceiverPath
            )
            signer.capabilities.publish(
                signer.capabilities.storage.issue<&{FungibleToken.Balance}>(vaultStoragePath),
                at: vaultBalancePath
            )
        }
        testTokenCVaultRef = signer.storage.borrow<&TestTokenC.Vault>(from: vaultStoragePath)
        testTokenCVaultRef!.deposit(from: <-TestTokenC.test_minter.mintTokens(amount: mintAmount))
        log("mint ".concat(testTokenCVaultRef!.balance.toString()))
        log("End -----------------------------")
    }
}
```