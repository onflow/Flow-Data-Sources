# Source: https://github.com/onflow/flow-evm-bridge/blob/main/solidity/src/interfaces/CrossVM.sol

```
// SPDX-License-Identifier: Unlicense
pragma solidity 0.8.24;

import {ICrossVM} from "./ICrossVM.sol";

abstract contract CrossVM is ICrossVM {
    string internal cadenceAddress;
    string internal cadenceIdentifier;

    constructor(string memory cadenceAddress_, string memory cadenceIdentifier_) {
        cadenceAddress = cadenceAddress_;
        cadenceIdentifier = cadenceIdentifier_;
    }

    function getCadenceAddress() external view returns (string memory) {
        return cadenceAddress;
    }

    function getCadenceIdentifier() external view returns (string memory) {
        return cadenceIdentifier;
    }
}

```