# Source: https://developers.flow.com/blockchain-development-tutorials/evm/development-tools/foundry

Using Foundry with Flow | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            + [Flow EVM Setup](/blockchain-development-tutorials/evm/setup)

              + [Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)

                + [Flow EVM Development Tools](/blockchain-development-tutorials/evm/development-tools)

                  - [Hardhat](/blockchain-development-tutorials/evm/development-tools/hardhat)- [Remix](/blockchain-development-tutorials/evm/development-tools/remix)- [Foundry](/blockchain-development-tutorials/evm/development-tools/foundry)+ [Build a Fully-Onchain Image Gallery](/blockchain-development-tutorials/evm/image-gallery)* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Flow EVM Guides](/blockchain-development-tutorials/evm)* [Flow EVM Development Tools](/blockchain-development-tutorials/evm/development-tools)* Foundry

On this page

# Using Foundry with Flow

Foundry is a suite of development tools that simplifies the process to develop and deploy Solidity contracts to EVM networks. This guide will walk you through how to deploy a Solidity contract to Flow EVM with the Foundry development toolchain. You can check out the official [Foundry docs].

In this guide, we'll deploy an ERC-20 token contract to Flow EVM using Foundry. We'll cover:

* How to develop and test a basic ERC-20 contract
* Deploy the contract to Flow EVM with Foundry tools
* How to query the Testnet state
* How to mutate Testnet state by sending transactions

## Overview[​](#overview "Direct link to Overview")

To use Flow across all Foundry tools you need to:

1. Provide the Flow EVM RPC URL to the command you are using:

   `_10

   --rpc-url https://testnet.evm.nodes.onflow.org`
2. Use the `--legacy` flag to turn off [EIP-1559] style transactions. Flow will support EIP-1559 soon and this flag won't be needed.

As an example, we'll show you how to deploy a fungible token contract to Flow EVM with Foundry. You will see how the above flags are used in practice.

## Example: Deploy an ERC-20 Token Contract to Flow EVM[​](#example-deploy-an-erc-20-token-contract-to-flow-evm "Direct link to Example: Deploy an ERC-20 Token Contract to Flow EVM")

ERC-20 tokens are the most common type of tokens on Ethereum. We'll use [OpenZeppelin] starter templates with Foundry on Flow Testnet to deploy our own token called `MyToken`.

### Installation[​](#installation "Direct link to Installation")

The best way to install Foundry, is to use the `foundryup` CLI tool. You can get it with the following command:

`_10

curl -L https://foundry.paradigm.xyz | bash`

Install the tools:

`_10

foundryup`

This will install the Foundry tool suite: `forge`, `cast`, `anvil`, and `chisel`.

You may need to reload your shell after `foundryup` installation.

Check out the official [Installation Guide] for more information about different platforms or how to install specific versions.

### Wallet setup[​](#wallet-setup "Direct link to Wallet setup")

We first need to generate a key pair for our EVM account. We can do this with the `cast` tool:

`_10

cast wallet new`

`cast` will print the private key and address of the new account. We can then paste the account address into the [Faucet] to fund it with some Testnet FLOW tokens.

You can verify the balance of the account after funding. Replace `$YOUR_ADDRESS` with the address of the account you funded:

`_10

cast balance --ether --rpc-url https://testnet.evm.nodes.onflow.org $YOUR_ADDRESS`

### Project setup[​](#project-setup "Direct link to Project setup")

First, create a new directory for your project:

`_10

mkdir mytoken

_10

cd mytoken`

We can use `init` to initialize a new project:

`_10

forge init`

This will create a contract called `Counter` in the `contracts` directory with associated tests and deployment scripts. We can replace this with our own ERC-20 contract. To verify the initial setup, you can run the tests for `Counter`:

`_10

forge test`

The tests should pass.

### Write the ERC-20 token contract[​](#write-the-erc-20-token-contract "Direct link to Write the ERC-20 token contract")

We'll use the OpenZeppelin ERC-20 contract template. To start, we'll add OpenZeppelin to our project:

`_10

forge install OpenZeppelin/openzeppelin-contracts`

Rename `src/Counter.sol` to `src/MyToken.sol` and replace the contents with the following:

`_10

pragma solidity ^0.8.20;

_10

_10

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

_10

_10

contract MyToken is ERC20 {

_10

constructor(uint256 initialMint_) ERC20("MyToken", "MyT") {

_10

_mint(msg.sender, initialMint_);

_10

}

_10

}`

The above is a basic ERC-20 token with the name `MyToken` and symbol `MyT`. It also mints the specified amount of tokens to the contract deployer. The amount is passed as a constructor argument during deployment.

Before we comnpile, we also need to update the test file.

### Testing[​](#testing "Direct link to Testing")

Rename `test/Counter.t.sol` to `test/MyToken.t.sol` and replace the contents with the following:

`_65

pragma solidity ^0.8.20;

_65

_65

import {Test, console2, stdError} from "forge-std/Test.sol";

_65

import {MyToken} from "../src/MyToken.sol";

_65

_65

contract MyTokenTest is Test {

_65

uint256 initialSupply = 420000;

_65

_65

MyToken public token;

_65

address ownerAddress = makeAddr("owner");

_65

address randomUserAddress = makeAddr("user");

_65

_65

function setUp() public {

_65

vm.prank(ownerAddress);

_65

token = new MyToken(initialSupply);

_65

}

_65

_65

/*

_65

Test general ERC-20 token properties

_65

*/

_65

function test_tokenProps() public view {

_65

assertEq(token.name(), "MyToken");

_65

assertEq(token.symbol(), "MyT");

_65

assertEq(token.decimals(), 18);

_65

assertEq(token.totalSupply(), initialSupply);

_65

assertEq(token.balanceOf(address(0)), 0);

_65

assertEq(token.balanceOf(ownerAddress), initialSupply);

_65

}

_65

_65

/*

_65

Test Revert transfer to sender with insufficient balance

_65

*/

_65

function test_transferRevertInsufficientBalance() public {

_65

vm.prank(randomUserAddress);

_65

vm.expectRevert(abi.encodeWithSignature("ERC20InsufficientBalance(address,uint256,uint256)", randomUserAddress, 0, 42));

_65

token.transfer(ownerAddress, 42);

_65

}

_65

_65

/*

_65

Test transfer

_65

*/

_65

function test_transfer() public {

_65

vm.prank(ownerAddress);

_65

assertEq(token.transfer(randomUserAddress, 42), true);

_65

assertEq(token.balanceOf(randomUserAddress), 42);

_65

assertEq(token.balanceOf(ownerAddress), initialSupply - 42);

_65

}

_65

_65

/*

_65

Test transferFrom with approval

_65

*/

_65

function test_transferFrom() public {

_65

vm.prank(ownerAddress);

_65

token.approve(randomUserAddress, 69);

_65

_65

uint256 initialRandomUserBalance = token.balanceOf(randomUserAddress);

_65

uint256 initialOwnerBalance = token.balanceOf(ownerAddress);

_65

_65

vm.prank(randomUserAddress);

_65

assertEq(token.transferFrom(ownerAddress, randomUserAddress, 42), true);

_65

assertEq(token.balanceOf(randomUserAddress), initialRandomUserBalance + 42);

_65

assertEq(token.balanceOf(ownerAddress), initialOwnerBalance - 42);

_65

assertEq(token.allowance(ownerAddress, randomUserAddress), 69 - 42);

_65

}

_65

}`

To make sure everything is okay, compile the contracts:

`_10

forge compile`

Run the tests:

`_10

forge test`

They should all succeed.

### Deploy to Flow Testnet[​](#deploy-to-flow-testnet "Direct link to Deploy to Flow Testnet")

We can now deploy `MyToken` with the `forge create` command. We need to provide the RPC URL, private key from a funded account with the faucet, and constructor arguments that is the initial mint amount in this case. We need to use the `--legacy` flag to turn off EIP-1559 style transactions. Replace `$DEPLOYER_PRIVATE_KEY` with the private key of the account you created earlier:

`_10

forge create --broadcast src/MyToken.sol:MyToken \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--private-key $DEPLOYER_PRIVATE_KEY \

_10

--constructor-args 42000000 \

_10

--legacy`

The above will print the deployed contract address. We'll use it in the next section to interact with the contract.

### Verify a smart contract[​](#verify-a-smart-contract "Direct link to Verify a smart contract")

After you deploy the contract, you can verify it so that others can see the source code and interact with it from Flow's block explorer. You can use the [`forge verify-contract`] command:

`_10

forge verify-contract --rpc-url https://testnet.evm.nodes.onflow.org/ \

_10

--verifier blockscout \

_10

--verifier-url https://evm-testnet.flowscan.io/api \

_10

$DEPLOYED_MYTOKEN_ADDRESS \

_10

src/MyToken.sol:MyToken`

info

When you verify a Mainnet contract, be sure to use the Mainnet [RPC] and block explorer URLs.

### Query Testnet state[​](#query-testnet-state "Direct link to Query Testnet state")

Based on the given constructor arguments, the deployer should own `42,000,000 MyT`. We can check the `MyToken` balance of the contract owner. Replace `$DEPLOYED_MYTOKEN_ADDRESS` with the address of the deployed contract and `$DEPLOYER_ADDRESS` with the address of the account you funded earlier:

`_10

cast balance \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--erc20 $DEPLOYED_MYTOKEN_ADDRESS \

_10

$DEPLOYER_ADDRESS`

This will return the amount specified during deployment. We can also call the associated function directly in the contract:

`_10

cast call $DEPLOYED_MYTOKEN_ADDRESS \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

"balanceOf(address)(uint256)" \

_10

$DEPLOYER_ADDRESS`

We can query other data like the token symbol:

`_10

cast call $DEPLOYED_MYTOKEN_ADDRESS \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

"symbol()(string)"`

### Send Transactions[​](#send-transactions "Direct link to Send Transactions")

Let's create a second account and move some tokens with a transaction. You can use `cast wallet new` to create a new test account. You don't need to fund it to receive tokens. Replace `$NEW_ADDRESS` with the address of the new account:

`_10

cast send $DEPLOYED_MYTOKEN_ADDRESS \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--private-key $DEPLOYER_PRIVATE_KEY \

_10

--legacy \

_10

"transfer(address,uint256)(bool)" \

_10

$NEW_ADDRESS 42`

We can check the balance of the new account:

`_10

cast balance \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--erc20 $DEPLOYED_MYTOKEN_ADDRESS \

_10

$NEW_ADDRESS`

The deployer will also own fewer tokens now:

`_10

cast balance \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--erc20 $DEPLOYED_MYTOKEN_ADDRESS \

_10

$DEPLOYER_ADDRESS`

[Foundry docs]: <https://book.getfoundry.sh/>)
[EIP-1559]: <https://eips.ethereum.org/EIPS/eip-1559>
[OpenZeppelin]: <https://www.openzeppelin.com/>
[Installation Guide]: <https://book.getfoundry.sh/getting-started/installation>
[Faucet]: <https://faucet.flow.com/fund-account>
[`forge verify-contract`]: <https://book.getfoundry.sh/reference/forge/forge-verify-contract>
[RPC]: ../../../build/evm/networks.md

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/evm/development-tools/foundry.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Remix](/blockchain-development-tutorials/evm/development-tools/remix)[Next

Build a Fully-Onchain Image Gallery](/blockchain-development-tutorials/evm/image-gallery)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Example: Deploy an ERC-20 Token Contract to Flow EVM](#example-deploy-an-erc-20-token-contract-to-flow-evm)
    + [Installation](#installation)+ [Wallet setup](#wallet-setup)+ [Project setup](#project-setup)+ [Write the ERC-20 token contract](#write-the-erc-20-token-contract)+ [Testing](#testing)+ [Deploy to Flow Testnet](#deploy-to-flow-testnet)+ [Verify a smart contract](#verify-a-smart-contract)+ [Query Testnet state](#query-testnet-state)+ [Send Transactions](#send-transactions)

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