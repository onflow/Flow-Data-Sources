# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/burn_lp_token.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapFactory from "../../contracts/SwapFactory.cdc"
import SwapInterfaces from "../../contracts/SwapInterfaces.cdc"
import SwapConfig from "../../contracts/SwapConfig.cdc"
import LogEntry from "../../contracts/env/LogEntry.cdc"

transaction(
    pairAddr: Address,
    lpTokenAmount: UFix64,
    toAddr: Address
) {
    prepare(userAccount: auth(BorrowValue) &Account) {
        let lpTokenCollectionFrom = userAccount.storage.borrow<auth(FungibleToken.Withdraw) &SwapFactory.LpTokenCollection>(from: SwapConfig.LpTokenCollectionStoragePath)
            ?? panic("Cannot borrow reference to LpTokenCollection")
        let lpTokenCollectionTo = getAccount(toAddr).capabilities.borrow<&{SwapInterfaces.LpTokenCollectionPublic}>(SwapConfig.LpTokenCollectionPublicPath)
            ?? panic("Cannot borrow reference to tansfer target user's LpTokenCollection")

        let lpTokenTransfer <- lpTokenCollectionFrom.withdraw(pairAddr: pairAddr, amount: lpTokenAmount)
        lpTokenCollectionTo.deposit(pairAddr: pairAddr, lpTokenVault: <- lpTokenTransfer)

        let pairPublicRef = getAccount(pairAddr).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
        let pairInfo = pairPublicRef.getPairInfo()
        LogEntry.LogBurnSwapLp(token0Key: pairInfo[0] as! String, token1Key: pairInfo[1] as! String, pairAddr: pairAddr, amountToBurn: lpTokenAmount)
    }
}
```