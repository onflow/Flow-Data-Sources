# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/transactions/deploy_using_evm_deployer.cdc

```
import "EVMDeployer"

transaction(name: String, bytecode: String, value: UInt) {
    prepare(signer: &Account) {}

    execute {
        EVMDeployer.deploy(name: name, bytecode: bytecode, value: value)
    }
}

```