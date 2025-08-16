# Source: https://developers.flow.com/evm/guides/vrf

VRF (Randomness) in Solidity | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [Flow Actions](/tutorials/defi)
* [Flow Blockchain 101](/tutorials/flow-101)
* [Use AI To Build On Flow](/tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/tutorials/gasless-transactions)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [Native VRF](/tutorials/native-vrf)

  + [Secure Randomness with Commit-Reveal in Cadence](/tutorials/native-vrf/commit-reveal-cadence)
  + [Deploy a Solidity Contract Using Cadence](/tutorials/native-vrf/deploy-solidity-contract)
  + [VRF (Randomness) in Solidity](/tutorials/native-vrf/vrf-in-solidity)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Integrations](/tutorials/integrations/crossmint)

* [Native VRF](/tutorials/native-vrf)
* VRF (Randomness) in Solidity

On this page

# VRF (Randomness) in Solidity

## **Introduction**[​](#introduction "Direct link to introduction")

Flow provides secure, native on-chain randomness that developers can leverage through Cadence Arch, a precompiled contract available on the Flow EVM environment. This guide will walk through how Solidity developers can use Cadence Arch to access Flow's verifiable randomness using Solidity.

### **What is Cadence Arch?**[​](#what-is-cadence-arch "Direct link to what-is-cadence-arch")

[Cadence Arch](https://github.com/onflow/flips/blob/main/protocol/20231116-evm-support.md#cadence-arch) is a precompiled smart contract that allows Solidity developers on Flow EVM to interact with Flow's randomness and other network features like block height. This contract can be accessed using its specific address, and Solidity developers can make static calls to retrieve random values and other information.

---

## **Prerequisites**[​](#prerequisites "Direct link to prerequisites")

* Basic Solidity knowledge.
* Installed Metamask extension.
* Remix IDE for compilation and deployment.
* Flow EVM Testnet setup in Metamask.

## **Network Information for Flow EVM**[​](#network-information-for-flow-evm "Direct link to network-information-for-flow-evm")

| **Parameter** | **Value** |
| --- | --- |
| **Network Name** | Flow EVM Testnet |
| **RPC Endpoint** | [Flow EVM Testnet RPC](https://testnet.evm.nodes.onflow.org/) |
| **Chain ID** | 545 |
| **Currency Symbol** | FLOW |
| **Block Explorer** | [Flow EVM Testnet Explorer](https://evm-testnet.flowscan.io/) |

## **Steps to Connect Flow EVM Testnet to Metamask**[​](#steps-to-connect-flow-evm-testnet-to-metamask "Direct link to steps-to-connect-flow-evm-testnet-to-metamask")

1. Open Metamask and click **Networks** -> **Add Network**.
2. Enter the following details:
   * **Network Name**: Flow EVM Testnet
   * **RPC URL**: `https://testnet.evm.nodes.onflow.org`
   * **Chain ID**: `545`
   * **Currency Symbol**: `FLOW`
   * **Block Explorer**: `https://evm-testnet.flowscan.io`
3. Click **Save** and switch to the Flow EVM Testnet.

![MetaMask Network Configuration](/assets/images/vrf-1-8cd4faeceebc20f715b261df0ef9b073.png)

## **Obtaining Testnet FLOW**[​](#obtaining-testnet-flow "Direct link to obtaining-testnet-flow")

You can fund your account with testnet FLOW using the [Flow Faucet](https://testnet-faucet.onflow.org/fund-account).  
Enter your Flow-EVM testnet address, and you'll receive testnet FLOW tokens to interact with smart contracts.

---

## **Solidity Code Example: Retrieving Random Numbers**[​](#solidity-code-example-retrieving-random-numbers "Direct link to solidity-code-example-retrieving-random-numbers")

Below is a simple Solidity contract that interacts with the Cadence Arch contract to retrieve a pseudo-random number.

`_17

// SPDX-License-Identifier: GPL-3.0

_17

pragma solidity >=0.7.0 <0.9.0;

_17

_17

contract CadenceArchCaller {

_17

// Address of the Cadence Arch contract

_17

address constant public cadenceArch = 0x0000000000000000000000010000000000000001;

_17

_17

// Function to fetch a pseudo-random value

_17

function revertibleRandom() public view returns (uint64) {

_17

// Static call to the Cadence Arch contract's revertibleRandom function

_17

(bool ok, bytes memory data) = cadenceArch.staticcall(abi.encodeWithSignature("revertibleRandom()"));

_17

require(ok, "Failed to fetch a random number through Cadence Arch");

_17

uint64 output = abi.decode(data, (uint64));

_17

// Return the random value

_17

return output;

_17

}

_17

}`

### **Explanation of the Contract**[​](#explanation-of-the-contract "Direct link to explanation-of-the-contract")

1. **Cadence Arch Address**:

   The `cadenceArch` variable stores the address of the Cadence Arch precompiled contract
   (`0x0000000000000000000000010000000000000001`), which is constant across Flow EVM.
2. **Revertible Random**:

   The `revertibleRandom()` function makes a static call to the `revertibleRandom<uint64>()` function to fetch a pseudo-random
   number. If the call is successful, it decodes the result as a `uint64` random value.

---

## **Deploying and Testing the Contract**[​](#deploying-and-testing-the-contract "Direct link to deploying-and-testing-the-contract")

### Compile and Deploy the Contract[​](#compile-and-deploy-the-contract "Direct link to Compile and Deploy the Contract")

1. Open Remix IDE.
2. Create a new file and paste the Solidity code above.

![Creating file in Remix](/assets/images/vrf-2-26a148ae96be310f27241d862652992f.png)

3. Compile the contract by selecting the appropriate Solidity compiler version (0.8.x).

![Compiling in Remix](/assets/images/vrf-3-694be8b1a09f9a3f960db18b17dc713e.png)

4. Connect Remix to your Metamask wallet (with Flow EVM testnet) by selecting **Injected Web3** as the environment.

![Connecting to MetaMask](/assets/images/vrf-4-e1a05dd1ccfec9650f563a28c44a2c60.png)

5. Deploy the contract.

![Deploying the contract](/assets/images/vrf-5-4c374061a3505fccd653efe6d58b22e3.png)

### Call revertibleRandom[​](#call-revertiblerandom "Direct link to Call revertibleRandom")

After deployment, you can interact with the contract to retrieve a random number.

Call the `revertibleRandom()` function in the left sidebar on the deployed contract. This will fetch a pseudo-random number generated by Flow's VRF.

![Calling revertibleRandom function](/assets/images/vrf-6-a4257b376af1a8c564848cae10ba5122.png)

The result will be a `uint64` random number generated on Flow EVM.

---

## **Generating Random Numbers in a Range**[​](#generating-random-numbers-in-a-range "Direct link to generating-random-numbers-in-a-range")

For use-cases like games and lotteries, it's useful to generate a random number within a specified range, the following example shows how to get a value between a min and max number.

`_17

// SPDX-License-Identifier: GPL-3.0

_17

pragma solidity >=0.7.0 <0.9.0;

_17

_17

contract RandomInRange {

_17

address constant public cadenceArch = 0x0000000000000000000000010000000000000001;

_17

_17

// Generate a random number between min and max

_17

function getRandomInRange(uint64 min, uint64 max) public view returns (uint64) {

_17

// Static call to the Cadence Arch contract's revertibleRandom function

_17

(bool ok, bytes memory data) = cadenceArch.staticcall(abi.encodeWithSignature("revertibleRandom()"));

_17

require(ok, "Failed to fetch a random number through Cadence Arch");

_17

uint64 randomNumber = abi.decode(data, (uint64));

_17

_17

// Return the number in the specified range

_17

return (randomNumber % (max + 1 - min)) + min;

_17

}

_17

}`

warning

The above code is susceptible to the [modulo bias](https://research.kudelskisecurity.com/2020/07/28/the-definitive-guide-to-modulo-bias-and-how-to-avoid-it/), particularly if the random number range is not a multiple of your desired range. To avoid this, you can use a more complex algorithm like rejection sampling, an example for which is provided in [this repository](https://github.com/onflow/random-coin-toss).

## **Secure Randomness with Commit-Reveal Scheme in Solidity**[​](#secure-randomness-with-commit-reveal-scheme-in-solidity "Direct link to secure-randomness-with-commit-reveal-scheme-in-solidity")

The **`revertibleRandom()`** function can be directly used to generate a pseudo-random number. However, in certain situations, especially involving untrusted callers, this function exposes a vulnerability: the ability of a transaction to **revert after seeing the random result**.

**The Issue with Using `revertibleRandom()` Directly:**

* When an untrusted party calls a contract function that uses `revertibleRandom()`, they receive the random number **during the transaction execution**.
* **Post-selection** is the ability of the caller to abort the transaction if the random outcome is unfavorable. In this case, the user could choose to revert the transaction (for example, if they lose a bet) and attempt to call the function again in hopes of a better outcome.
* This can lead to a form of **transaction reversion attack**, where the randomness can be exploited by repeatedly attempting transactions until a favorable result is obtained.

## Read More[​](#read-more "Direct link to Read More")

For further details on Flow's randomness and secure development practices, check out the [Flow Randomness Documentation](https://developers.flow.com/build/advanced-concepts/randomness).

You can also view an example in both Solidity and Cadence of a [random coin toss implentation](https://github.com/onflow/random-coin-toss) using the VRF.

*This documentation was contributed by [Noah Naizir](https://x.com/noah_overflow) a community developer.*

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/native-vrf/vrf-in-solidity.md)

Last updated on **Jun 9, 2025** by **Ali Serag**

[Previous

Deploy a Solidity Contract Using Cadence](/tutorials/native-vrf/deploy-solidity-contract)[Next

FlowtoBooth](/tutorials/flowtobooth)

###### Rate this page

😞😐😊

Copy as Markdown

* [**Introduction**](#introduction)
  + [**What is Cadence Arch?**](#what-is-cadence-arch)
* [**Prerequisites**](#prerequisites)
* [**Network Information for Flow EVM**](#network-information-for-flow-evm)
* [**Steps to Connect Flow EVM Testnet to Metamask**](#steps-to-connect-flow-evm-testnet-to-metamask)
* [**Obtaining Testnet FLOW**](#obtaining-testnet-flow)
* [**Solidity Code Example: Retrieving Random Numbers**](#solidity-code-example-retrieving-random-numbers)
  + [**Explanation of the Contract**](#explanation-of-the-contract)
* [**Deploying and Testing the Contract**](#deploying-and-testing-the-contract)
  + [Compile and Deploy the Contract](#compile-and-deploy-the-contract)
  + [Call revertibleRandom](#call-revertiblerandom)
* [**Generating Random Numbers in a Range**](#generating-random-numbers-in-a-range)
* [**Secure Randomness with Commit-Reveal Scheme in Solidity**](#secure-randomness-with-commit-reveal-scheme-in-solidity)
* [Read More](#read-more)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.