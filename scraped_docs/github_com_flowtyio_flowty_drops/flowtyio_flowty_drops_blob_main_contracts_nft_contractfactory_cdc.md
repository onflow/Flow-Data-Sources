# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/nft/ContractFactory.cdc

```
import "ContractFactoryTemplate"
import "AddressUtils"

access(all) contract ContractFactory {
    access(all) fun createContract(templateType: Type, acct: auth(Contracts) &Account, name: String, params: {String: AnyStruct}, initializeIdentifier: String) {
        let templateAddr = AddressUtils.parseAddress(templateType)!
        let contractName = templateType.identifier.split(separator: ".")[2]
        let templateContract = getAccount(templateAddr).contracts.borrow<&{ContractFactoryTemplate}>(name: contractName)
            ?? panic("provided type is not a ContractTemplateFactory")
        
        templateContract.createContract(acct: acct, name: name, params: params, initializeIdentifier: initializeIdentifier)
    }
}
```