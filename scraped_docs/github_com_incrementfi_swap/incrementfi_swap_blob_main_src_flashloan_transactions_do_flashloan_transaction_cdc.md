# Source: https://github.com/IncrementFi/Swap/blob/main/src/flashloan/transactions/do_flashloan.transaction.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"

/*
    E.g.: Flashloan request only $USDC from FUSD/USDC pool
*/
transaction(pairAddr: Address, requestedVaultType: Type, requestedAmount: UFix64) {
    prepare(signer: auth(BorrowValue) &Account) {
        let pairRef = getAccount(pairAddr).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)
            ?? panic("cannot borrow reference to PairPublic")

        // TODO: add additional args? and generalize this transaction
        let args: {String: AnyStruct} = {
            "profitReceiver": signer.address
        }

        let executorRef = signer.storage.borrow<&{SwapInterfaces.FlashLoanExecutor}>(from: /storage/swap_flashloan_executor_path)
            ?? panic("cannot borrow reference to FlashLoanExecutor")
        pairRef.flashloan(executor: executorRef, requestedTokenVaultType: requestedVaultType, requestedAmount: requestedAmount, params: args)
    }
}
```