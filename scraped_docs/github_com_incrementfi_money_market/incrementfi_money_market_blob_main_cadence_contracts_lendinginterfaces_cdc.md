# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/contracts/LendingInterfaces.cdc

```
/**

# Lending related interface definitions all-in-one

# Author: Increment Labs

*/
import FungibleToken from "./tokens/FungibleToken.cdc"

access(all) contract interface LendingInterfaces {
    
    access(all) resource interface PoolPublic {
        access(all) view fun getPoolAddress(): Address
        access(all) view fun getUnderlyingTypeString(): String
        access(all) view fun getUnderlyingAssetType(): String
        access(all) view fun getUnderlyingToLpTokenRateScaled(): UInt256
        access(all) view fun getAccountLpTokenBalanceScaled(account: Address): UInt256
        /// Return snapshot of account borrowed balance in scaled UInt256 format
        access(all) view fun getAccountBorrowBalanceScaled(account: Address): UInt256
        /// Return: [scaledExchangeRate, scaledLpTokenBalance, scaledBorrowBalance, scaledAccountBorrowPrincipal, scaledAccountBorrowIndex]
        access(all) view fun getAccountSnapshotScaled(account: Address): [UInt256; 5]
        access(all) view fun getAccountRealtimeScaled(account: Address): [UInt256; 5]
        access(all) view fun getInterestRateModelAddress(): Address
        access(all) view fun getPoolReserveFactorScaled(): UInt256
        access(all) view fun getPoolAccrualBlockNumber(): UInt256
        access(all) view fun getPoolTotalBorrowsScaled(): UInt256
        access(all) view fun getPoolBorrowIndexScaled(): UInt256
        access(all) view fun getPoolTotalSupplyScaled(): UInt256
        access(all) view fun getPoolCash(): UInt256
        access(all) view fun getPoolTotalLpTokenSupplyScaled(): UInt256
        access(all) view fun getPoolTotalReservesScaled(): UInt256
        access(all) view fun getPoolBorrowRateScaled(): UInt256
        access(all) view fun getPoolSupplyAprScaled(): UInt256
        access(all) view fun getPoolBorrowAprScaled(): UInt256
        access(all) view fun getPoolSupplierCount(): UInt256
        access(all) view fun getPoolBorrowerCount(): UInt256
        access(all) view fun getPoolSupplierList(): [Address]
        access(all) view fun getPoolBorrowerList(): [Address]
        access(all) view fun getPoolSupplierSlicedList(from: UInt64, to: UInt64): [Address]
        access(all) view fun getPoolBorrowerSlicedList(from: UInt64, to: UInt64): [Address]
        access(all) view fun getFlashloanRateBps(): UInt64
        
        /// Accrue pool interest and checkpoint latest data to pool states
        access(all) fun accrueInterest()
        access(all) view fun accrueInterestReadonly(): [UInt256; 4]
        access(all) view fun getPoolCertificateType(): Type
        /// Note: Check to ensure @callerPoolCertificate's run-time type is another LendingPool's.IdentityCertificate,
        /// so that this public seize function can only be invoked by another LendingPool contract
        access(all) fun seize(
            seizerPoolCertificate: @{LendingInterfaces.IdentityCertificate},
            seizerPool: Address,
            liquidator: Address,
            borrower: Address,
            scaledBorrowerCollateralLpTokenToSeize: UInt256
        )

        access(all) fun supply(supplierAddr: Address, inUnderlyingVault: @{FungibleToken.Vault})
        access(all) fun redeem(userCertificate: &{LendingInterfaces.IdentityCertificate}, numLpTokenToRedeem: UFix64): @{FungibleToken.Vault}
        access(all) fun redeemUnderlying(userCertificate: &{LendingInterfaces.IdentityCertificate}, numUnderlyingToRedeem: UFix64): @{FungibleToken.Vault}
        access(all) fun borrow(userCertificate: &{LendingInterfaces.IdentityCertificate}, borrowAmount: UFix64): @{FungibleToken.Vault}
        access(all) fun repayBorrow(borrower: Address, repayUnderlyingVault: @{FungibleToken.Vault}): @{FungibleToken.Vault}?
        access(all) fun liquidate(liquidator: Address, borrower: Address, poolCollateralizedToSeize: Address, repayUnderlyingVault: @{FungibleToken.Vault}): @{FungibleToken.Vault}?
        access(all) fun flashloan(executor: &{LendingInterfaces.FlashLoanExecutor}, requestedAmount: UFix64, params: {String: AnyStruct}) {return}
    }

    access(all) resource interface PoolAdminPublic {
        access(all) fun setInterestRateModel(newInterestRateModelAddress: Address)
        access(all) fun setReserveFactor(newReserveFactor: UFix64)
        access(all) fun setPoolSeizeShare(newPoolSeizeShare: UFix64)
        access(all) fun setComptroller(newComptrollerAddress: Address)
        /// A pool can only be initialized once
        access(all) fun initializePool(reserveFactor: UFix64, poolSeizeShare: UFix64, interestRateModelAddress: Address)
        access(all) fun withdrawReserves(reduceAmount: UFix64): @{FungibleToken.Vault}
        access(all) fun setFlashloanRateBps(rateBps: UInt64)
        access(all) fun setFlashloanOpen(isOpen: Bool)
    }

    access(all) resource interface FlashLoanExecutor {
        access(all) fun executeAndRepay(loanedToken: @{FungibleToken.Vault}, params: {String: AnyStruct}): @{FungibleToken.Vault}
    }
    
    access(all) resource interface InterestRateModelPublic {
        /// exposing model specific fields, e.g.: modelName, model params.
        access(all) view fun getInterestRateModelParams(): {String: AnyStruct}
        /// pool's capital utilization rate (scaled up by scaleFactor, e.g. 1e18)
        access(all) view fun getUtilizationRate(cash: UInt256, borrows: UInt256, reserves: UInt256): UInt256
        /// Get the borrow interest rate per block (scaled up by scaleFactor, e.g. 1e18)
        access(all) view fun getBorrowRate(cash: UInt256, borrows: UInt256, reserves: UInt256): UInt256
        /// Get the supply interest rate per block (scaled up by scaleFactor, e.g. 1e18)
        access(all) view fun getSupplyRate(cash: UInt256, borrows: UInt256, reserves: UInt256, reserveFactor: UInt256): UInt256
        /// Get the number of blocks per year.
        access(all) view fun getBlocksPerYear(): UInt256
    }

    /// IdentityCertificate resource which is used to identify account address or perform caller authentication
    access(all) resource interface IdentityCertificate {}

    access(all) resource interface OraclePublic {
        /// Get the given pool's underlying asset price denominated in USD.
        /// Note: Return value of 0.0 means the given pool's price feed is not available.
        access(all) view fun getUnderlyingPrice(pool: Address): UFix64

        /// Return latest reported data in [timestamp, priceData]
        access(all) view fun latestResult(pool: Address): [UFix64; 2]

        /// Return supported markets' addresses
        access(all) view fun getSupportedFeeds(): [Address]
    }

    access(all) resource interface ComptrollerPublic {
        /// Return error string on condition (or nil)
        access(all) fun supplyAllowed(
            poolCertificate: @{LendingInterfaces.IdentityCertificate},
            poolAddress: Address,
            supplierAddress: Address,
            supplyUnderlyingAmountScaled: UInt256
        ): String?

        access(all) fun redeemAllowed(
            poolCertificate: @{LendingInterfaces.IdentityCertificate},
            poolAddress: Address,
            redeemerAddress: Address,
            redeemLpTokenAmountScaled: UInt256
        ): String?

        access(all) fun borrowAllowed(
            poolCertificate: @{LendingInterfaces.IdentityCertificate},
            poolAddress: Address,
            borrowerAddress: Address,
            borrowUnderlyingAmountScaled: UInt256
        ): String?
        
        access(all) fun repayAllowed(
            poolCertificate: @{LendingInterfaces.IdentityCertificate},
            poolAddress: Address,
            borrowerAddress: Address,
            repayUnderlyingAmountScaled: UInt256
        ): String?

        access(all) fun liquidateAllowed(
            poolCertificate: @{LendingInterfaces.IdentityCertificate},
            poolBorrowed: Address,
            poolCollateralized: Address,
            borrower: Address,
            repayUnderlyingAmountScaled: UInt256
        ): String?

        access(all) fun seizeAllowed(
            poolCertificate: @{LendingInterfaces.IdentityCertificate},
            borrowPool: Address,
            collateralPool: Address,
            liquidator: Address,
            borrower: Address,
            seizeCollateralPoolLpTokenAmountScaled: UInt256
        ): String?

        access(all) fun callerAllowed(
            callerCertificate: @{LendingInterfaces.IdentityCertificate},
            callerAddress: Address
        ): String?

        access(all) fun calculateCollateralPoolLpTokenToSeize(
            borrower: Address,
            borrowPool: Address,
            collateralPool: Address,
            actualRepaidBorrowAmountScaled: UInt256
        ): UInt256

        access(all) view fun getUserCertificateType(): Type
        access(all) view fun getPoolPublicRef(poolAddr: Address): &{PoolPublic}
        access(all) view fun getAllMarkets(): [Address]
        access(all) view fun getMarketInfo(poolAddr: Address): {String: AnyStruct}
        access(all) view fun getUserMarkets(userAddr: Address): [Address]
        access(all) view fun getUserCrossMarketLiquidity(userAddr: Address): [String; 3]
        access(all) view fun getUserMarketInfo(userAddr: Address, poolAddr: Address): {String: AnyStruct}
    }
}
```