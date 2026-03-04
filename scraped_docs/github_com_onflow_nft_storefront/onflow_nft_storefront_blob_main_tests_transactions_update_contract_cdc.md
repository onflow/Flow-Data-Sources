# Source: https://github.com/onflow/nft-storefront/blob/main/tests/transactions/update_contract.cdc

```
transaction(name: String, code: String) {
	prepare(signer: auth(Contracts) &Account) {
		signer.contracts.update(name: name, code: code.decodeHex())
	}
}
```