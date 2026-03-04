# Source: https://github.com/IncrementFi/Oracle/blob/main/cadence/transactions/tool/deploy_by_template.cdc

```
import OracleInterface from "../../contracts/OracleInterface.cdc"
import OracleConfig from "../../contracts/OracleConfig.cdc"

// deploy code copied by a deployed contract
transaction(codeAddr: Address, codeName: String) {
    prepare(deployAccount: auth(AddContract) &Account) {
        let code = getAccount(codeAddr).contracts.get(name: codeName)!.code
        deployAccount.contracts.add(name: codeName, code: code)
    }
}
```