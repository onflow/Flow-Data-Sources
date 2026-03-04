# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/hw_v1_storage_check.cdc

```
access(all) fun main(account: Address): {String: AnyStruct} {
    
    let vaultStatus: {String: AnyStruct} = {}  
    
    vaultStatus.insert(key: "FlowBalance", getAccount(account).balance)
    vaultStatus.insert(key: "availableFlowBalance", getAccount(account).availableBalance)
    vaultStatus.insert(key: "storageUsed", getAccount(account).storage.used)
    vaultStatus.insert(key: "storageCapacity", getAccount(account).storage.capacity)

    return vaultStatus
}

```