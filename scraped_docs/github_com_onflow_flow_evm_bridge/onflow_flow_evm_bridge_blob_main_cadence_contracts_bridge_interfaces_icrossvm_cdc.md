# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/contracts/bridge/interfaces/ICrossVM.cdc

```
import "EVM"

/// Contract interface denoting a cross-VM implementation, exposing methods to query EVM-associated addresses
///
access(all)
contract interface ICrossVM {

    /// Retrieves the corresponding EVM contract address, assuming a 1:1 relationship between VM implementations
    ///
    access(all)
    view fun getEVMContractAddress(): EVM.EVMAddress
}

```