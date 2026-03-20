# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/FlowServiceAccount/add_fee_child_accounts.cdc

```
transaction(accounts: Int) {
    prepare(admin: auth(Storage, BorrowValue, UpdateContract) &Account) {
       let feeChildAccounts: [Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>] =
            admin.storage.load<[Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>]>(from: /storage/ChildFeeAccounts) ?? []

        var i = 0
        while i < accounts {
            i = i + 1
            let acc = Account(payer: admin)
            let cap = acc.capabilities
                .account
                .issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>()

            feeChildAccounts.append(cap)
        }

        admin.storage.save<[Capability<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>]>(feeChildAccounts, to: /storage/ChildFeeAccounts)
    }
}

```