# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/evm-bridging/cadence/transactions/admin/set_up_royalty_management.cdc

```
import "EVM"

/// Sets up royalty management for an ERC721 contract
///
/// @param erc721C - The EVM address of the ERC721 contract
/// @param validator - The EVM address of the validator contract
/// @param royaltyRecipient - The EVM address of the royalty recipient
/// @param royaltyBasisPoints - The royalty basis points (0-10000)
transaction(
    erc721C: String,
    validator: String,
    royaltyRecipient: String,
    royaltyBasisPoints: UInt128,
) {
    prepare(signer: auth(BorrowValue) &Account) {
        // Borrow COA from signer's account storage
        let coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: /storage/evm)
            ?? panic("Could not find coa in signer's account.")

        // Set validator contract
        mustCall(coa, EVM.addressFromString(erc721C),
            functionSig: "setTransferValidator(address)",
            args: [EVM.addressFromString(validator)]
        )

        // Set royalty info
        mustCall(coa, EVM.addressFromString(erc721C),
            functionSig: "setRoyaltyInfo((address,uint96))",
            args: [EVM.addressFromString(royaltyRecipient), royaltyBasisPoints]
        )
    }
}

/// Calls a function on an EVM contract from provided coa
///
access(all) fun mustCall(
    _ coa: auth(EVM.Call) &EVM.CadenceOwnedAccount,
    _ contractAddr: EVM.EVMAddress,
    functionSig: String,
    args: [AnyStruct]
): EVM.Result {
    let res = coa.call(
        to: contractAddr,
        data: EVM.encodeABIWithSignature(functionSig, args),
        gasLimit: 4_000_000,
        value: EVM.Balance(attoflow: 0)
    )

    assert(res.status == EVM.Status.successful,
        message: "Failed to call '".concat(functionSig)
            .concat("\n\t error code: ").concat(res.errorCode.toString())
            .concat("\n\t error message: ").concat(res.errorMessage)
            .concat("\n\t gas used: ").concat(res.gasUsed.toString())
            .concat("\n\t args count: ").concat(args.length.toString())
            .concat("\n\t caller address: 0x").concat(coa.address().toString())
            .concat("\n\t contract address: 0x").concat(contractAddr.toString())
    )

    return res
}

```