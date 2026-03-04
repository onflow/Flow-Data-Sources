# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/sign_terms.testnet.cdc

```
/// By signing this transaction you agree to our Term of Service here: https://docs.increment.fi/miscs/term-of-service.
transaction() {
    prepare(userAccount: auth(Storage) &Account) {
        userAccount.storage.load<Bool>(from: /storage/incrementFiTerms)
        userAccount.storage.save(true, to: /storage/incrementFiTerms)
    }
}
```