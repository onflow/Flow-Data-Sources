# Source: https://github.com/onflow/flow-nft/blob/master/tests/transactions/upgrade_nft_contract.cdc

```

transaction(code: [UInt8]) {

    prepare(acct: auth(UpdateContract) &Account) {

        acct.contracts.update__experimental(name: "NonFungibleToken", code: code)
    }
}
```