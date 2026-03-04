# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/user/sign_terms.mainnet.cdc

```
/// By signing this transaction you agree to our Term of Service here: https://docs.increment.fi/miscs/term-of-service.
import LogEntry from "../../contracts/env/LogEntry.cdc"  // Mainnet deployment addr: 0xe876e00638d54e75

transaction() {
    prepare(userAccount: auth(Storage) &Account) {
        userAccount.storage.load<Bool>(from: /storage/incrementFiTerms)
        userAccount.storage.save(true, to: /storage/incrementFiTerms)
        LogEntry.LogAgreement(addr: userAccount.address)
    }
}
```