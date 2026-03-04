# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/split_swap_exact_tokens_for_tokens.cdc

```
import FungibleToken from "../../contracts/env/FungibleToken.cdc"
import SwapRouter from "../../contracts/SwapRouter.cdc"
import SwapError from "../../contracts/SwapError.cdc"

transaction(
    tokenKeyFlatSplitPath: [String],
    amountInSplit: [UFix64],
    amountOutMin: UFix64,
    deadline: UFix64,
    tokenInVaultPath: StoragePath,
    tokenOutVaultPath: StoragePath,
    tokenOutReceiverPath: PublicPath,
    tokenOutBalancePath: PublicPath,
    Token1Name: String,
    Token1Addr: Address
) {
    prepare(userAccount: auth(Storage, Capabilities) &Account) {
        assert(deadline >= getCurrentBlock().timestamp, message:
            SwapError.ErrorEncode(
                msg: "EXPIRED",
                err: SwapError.ErrorCode.EXPIRED
            )
        )

        let len = tokenKeyFlatSplitPath.length
        let tokenInKey = tokenKeyFlatSplitPath[0]
        let tokenOutKey = tokenKeyFlatSplitPath[len-1]

        var tokenOutAmountTotal = 0.0

        var tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: tokenOutVaultPath)
        if tokenOutReceiverRef == nil {
            let token1AddrStr = Token1Addr.toString()
            let token1AddrStr0xTrimmed = token1AddrStr.slice(from: 2, upTo: token1AddrStr.length)
            let token1VaultRuntimeType = CompositeType("A.".concat(token1AddrStr0xTrimmed).concat(".").concat(Token1Name).concat(".Vault")) ?? panic("token1 get runtime type fail")
            userAccount.storage.save(<-getAccount(Token1Addr).contracts.borrow<&{FungibleToken}>(name: Token1Name)!.createEmptyVault(vaultType: token1VaultRuntimeType), to: tokenOutVaultPath)
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Receiver}>(tokenOutVaultPath),
                at: tokenOutReceiverPath
            )
            userAccount.capabilities.publish(
                userAccount.capabilities.storage.issue<&{FungibleToken.Balance}>(tokenOutVaultPath),
                at: tokenOutBalancePath
            )
            tokenOutReceiverRef = userAccount.storage.borrow<&{FungibleToken.Vault}>(from: tokenOutVaultPath)
        }

        var pathIndex = 0
        var i = 0
        var path: [String] = []
        while(i < len) {
            var curTokenKey = tokenKeyFlatSplitPath[i]
            path.append(curTokenKey)
            if (curTokenKey == tokenOutKey) {
                log(path)
                let tokenInAmount = amountInSplit[pathIndex]

                let tokenInVault <- userAccount.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(from: tokenInVaultPath)!.withdraw(amount: tokenInAmount)
                let tokenOutVault <- SwapRouter.swapWithPath(vaultIn: <- tokenInVault, tokenKeyPath: path, exactAmounts: nil)

                tokenOutAmountTotal = tokenOutAmountTotal + tokenOutVault.balance
                tokenOutReceiverRef!.deposit(from: <- tokenOutVault)

                path = []
                pathIndex = pathIndex + 1
            }
            i = i + 1
        }

        assert(tokenOutAmountTotal >= amountOutMin, message:
            SwapError.ErrorEncode(
                msg: "SLIPPAGE_OFFSET_TOO_LARGE expect min ".concat(amountOutMin.toString()).concat(" got ").concat(tokenOutAmountTotal.toString()),
                err: SwapError.ErrorCode.SLIPPAGE_OFFSET_TOO_LARGE
            )
        )
    }
}
```