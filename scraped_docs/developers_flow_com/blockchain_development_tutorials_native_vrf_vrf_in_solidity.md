# Source: https://developers.flow.com/blockchain-development-tutorials/native-vrf/vrf-in-solidity

VRF (Randomness) in Solidity | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                + [Secure Randomness with Commit-Reveal in Cadence](/blockchain-development-tutorials/native-vrf/commit-reveal-cadence)+ [VRF (Randomness) in Solidity](/blockchain-development-tutorials/native-vrf/vrf-in-solidity)* [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)* VRF (Randomness) in Solidity

On this page

# VRF (Randomness) in Solidity

Flow provides secure, native onchain randomness that developers can leverage through Cadence Arch, a precompiled contract available on the Flow EVM environment. This guide walks you through how Consumer Decentralized Finance (DeFi) developers can use Cadence Arch to access Flow's verifiable randomness with Consumer DeFi.

### What is Cadence Arch?[​](#what-is-cadence-arch "Direct link to What is Cadence Arch?")

[Cadence Arch](https://github.com/onflow/flips/blob/main/protocol/20231116-evm-support.md#cadence-arch) is a precompiled smart contract that allows DeFi developers on Flow EVM to interact with Flow's randomness and other network features like block height. This contract can be accessed with its specific address, and DeFi developers can make static calls to retrieve random values and other information.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Basic DeFi knowledge
* Installed Metamask extension
* Remix IDE for compilation and deployment
* Flow EVM Testnet setup in Metamask

## Network information for Flow EVM[​](#network-information-for-flow-evm "Direct link to Network information for Flow EVM")

See [Network information](/build/evm/quickstart#network-information) for more details.

## Steps to connect Flow EVM testnet to metamask[​](#steps-to-connect-flow-evm-testnet-to-metamask "Direct link to Steps to connect Flow EVM testnet to metamask")

See [Wallets & Configurations](/blockchain-development-tutorials/evm/setup/integrating-metamask) for more details.

## Solidity commit reveal[​](#solidity-commit-reveal "Direct link to Solidity commit reveal")

Make sure you review the Solidity version of the [commit reveal](https://github.com/onflow/random-coin-toss/blob/main/solidity/src/CoinToss.sol) to learn more about Flow EVM's native secure randomness through a simple demonstration.

## Obtaining testnet FLOW[​](#obtaining-testnet-flow "Direct link to Obtaining testnet FLOW")

You can fund your account with testnet FLOW with the [Flow Faucet](https://testnet-faucet.onflow.org/fund-account).

Enter your Flow-EVM testnet address, and you'll receive testnet FLOW tokens to interact with smart contracts.

## Solidity code example: retrieving random numbers[​](#solidity-code-example-retrieving-random-numbers "Direct link to Solidity code example: retrieving random numbers")

The following is a simple Solidity contract that interacts with the Cadence Arch contract to retrieve a pseudo-random number:

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

### Explanation of the contract[​](#explanation-of-the-contract "Direct link to Explanation of the contract")

1. **Cadence Arch Address**:

   The `cadenceArch` variable stores the address of the Cadence Arch precompiled contract (`0x0000000000000000000000010000000000000001`), which is constant across Flow EVM.
2. **Revertible Random**:

   The `revertibleRandom()` function makes a static call to the `revertibleRandom<uint64>()` function to fetch a pseudo-random number. If the call is successful, it decodes the result as a `uint64` random value.

## Deploy and test the contract[​](#deploy-and-test-the-contract "Direct link to Deploy and test the contract")

### Compile and deploy the contract[​](#compile-and-deploy-the-contract "Direct link to Compile and deploy the contract")

1. Open Remix IDE.
2. Create a new file and paste the Solidity code above.

   ![Creating file in Remix](/assets/images/vrf-2-26a148ae96be310f27241d862652992f.png)
3. To compile the contract, select the appropriate Consumer DeFi compiler version (0.8.x).

   ![Compiling in Remix](/assets/images/vrf-3-694be8b1a09f9a3f960db18b17dc713e.png)
4. Connect Remix to your Metamask wallet (with Flow EVM testnet). To do this, select **Injected Web3** as the environment.

   ![Connecting to MetaMask](/assets/images/vrf-4-e1a05dd1ccfec9650f563a28c44a2c60.png)
5. Deploy the contract.

   ![Deploying the contract](/assets/images/vrf-5-4c374061a3505fccd653efe6d58b22e3.png)

### Call revertibleRandom[​](#call-revertiblerandom "Direct link to Call revertibleRandom")

After deployment, you can interact with the contract to retrieve a random number.

Call the `revertibleRandom()` function in the left sidebar on the deployed contract. This fetches a pseudo-random number that Flow's VRF generates.

![Calling revertibleRandom function](/assets/images/vrf-6-a4257b376af1a8c564848cae10ba5122.png)

The result will be a `uint64` random number generated on Flow EVM.

## Generate random numbers in a range[​](#generate-random-numbers-in-a-range "Direct link to Generate random numbers in a range")

For use-cases like games and lotteries, it's useful to generate a random number within a specified range. The following example shows how to get a value between a min and max number.

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

## Secure randomness with commit-reveal scheme in Solidity[​](#secure-randomness-with-commit-reveal-scheme-in-solidity "Direct link to Secure randomness with commit-reveal scheme in Solidity")

You can use the **`revertibleRandom()`** function directly to generate a pseudo-random number. However, in certain situations, especially with untrusted callers, this function exposes a vulnerability: the ability of a transaction to **revert after seeing the random result**.

**The Issue with Using `revertibleRandom()` Directly**

* When an untrusted party calls a contract function that uses `revertibleRandom()`, they receive the random number **during the transaction execution**.
* **Post-selection** is the caller's ability to abort the transaction if the random outcome is unfavorable. In this case, the user could choose to revert the transaction (for example, if they lose a bet) and attempt to call the function again in hopes of a better outcome.
* This can lead to a form of *transaction reversion attack*, where the randomness can be exploited by repeatedly attempting transactions until a favorable result is obtained.

## Further reading[​](#further-reading "Direct link to Further reading")

For further details on Flow's randomness and secure development practices, check out the [Flow Randomness Documentation](https://developers.flow.com/build/cadence/advanced-concepts/randomness).

You can also view an example in both Solidity and Cadence of a [random coin toss implentation](https://github.com/onflow/random-coin-toss) using the VRF.

*This documentation was contributed by [Noah Naizir](https://x.com/noah_overflow) a community developer.*

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/native-vrf/vrf-in-solidity.md)

Last updated on **Nov 11, 2025** by **cshannon1218**

[Previous

Secure Randomness with Commit-Reveal in Cadence](/blockchain-development-tutorials/native-vrf/commit-reveal-cadence)[Next

Token Development and Registration](/blockchain-development-tutorials/tokens)

###### Rate this page

😞😐😊

Copy as Markdown

* [What is Cadence Arch?](#what-is-cadence-arch)* [Prerequisites](#prerequisites)* [Network information for Flow EVM](#network-information-for-flow-evm)* [Steps to connect Flow EVM testnet to metamask](#steps-to-connect-flow-evm-testnet-to-metamask)* [Solidity commit reveal](#solidity-commit-reveal)* [Obtaining testnet FLOW](#obtaining-testnet-flow)* [Solidity code example: retrieving random numbers](#solidity-code-example-retrieving-random-numbers)
              + [Explanation of the contract](#explanation-of-the-contract)* [Deploy and test the contract](#deploy-and-test-the-contract)
                + [Compile and deploy the contract](#compile-and-deploy-the-contract)+ [Call revertibleRandom](#call-revertiblerandom)* [Generate random numbers in a range](#generate-random-numbers-in-a-range)* [Secure randomness with commit-reveal scheme in Solidity](#secure-randomness-with-commit-reveal-scheme-in-solidity)* [Further reading](#further-reading)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.