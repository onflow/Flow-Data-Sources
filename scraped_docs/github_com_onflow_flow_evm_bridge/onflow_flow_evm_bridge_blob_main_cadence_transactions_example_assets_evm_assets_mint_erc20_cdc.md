# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/transactions/example-assets/evm-assets/mint_erc20.cdc

```
import "EVM"

transaction(
    recipientHexAddress: String,
    amount: UInt256,
    erc20HexAddress: String,
    gasLimit: UInt64
) {
    
    let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount
    
    prepare(signer: auth(BorrowValue) &Account) {
        self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: /storage/evm)
            ?? panic("Signer does not have a COA in storage")
    }

    execute {
        let recipientAddress = EVM.addressFromString(recipientHexAddress)
        let erc20Address = EVM.addressFromString(erc20HexAddress)
        let calldata = EVM.encodeABIWithSignature(
            "mint(address,uint256)",
            [recipientAddress, amount]
        )
        let callResult = self.coa.call(
            to: erc20Address,
            data: calldata,
            gasLimit: gasLimit,
            value: EVM.Balance(attoflow: 0)
        )
        assert(callResult.status == EVM.Status.successful, message: "ERC20 mint failed with code: ".concat(callResult.errorCode.toString()))
    }
}

```