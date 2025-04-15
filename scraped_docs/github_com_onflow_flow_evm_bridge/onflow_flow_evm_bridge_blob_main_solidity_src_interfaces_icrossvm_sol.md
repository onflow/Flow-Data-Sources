# Source: https://github.com/onflow/flow-evm-bridge/blob/main/solidity/src/interfaces/ICrossVM.sol

```
pragma solidity 0.8.24;

interface ICrossVM {
    function getCadenceAddress() external view returns (string memory);
    function getCadenceIdentifier() external view returns (string memory);
}

```