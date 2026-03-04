# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/admin/set_protocol_fee.cdc

```
import LiquidStakingConfig from "../../contracts/LiquidStakingConfig.cdc"

transaction(newProtocolCut: UFix64) {
    prepare(signer: auth(BorrowValue) &Account) {
        let adminRef = signer.storage.borrow<&LiquidStakingConfig.Admin>(from: LiquidStakingConfig.adminPath)
            ?? panic("cannot borrow reference to Liquid Staking Admin")
        adminRef.setProtocolFee(protocolFee: newProtocolCut)
    }
}
```