# Source: https://github.com/Noah-Overflow/Cadence-Arch-example/blob/main/foundry/src/Counter.sol

```
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Counter {
    uint256 public number;

    function setNumber(uint256 newNumber) public {
        number = newNumber;
    }

    function increment() public {
        number++;
    }
}

```