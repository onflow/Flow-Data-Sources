# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/register_key.cdc

```
import Crypto

/*
[
	ac915cf356a8da0adbd6fb7bed6e4d7c6b3a6a5a3afd933aadb09bddda246acc7700ebcac5aa113646e5c6b0409890ebafa14b9160cdde0b7f96fde2e1ab72d3: String,
	1: UInt8,
	3: UInt8,
	1000.00000000: UFix64
]
*/

transaction(publicKey: String, signatureAlgorithm: UInt8, hashAlgorithm: UInt8, weight: UFix64) {
    prepare(signer: auth(Keys) &Account) {
        let key = PublicKey(
            publicKey: publicKey.decodeHex(),
            signatureAlgorithm: SignatureAlgorithm(rawValue: signatureAlgorithm)!
        )

        signer.keys.add(
            publicKey: key,
            hashAlgorithm: HashAlgorithm(rawValue: hashAlgorithm)!,
            weight: weight
        )
    }   
}
```