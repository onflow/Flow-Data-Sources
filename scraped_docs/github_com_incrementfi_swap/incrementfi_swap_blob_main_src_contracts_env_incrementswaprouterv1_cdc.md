# Source: https://github.com/IncrementFi/Swap/blob/main/src/contracts/env/IncrementSwapRouterV1.cdc

```
/**

# The router supports a chained swap trade among both uni-v2 style volatile pairs and stable pairs

# This is the updated version of SwapRouter.cdc, which includes support for increment stable pools.
# One of the enhancements is that the router now automatically selects the optimal quoting pool on-chain.
# This eliminates the complexity of choosing from a variety of pool types.

# The new router supports the generic Pool-Based DEX Swap Standard on Flow.
# It provides the following interface resources:
*   ImmediateSwap
*   ImmediateSwapQuotation
    
# Author: IncrementFi

*/
import DexSyncSwap from "./DexSyncSwap.cdc"

import FungibleToken from "./FungibleToken.cdc"
import SwapFactory from "../SwapFactory.cdc"
import StableSwapFactory from "../StableSwapFactory.cdc"
import SwapInterfaces from "../SwapInterfaces.cdc"
import SwapConfig from "../SwapConfig.cdc"
import SwapError from "../SwapError.cdc"

access(all) contract IncrementSwapRouterV1 {

    /// Swap event for Pool-Based DEX Swap Standard
    access(all) event Swap(
        receiverAddress: Address?,
        sourceTokenAmount: UFix64,
        receivedTargetTokenAmount: UFix64,
        sourceToken: Type,
        targetToken: Type
    )

    /// Flow Pool-Based DEX Swap Standards
    access(all) let immediateSwapQuotation: @ImmediateSwapQuotation
    access(all) let immediateSwap: @ImmediateSwap

    /// 
    access(all) resource ImmediateSwapQuotation: DexSyncSwap.ImmediateSwapQuotation {
        /// @notice Provides the quotation of the target token amount for the
        /// corresponding provided sell amount i.e amount of source tokens.
        ///
        /// If the source to target token path doesn't exists then below function
        /// would return `nil`.
        /// Below function would return the quoted amount after deduction of the fees.
        ///
        /// If the sourceToTargetTokenPath is [Type<FLOW>, Type<BLOCTO>]. 
        /// Where sourceToTargetTokenPath[0] is the source token while 
        /// sourceToTargetTokenPath[sourceToTargetTokenPath.length -1] is 
        /// target token. i.e. FLOW and BLOCTO respectively.
        ///
        /// @param sourceToTargetTokenPath: Offchain computed optimal path from
        ///                                 source token to target token.
        /// @param sourceAmount Amount of source token user wants to sell to buy target token.
        /// @return Amount of target token user would get after selling `sourceAmount`.
        ///
        access(all) fun getExactSellQuoteUsingPath(
            sourceToTargetTokenPath: [Type],
            sourceAmount: UFix64
        ): UFix64? {
            let tokenKeyPath: [String] = IncrementSwapRouterV1.convertTypeListToIdentifierList(typeList: sourceToTargetTokenPath)
            let amountOuts = IncrementSwapRouterV1.getAmountsOut(amountIn: sourceAmount, tokenKeyPath: tokenKeyPath)
            return (amountOuts == nil)? nil : amountOuts![amountOuts!.length-1]
        }

        /// @notice Provides the quotation of the source token amount if user wants to
        /// buy provided targetAmount, i.e. amount of target token.
        ///
        /// If the source to target token path doesn't exists then below function
        /// would return `nil`.
        /// Below function would return the quoted amount after deduction of the fees.
        ///
        /// If the sourceToTargetTokenPath is [Type<FLOW>, Type<BLOCTO>]. 
        /// Where sourceToTargetTokenPath[0] is the source token while 
        /// sourceToTargetTokenPath[sourceToTargetTokenPath.length -1] is 
        /// target token. i.e. FLOW and BLOCTO respectively.
        ///
        /// @param sourceToTargetTokenPath: Offchain computed optimal path from
        ///                                 source token to target token.
        /// @param targetAmount: Amount of target token user wants to buy.
        /// @return Amount of source token user has to pay to buy provided `targetAmount` of target token.
        ///
        access(all) fun getExactBuyQuoteUsingPath(
            sourceToTargetTokenPath: [Type],
            targetAmount: UFix64
        ): UFix64? {
            let tokenKeyPath: [String] = IncrementSwapRouterV1.convertTypeListToIdentifierList(typeList: sourceToTargetTokenPath)
            let amountOuts = IncrementSwapRouterV1.getAmountsIn(amountOut: targetAmount, tokenKeyPath: tokenKeyPath)
            return (amountOuts == nil)? nil : amountOuts![0]
        }

    }

    access(all) fun createImmediateSwapQuotation(): @ImmediateSwapQuotation {
        return <- create ImmediateSwapQuotation()
    }

    ///
    access(all) resource ImmediateSwap: DexSyncSwap.ImmediateSwap {

        /// @notice It will Swap the source token for the target token, In the below API, provided `sourceVault` would be consumed fully
        ///
        /// If the user wants to swap USDC to FLOW then the
        /// sourceToTargetTokenPath is [Type<USDC>, Type<FLOW>] and
        /// USDC would be the source token
        ///
        /// Necessary constraints
        /// - For the given source vault balance, Swapped target token amount should be
        ///   greater than or equal to `minimumTargetTokenAmount`, otherwise swap would fail.
        /// - If the swap settlement time i.e getCurrentBlock().timestamp is less than or
        ///   equal to the provided expiry then the swap would fail.
        /// - Provided `recipient` capability should be valid otherwise the swap would fail.
        /// - If the provided path doesn’t exists then the swap would fail.
        ///
        /// @param sourceToTargetTokenPath:   Off-chain computed path for reaching source token to target token
        ///                                   `sourceToTargetTokenPath[0]` should be the source token type while
        ///                                   `sourceToTargetTokenPath[sourceToTargetTokenPath.length - 1]` should be the target token
        ///                                    and all the remaining intermediaries token types would be necessary swap hops to swap the
        ///                                    source token with target token.
        /// @param sourceVault:                Vault that holds the source token.
        /// @param minimumTargetTokenAmount:   Minimum amount expected from the swap, If swapped amount is less than `minimumTargetTokenAmount`
        ///                                    then function execution would throw a error.
        /// @param expiry:                     Unix timestamp after which trade would get invalidated.
        /// @param recipient:                  A valid capability that receives target token after the completion of function execution.
        /// @return receivedTargetTokenAmount: Amount of tokens user would received after the swap
        access(all) fun swapExactSourceToTargetTokenUsingPath(
            sourceToTargetTokenPath: [Type],
            sourceVault: @{FungibleToken.Vault},
            minimumTargetTokenAmount: UFix64,
            expiry: UFix64,
            recipient: Capability<&{FungibleToken.Receiver}>,
        ): UFix64 {
            let tokenKeyPath: [String] = IncrementSwapRouterV1.convertTypeListToIdentifierList(typeList: sourceToTargetTokenPath)
            let sourceTokenAmount = sourceVault.balance

            let vaultOut <- IncrementSwapRouterV1.swapExactTokensForTokens(
                exactVaultIn: <- sourceVault,
                amountOutMin: minimumTargetTokenAmount,
                tokenKeyPath: tokenKeyPath,
                deadline: expiry
            )
            let amountOut = vaultOut.balance
            recipient.borrow()!.deposit(from: <- vaultOut)

            emit Swap(receiverAddress: recipient.address, sourceTokenAmount: sourceTokenAmount, receivedTargetTokenAmount: amountOut, sourceToken: sourceToTargetTokenPath[0], targetToken: sourceToTargetTokenPath[sourceToTargetTokenPath.length-1])
            return amountOut
        }

        /// @notice It will Swap the exact source token for to target token and          
        /// return `FungibleToken.Vault`
        ///
        /// If the user wants to swap USDC to FLOW then the
        /// sourceToTargetTokenPath is [Type<USDC>, Type<FLOW>] and
        /// USDC would be the source token.
        /// 
        /// This function would be more useful when smart contract is the function call initiator
        /// and wants to perform some actions using the receiving amount.
        ///
        /// Necessary constraints
        /// - For the given source vault balance, Swapped target token amount should be
        ///   greater than or equal to `minimumTargetTokenAmount`, otherwise swap would fail
        /// - If the swap settlement time i.e getCurrentBlock().timestamp is less than or equal to the provided expiry then the swap would fail
        /// - If the provided path doesn’t exists then the swap would fail.
        ///
        /// @param sourceToTargetTokenPath:  Off-chain computed path for reaching source token to target token
        ///                                 `sourceToTargetTokenPath[0]` should be the source token type while
        ///                                 `sourceToTargetTokenPath[sourceToTargetTokenPath.length - 1]` should be the target token
        ///                                  and all the remaining intermediaries token types would be necessary swap hops to swap the
        ///                                  source token with target token.
        /// @param sourceVault:              Vault that holds the source token.
        /// @param minimumTargetTokenAmount: Minimum amount expected from the swap, If swapped amount is less than `minimumTargetTokenAmount`
        ///                                  then function execution would throw a error.
        /// @param expiry:                   Unix timestamp after which trade would get invalidated.
        /// @return A valid vault that holds target token and an optional vault that may hold leftover source tokens.
        access(all) fun swapExactSourceToTargetTokenUsingPathAndReturn(
            sourceToTargetTokenPath: [Type],
            sourceVault: @{FungibleToken.Vault},
            minimumTargetTokenAmount: UFix64,
            expiry: UFix64
        ): @{FungibleToken.Vault} {
            let tokenKeyPath: [String] = IncrementSwapRouterV1.convertTypeListToIdentifierList(typeList: sourceToTargetTokenPath)
            let sourceTokenAmount = sourceVault.balance
            
            let vaultOut <- IncrementSwapRouterV1.swapExactTokensForTokens(
                exactVaultIn: <- sourceVault,
                amountOutMin: minimumTargetTokenAmount,
                tokenKeyPath: tokenKeyPath,
                deadline: expiry
            )

            emit Swap(receiverAddress: nil, sourceTokenAmount: sourceTokenAmount, receivedTargetTokenAmount: vaultOut.balance, sourceToken: sourceToTargetTokenPath[0], targetToken: sourceToTargetTokenPath[sourceToTargetTokenPath.length-1])
            return <- vaultOut
        }

        /// @notice It will Swap the source token for the target token while expected targetToken amount would be fixed
        ///
        /// If the user wants to swap USDC to FLOW then the
        /// sourceToTargetTokenPath is [Type<USDC>, Type<FLOW>] and
        /// USDC would be the source token
        ///
        /// Necessary constraints
        /// - For the given source vault balance, Swapped target token amount should be
        ///   equal to `exactTargetAmount`, otherwise swap would fail.
        /// - If the swap settlement time i.e getCurrentBlock().timestamp is less than or
        ///   equal to the provided expiry then the swap would fail.
        /// - Provided `recipient` capability should be valid otherwise the swap would fail.
        /// - If the provided path doesn’t exists then the swap would fail.
        ///
        /// @param sourceToTargetTokenPath:   Off-chain computed path for reaching source token to target token
        ///                                   `sourceToTargetTokenPath[0]` should be the source token type while
        ///                                   `sourceToTargetTokenPath[sourceToTargetTokenPath.length - 1]` should be the target token
        ///                                    and all the remaining intermediaries token types would be necessary swap hops to swap the
        ///                                    source token with target token.
        /// @param sourceVault:                Vault that holds the source token.
        /// @param exactTargetAmount:          Exact amount expected from the swap, If swapped amount is different from `exactTargetAmount`
        ///                                    then function execution would throw a error.
        /// @param expiry:                     Unix timestamp after which trade would get invalidated.
        /// @param recipient:                  A valid capability that receives target token after the completion of function execution.
        /// @param remainingSourceTokenRecipient: A valid capability that receives surplus source token after the completion of function execution.
        access(all) fun swapSourceToExactTargetTokenUsingPath(
            sourceToTargetTokenPath: [Type],
            sourceVault: @{FungibleToken.Vault},
            exactTargetAmount: UFix64,
            expiry: UFix64,
            recipient: Capability<&{FungibleToken.Receiver}>,
            remainingSourceTokenRecipient: Capability<&{FungibleToken.Receiver}>
        ): UFix64 {
            let tokenKeyPath: [String] = IncrementSwapRouterV1.convertTypeListToIdentifierList(typeList: sourceToTargetTokenPath)
            let sourceTokenAmount = sourceVault.balance
            let swapResVault <- IncrementSwapRouterV1.swapTokensForExactTokens(
                vaultInMax: <- sourceVault,
                exactAmountOut: exactTargetAmount,
                tokenKeyPath: tokenKeyPath,
                deadline: expiry
            )
            let vaultOut <- swapResVault.removeFirst()
            let vaultInLeft <- swapResVault.removeLast()
            destroy swapResVault

            let amountOut = vaultOut.balance
            recipient.borrow()!.deposit(from: <- vaultOut)
            remainingSourceTokenRecipient.borrow()!.deposit(from: <- vaultInLeft)
            
            emit Swap(receiverAddress: recipient.address, sourceTokenAmount: sourceTokenAmount, receivedTargetTokenAmount: amountOut, sourceToken: sourceToTargetTokenPath[0], targetToken: sourceToTargetTokenPath[sourceToTargetTokenPath.length-1])
            return amountOut
        }

        /// @notice It will Swap the source token for to target token and          
        /// return `ExactSwapAndReturnValue`
        ///
        /// If the user wants to swap USDC to FLOW then the
        /// sourceToTargetTokenPath is [Type<USDC>, Type<FLOW>] and
        /// USDC would be the source token.
        /// 
        /// This function would be more useful when smart contract is the function call initiator
        /// and wants to perform some actions using the receiving amount.
        ///
        /// Necessary constraints
        /// - For the given source vault balance, Swapped target token amount should be
        ///   greater than or equal to exactTargetAmount, otherwise swap would fail
        /// - If the swap settlement time i.e getCurrentBlock().timestamp is less than or equal to the provided expiry then the swap would fail
        /// - If the provided path doesn’t exists then the swap would fail.
        ///
        /// @param sourceToTargetTokenPath: Off-chain computed path for reaching source token to target token
        ///                                 `sourceToTargetTokenPath[0]` should be the source token type while
        ///                                 `sourceToTargetTokenPath[sourceToTargetTokenPath.length - 1]` should be the target token
        ///                                 and all the remaining intermediaries token types would be necessary swap hops to swap the
        ///                                 source token with target token.
        /// @param sourceVault:             Vault that holds the source token.
        /// @param exactTargetAmount:       Exact amount expected from the swap, If swapped amount is less than `exactTargetAmount` then
        ///                                 function execution would throw a error.
        /// @param expiry:                  Unix timestamp after which trade would get invalidated.
        /// @return A valid vault that holds target token and an optional vault that may hold leftover source tokens.
        ///     The way to unpack the return vault:
        ///         let targetVault <- res.targetTokenVault.withdraw(amount: res.targetTokenVault.balance)
        ///         let remainingVault <- res.remainingSourceTokenVault?.withdraw(amount: res.remainingSourceTokenVault?.balance!)!
        access(all) fun swapSourceToExactTargetTokenUsingPathAndReturn(
            sourceToTargetTokenPath: [Type],
            sourceVault: @{FungibleToken.Vault},
            exactTargetAmount: UFix64,
            expiry: UFix64
        ): @{DexSyncSwap.ExactSwapAndReturnValue} {
            let tokenKeyPath: [String] = IncrementSwapRouterV1.convertTypeListToIdentifierList(typeList: sourceToTargetTokenPath)
            let sourceTokenAmount = sourceVault.balance
            let swapResVault <- IncrementSwapRouterV1.swapTokensForExactTokens(
                vaultInMax: <- sourceVault,
                exactAmountOut: exactTargetAmount,
                tokenKeyPath: tokenKeyPath,
                deadline: expiry
            )
            let vaultOut <- swapResVault.removeFirst()
            let vaultInLeft <- swapResVault.removeLast()
            destroy swapResVault
            
            emit Swap(receiverAddress: nil, sourceTokenAmount: sourceTokenAmount, receivedTargetTokenAmount: vaultOut.balance, sourceToken: sourceToTargetTokenPath[0], targetToken: sourceToTargetTokenPath[sourceToTargetTokenPath.length-1])
            return <- create ExactSwapAndReturnValue(
                targetTokenVault: <- vaultOut,
                remainingSourceTokenVault: <- vaultInLeft
            )
        }
    }
    
    access(all) resource ExactSwapAndReturnValue: DexSyncSwap.ExactSwapAndReturnValue {
        access(all) let targetTokenVault: @{FungibleToken.Vault}
        access(all) let remainingSourceTokenVault: @{FungibleToken.Vault}?

        init(targetTokenVault: @{FungibleToken.Vault}, remainingSourceTokenVault: @{FungibleToken.Vault}?) {
            self.targetTokenVault <- targetTokenVault
            self.remainingSourceTokenVault <- remainingSourceTokenVault
        }
    }

    access(all) fun createImmediateSwap(): @ImmediateSwap {
        return <- create ImmediateSwap()
    }

    // Perform a chained swap calculation starting with exact amountIn
    //
    // @Param  - amountIn:     e.g. 50.0
    // @Param  - tokenKeyPath: e.g. ["A.f8d6e0586b0a20c7.FUSD", "A.f8d6e0586b0a20c7.FlowToken", "A.f8d6e0586b0a20c7.USDC"]
    // @Return - [UFix64]:     e.g. [50.0, 10.0, 48.0]
    access(all) fun getAmountsOut(amountIn: UFix64, tokenKeyPath: [String]): [UFix64]? {
        pre {
            tokenKeyPath.length >= 2: SwapError.ErrorEncode(msg: "SwapRouter: Invalid path", err: SwapError.ErrorCode.INVALID_PARAMETERS)
        }
        var amounts: [UFix64] = []
        amounts.append(amountIn)
        var i: Int = 0
        while (i < tokenKeyPath.length-1) {
            var amountOut: UFix64? = nil
            // volatile pool
            let volatilePairAddr = SwapFactory.getPairAddress(token0Key: tokenKeyPath[i], token1Key: tokenKeyPath[i+1])
            if volatilePairAddr != nil {
                let poolPublicRef = getAccount(volatilePairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                let poolInfo = poolPublicRef.getPairInfo()
                if (poolInfo[2] as! UFix64) > 0.0 {
                    let curAmountOut = poolPublicRef.getAmountOut(amountIn: amounts[i], tokenInKey: tokenKeyPath[i])
                    if amountOut == nil || curAmountOut > amountOut! {
                        amountOut = curAmountOut
                    }
                }
            }
            // stable pool
            let stablePairAddr = StableSwapFactory.getPairAddress(token0Key: tokenKeyPath[i], token1Key: tokenKeyPath[i+1])
            if stablePairAddr != nil {
                let poolPublicRef = getAccount(stablePairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                let poolInfo = poolPublicRef.getPairInfo()
                if (poolInfo[2] as! UFix64) > 0.0 {
                    let curAmountOut = poolPublicRef.getAmountOut(amountIn: amounts[i], tokenInKey: tokenKeyPath[i])
                    if amountOut == nil || curAmountOut > amountOut! {
                        amountOut = curAmountOut
                    }
                }
            }
            if (amountOut == nil) { return nil }
            amounts.append(amountOut!)
            i = i + 1
        }
        return amounts
    }

    /// Perform a chained swap calculation end with exact amountOut
    access(all) fun getAmountsIn(amountOut: UFix64, tokenKeyPath: [String]): [UFix64]? {
        pre {
            tokenKeyPath.length >= 2: SwapError.ErrorEncode(msg: "SwapRouter: Invalid path", err: SwapError.ErrorCode.INVALID_PARAMETERS)
        }
        var amounts: [UFix64] = []
        for tokenKey in tokenKeyPath {
            amounts.append(0.0)
        }
        amounts[amounts.length-1] = amountOut
        var i: Int = tokenKeyPath.length-1
        while (i > 0) {
            var amountIn: UFix64? = nil
            // volatile pool
            let volatilePairAddr = SwapFactory.getPairAddress(token0Key: tokenKeyPath[i], token1Key: tokenKeyPath[i-1])
            if volatilePairAddr != nil {
                let poolPublicRef = getAccount(volatilePairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                let poolInfo = poolPublicRef.getPairInfo()
                let tokenOutReserve = ((poolInfo[0] as! String)==tokenKeyPath[i])? (poolInfo[2] as! UFix64) : (poolInfo[3] as! UFix64)
                if (poolInfo[2] as! UFix64) > 0.0 && tokenOutReserve > amounts[i] {
                    let curAmountIn = poolPublicRef.getAmountIn(amountOut: amounts[i], tokenOutKey: tokenKeyPath[i])
                    if amountIn == nil || curAmountIn < amountIn! {
                        amountIn = curAmountIn
                    }
                }
            }
            // stable pool
            let stablePairAddr = StableSwapFactory.getPairAddress(token0Key: tokenKeyPath[i], token1Key: tokenKeyPath[i-1])
            if stablePairAddr != nil {
                let poolPublicRef = getAccount(stablePairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
                let poolInfo = poolPublicRef.getPairInfo()
                let tokenOutReserve = ((poolInfo[0] as! String)==tokenKeyPath[i])? (poolInfo[2] as! UFix64) : (poolInfo[3] as! UFix64)
                if (poolInfo[2] as! UFix64) > 0.0 && tokenOutReserve > amounts[i] {
                    let curAmountIn = poolPublicRef.getAmountIn(amountOut: amounts[i], tokenOutKey: tokenKeyPath[i])
                    if amountIn == nil || curAmountIn < amountIn! {
                        amountIn = curAmountIn
                    }
                }
            }
            if (amountIn == nil) { return nil }
            /// Calculate from back to front
            amounts[i-1] = amountIn!
            i = i - 1
        }
        return amounts
    }    


    /// SwapExactTokensForTokens
    ///
    /// Make sure the exact amountIn in swap start
    /// @Param  - exactVaultIn: Vault with exact amountIn
    /// @Param  - amountOutMin: Desired minimum amountOut to do slippage check
    /// @Param  - tokenKeyPath: Chained swap
    ///                         e.g. if swap from FUSD to USDC through FlowToken
    ///                              [A.f8d6e0586b0a20c7.FUSD, A.f8d6e0586b0a20c7.FlowToken, A.f8d6e0586b0a20c7.USDC]
    /// @Param  - deadline:     The timeout block timestamp for the transaction
    /// @Return - Vault:        outVault
    access(all) fun swapExactTokensForTokens(
        exactVaultIn: @{FungibleToken.Vault},
        amountOutMin: UFix64,
        tokenKeyPath: [String],
        deadline: UFix64
    ): @{FungibleToken.Vault} {
        assert(deadline >= getCurrentBlock().timestamp, message:
            SwapError.ErrorEncode(
                msg: "SwapRouter: expired",
                err: SwapError.ErrorCode.EXPIRED
            )
        )
        let amounts = self.getAmountsOut(amountIn: exactVaultIn.balance, tokenKeyPath: tokenKeyPath)
        assert(amounts![amounts!.length-1] >= amountOutMin, message:
            SwapError.ErrorEncode(
                msg: "SwapRouter: INSUFFICIENT_OUTPUT_AMOUNT",
                err: SwapError.ErrorCode.INSUFFICIENT_OUTPUT_AMOUNT
            )
        )
        return <- self.swapWithPath(vaultIn: <-exactVaultIn, tokenKeyPath: tokenKeyPath, exactAmounts: nil)
    }

    /// SwapTokensForExactTokens
    ///
    /// @Param  - vaultInMax:     Vault with enough input to swap, checks slippage
    /// @Param  - exactAmountOut: Make sure the exact amountOut in swap end
    /// @Param  - tokenKeyPath:   Chained swap
    ///                           e.g. if swap from FUSD to USDC through FlowToken
    ///                                [A.f8d6e0586b0a20c7.FUSD, A.f8d6e0586b0a20c7.FlowToken, A.f8d6e0586b0a20c7.USDC]
    /// @Param  - deadline:       The timeout block timestamp for the transaction
    /// @Return - [OutVault, RemainingInVault]
    access(all) fun swapTokensForExactTokens(
        vaultInMax: @{FungibleToken.Vault},
        exactAmountOut: UFix64,
        tokenKeyPath: [String],
        deadline: UFix64
    ): @[{FungibleToken.Vault}] {
        assert(deadline >= getCurrentBlock().timestamp, message:
            SwapError.ErrorEncode(
                msg: "SwapRouter: expired",
                err: SwapError.ErrorCode.EXPIRED
            )
        )
        let amountInMax = vaultInMax.balance
        let amounts = self.getAmountsIn(amountOut: exactAmountOut, tokenKeyPath: tokenKeyPath)
        assert(amounts![0] <= amountInMax, message:
            SwapError.ErrorEncode(
                msg: "SwapRouter: EXCESSIVE_INPUT_AMOUNT",
                err: SwapError.ErrorCode.EXCESSIVE_INPUT_AMOUNT
            )
        )
        let vaultInExact <- vaultInMax.withdraw(amount: amounts![0])

        return <- [
            <- self.swapWithPath(vaultIn: <-vaultInExact, tokenKeyPath: tokenKeyPath, exactAmounts: amounts),
            <- vaultInMax
        ]
    }
    
    ///
    access(all) fun swapWithPair(
        vaultIn: @{FungibleToken.Vault},
        exactAmountOut: UFix64?,
        tokenInKey: String,
        tokenOutKey: String
    ): @{FungibleToken.Vault} {
        let amountIn = vaultIn.balance

        var maxAmountOut: UFix64? = nil
        var maxOutPoolRef: &{SwapInterfaces.PairPublic}? = nil 
        // volatile pool
        let volatilePairAddr = SwapFactory.getPairAddress(token0Key: tokenInKey, token1Key: tokenOutKey)
        if volatilePairAddr != nil {
            let poolPublicRef = getAccount(volatilePairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
            let curAmountOut = poolPublicRef.getAmountOut(amountIn: amountIn, tokenInKey: tokenInKey)
            if maxAmountOut == nil || curAmountOut > maxAmountOut! {
                maxAmountOut = curAmountOut
                maxOutPoolRef = poolPublicRef
            }
        }
        // stable pool
        let stablePairAddr = StableSwapFactory.getPairAddress(token0Key: tokenInKey, token1Key: tokenOutKey)
        if stablePairAddr != nil {
            let poolPublicRef = getAccount(stablePairAddr!).capabilities.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)!
            let curAmountOut = poolPublicRef.getAmountOut(amountIn: amountIn, tokenInKey: tokenInKey)
            if maxAmountOut == nil || curAmountOut > maxAmountOut! {
                maxAmountOut = curAmountOut
                maxOutPoolRef = poolPublicRef
            }
        }

        return <- maxOutPoolRef!.swap(vaultIn: <- vaultIn, exactAmountOut: exactAmountOut)
    }
    
    ///
    access(all) fun swapWithPath(vaultIn: @{FungibleToken.Vault}, tokenKeyPath: [String], exactAmounts: [UFix64]?): @{FungibleToken.Vault} {
        pre {
            tokenKeyPath.length >= 2: SwapError.ErrorEncode(msg: "Invalid path.", err: SwapError.ErrorCode.INVALID_PARAMETERS)
        }
        /// To reduce the gas cost, handle the first five swap out of the loop
        var exactAmountOut1: UFix64? = nil
        if exactAmounts != nil { exactAmountOut1 = exactAmounts![1] }
        let vaultOut1 <- self.swapWithPair(vaultIn: <- vaultIn, exactAmountOut: exactAmountOut1, tokenInKey: tokenKeyPath[0], tokenOutKey: tokenKeyPath[1])
        if tokenKeyPath.length == 2 {
            return <-vaultOut1
        }

        var exactAmountOut2: UFix64? = nil
        if exactAmounts != nil { exactAmountOut2 = exactAmounts![2] }
        let vaultOut2 <- self.swapWithPair(vaultIn: <- vaultOut1, exactAmountOut: exactAmountOut2, tokenInKey: tokenKeyPath[1], tokenOutKey: tokenKeyPath[2])
        if tokenKeyPath.length == 3 {
            return <-vaultOut2
        }

        var exactAmountOut3: UFix64? = nil
        if exactAmounts != nil { exactAmountOut3 = exactAmounts![3] }
        let vaultOut3 <- self.swapWithPair(vaultIn: <- vaultOut2, exactAmountOut: exactAmountOut3, tokenInKey: tokenKeyPath[2], tokenOutKey: tokenKeyPath[3])
        if tokenKeyPath.length == 4 {
            return <-vaultOut3
        }

        var exactAmountOut4: UFix64? = nil
        if exactAmounts != nil { exactAmountOut4 = exactAmounts![4] }
        let vaultOut4 <- self.swapWithPair(vaultIn: <- vaultOut3, exactAmountOut: exactAmountOut4, tokenInKey: tokenKeyPath[3], tokenOutKey: tokenKeyPath[4])
        if tokenKeyPath.length == 5 {
            return <-vaultOut4
        }
        /// Loop swap for any length path
        var index = 4
        var curVaultOut <- vaultOut4
        while(index < tokenKeyPath.length-1) {
            var inVault <- curVaultOut.withdraw(amount: curVaultOut.balance)
            
            var exactAmountOut: UFix64? = nil
            if exactAmounts != nil { exactAmountOut = exactAmounts![index+1] }
            var out <- self.swapWithPair(vaultIn: <- inVault, exactAmountOut: exactAmountOut, tokenInKey: tokenKeyPath[index], tokenOutKey:tokenKeyPath[index+1])
            curVaultOut <-> out

            destroy out
            index = index + 1
        }
    
        return <-curVaultOut
    }

    access(all) fun convertTypeListToIdentifierList(typeList: [Type]): [String] {
        let identifierList: [String] = []
        for tokenType in typeList {
            identifierList.append(tokenType.identifier)
        }
        return identifierList
    }

    init() {
        self.immediateSwapQuotation <- create ImmediateSwapQuotation()
        self.immediateSwap <- create ImmediateSwap()
    }
}
```