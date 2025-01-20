# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/admin/upgrade_staking.cdc

```

transaction(code: [UInt8]) {

    prepare(acct: auth(UpdateContract) &Account) {
        acct.contracts.update(name: "FlowIDTableStaking", code: code)
    }
}
```