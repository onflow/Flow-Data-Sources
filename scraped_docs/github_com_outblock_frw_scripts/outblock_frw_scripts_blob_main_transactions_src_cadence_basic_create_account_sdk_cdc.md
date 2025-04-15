# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/basic/create_account_sdk.cdc

```
import Crypto

transaction(publicKey: String, signatureAlgorithm: UInt8, hashAlgorithm: UInt8, weight: UFix64, contracts: {String: String}) {
    prepare(signer: auth(BorrowValue | Storage) &Account) {
        let account = Account(payer: signer)

        let key = PublicKey(
            publicKey: publicKey.decodeHex(),
            signatureAlgorithm: SignatureAlgorithm(rawValue: signatureAlgorithm)!
        )

        account.keys.add(
            publicKey: key,
            hashAlgorithm: HashAlgorithm(rawValue: hashAlgorithm)!,
            weight: weight
        )

        for contract in contracts.keys {
            account.contracts.add(name: contract, code: contracts[contract]!.decodeHex())
        }
    }
}
```