# Source: https://github.com/Noah-Overflow/Cadence-Arch-example/blob/main/foundry/src/CadenceArch.sol

```
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract CadenceArchCaller {
    // Declare Cadence Arch's address as a const
    address constant public cadenceArch = 0x0000000000000000000000010000000000000001;
    
    // Function to get a pseudo-random value
    function revertibleRandom() public view returns (uint64) {
        (bool ok, bytes memory data) = cadenceArch.staticcall(abi.encodeWithSignature("revertibleRandom()"));
        require(ok, "failed to fetch a random number through cadence arch");
        uint64 output = abi.decode(data, (uint64));
        // Return random value
        return output;
    }
}
```