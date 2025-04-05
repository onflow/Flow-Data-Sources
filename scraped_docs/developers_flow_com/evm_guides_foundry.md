# Source: https://developers.flow.com/evm/guides/foundry

Using Foundry with Flow | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Network Information](/evm/networks)
* [EVM Quickstart](/evm/quickstart)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)

  + [Integrating Metamask](/evm/guides/integrating-metamask)
  + [Hardhat](/evm/guides/hardhat)
  + [Remix](/evm/guides/remix)
  + [Rainbowkit](/evm/guides/rainbowkit)
  + [Viem & Wagmi](/evm/guides/wagmi)
  + [Foundry](/evm/guides/foundry)
  + [VRF (Randomness) in Solidity](/evm/guides/vrf)
  + [Ethers](/evm/guides/ethers)
  + [Web3.js](/evm/guides/web3-js)

* Guides
* Foundry

On this page

# Using Foundry with Flow

Foundry is a suite of development tools that simplifies the process of developing and deploying Solidity contracts to EVM networks. This guide will walk you through the process of deploying a Solidity contract to Flow EVM using the Foundry development toolchain. You can check out the official Foundry docs [here](https://book.getfoundry.sh/).

In this guide, we'll deploy an ERC-20 token contract to Flow EVM using Foundry. We'll cover:

* Developing and testing a basic ERC-20 contract
* Deploying the contract to Flow EVM using Foundry tools
* Querying Testnet state
* Mutating Testnet state by sending transactions

## Overview[​](#overview "Direct link to Overview")

To use Flow across all Foundry tools you need to:

1. Provide the Flow EVM RPC URL to the command you are using:

   `_10

   --rpc-url https://testnet.evm.nodes.onflow.org`
2. Use the `--legacy` flag to disable [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) style transactions. Flow will support EIP-1559 soon and this flag won't be needed.

As an example, we'll show you how to deploy a fungible token contract to Flow EVM using Foundry. You will see how the above flags are used in practice.

## Example: Deploying an ERC-20 Token Contract to Flow EVM[​](#example-deploying-an-erc-20-token-contract-to-flow-evm "Direct link to Example: Deploying an ERC-20 Token Contract to Flow EVM")

ERC-20 tokens are the most common type of tokens on Ethereum. We'll use [OpenZeppelin](https://www.openzeppelin.com/) starter templates with Foundry on Flow Testnet to deploy our own token called `MyToken`.

### Installation[​](#installation "Direct link to Installation")

The best way to install Foundry, is to use the `foundryup` CLI tool. You can get it using the following command:

`_10

curl -L https://foundry.paradigm.xyz | bash`

Install the tools:

`_10

foundryup`

This will install the Foundry tool suite: `forge`, `cast`, `anvil`, and `chisel`.

You may need to reload your shell after `foundryup` installation.

Check out the official [Installation](https://book.getfoundry.sh/getting-started/installation) guide for more information about different platforms or installing specific versions.

### Wallet Setup[​](#wallet-setup "Direct link to Wallet Setup")

We first need to generate a key pair for our EVM account. We can do this using the `cast` tool:

`_10

cast wallet new`

`cast` will print the private key and address of the new account. We can then paste the account address into the [Faucet](https://faucet.flow.com/fund-account) to fund it with some Testnet FLOW tokens.

You can verify the balance of the account after funding. Replace `$YOUR_ADDRESS` with the address of the account you funded:

`_10

cast balance --ether --rpc-url https://testnet.evm.nodes.onflow.org $YOUR_ADDRESS`

### Project Setup[​](#project-setup "Direct link to Project Setup")

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

### Writing the ERC-20 Token Contract[​](#writing-the-erc-20-token-contract "Direct link to Writing the ERC-20 Token Contract")

We'll use the OpenZeppelin ERC-20 contract template. We can start by adding OpenZeppelin to our project:

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

Before compiling, we also need to update the test file.

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

You can now make sure everything is okay by compiling the contracts:

`_10

forge compile`

Run the tests:

`_10

forge test`

They should all succeed.

### Deploying to Flow Testnet[​](#deploying-to-flow-testnet "Direct link to Deploying to Flow Testnet")

We can now deploy `MyToken` using the `forge create` command. We need to provide the RPC URL, private key from a funded account using the faucet, and constructor arguments that is the initial mint amount in this case. We need to use the `--legacy` flag to disable EIP-1559 style transactions. Replace `$DEPLOYER_PRIVATE_KEY` with the private key of the account you created earlier:

`_10

forge create --rpc-url https://testnet.evm.nodes.onflow.org \

_10

--private-key $DEPLOYER_PRIVATE_KEY \

_10

--constructor-args 42000000 \

_10

--legacy \

_10

src/MyToken.sol:MyToken`

The above will print the deployed contract address. We'll use it in the next section to interact with the contract.

### Verifying a Smart Contract[​](#verifying-a-smart-contract "Direct link to Verifying a Smart Contract")

Once deployed, you can verify the contract so that others can see the source code and interact with it from Flow's block explorer. You can use the [`forge verify-contract`](https://book.getfoundry.sh/reference/forge/forge-verify-contract) command:

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

When verifying a Mainnet contract, be sure to use the Mainnet [RPC](/evm/networks) and block explorer URLs.

### Querying Testnet State[​](#querying-testnet-state "Direct link to Querying Testnet State")

Based on the given constructor arguments, the deployer should own `42,000,000 MyT`. We can check the `MyToken` balance of the contract owner. Replace `$DEPLOYED_MYTOKEN_ADDRESS` with the address of the deployed contract and `$DEPLOYER_ADDRESS` with the address of the account you funded earlier:

`_10

cast balance \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--erc20 $DEPLOYED_MYTOKEN_ADDRESS \

_10

$DEPLOYER_ADDRESS`

This should return the amount specified during deployment. We can also call the associated function directly in the contract:

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

### Sending Transactions[​](#sending-transactions "Direct link to Sending Transactions")

Let's create a second account and move some tokens using a transaction. You can use `cast wallet new` to create a new test account. You don't need to fund it to receive tokens. Replace `$NEW_ADDRESS` with the address of the new account:

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

The deployer should also own less tokens now:

`_10

cast balance \

_10

--rpc-url https://testnet.evm.nodes.onflow.org \

_10

--erc20 $DEPLOYED_MYTOKEN_ADDRESS \

_10

$DEPLOYER_ADDRESS`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/guides/foundry.md)

Last updated on **Mar 31, 2025** by **Josh Hannan**

[Previous

Viem & Wagmi](/evm/guides/wagmi)[Next

VRF (Randomness) in Solidity](/evm/guides/vrf)

###### Rate this page

😞😐😊

* [Overview](#overview)
* [Example: Deploying an ERC-20 Token Contract to Flow EVM](#example-deploying-an-erc-20-token-contract-to-flow-evm)
  + [Installation](#installation)
  + [Wallet Setup](#wallet-setup)
  + [Project Setup](#project-setup)
  + [Writing the ERC-20 Token Contract](#writing-the-erc-20-token-contract)
  + [Testing](#testing)
  + [Deploying to Flow Testnet](#deploying-to-flow-testnet)
  + [Verifying a Smart Contract](#verifying-a-smart-contract)
  + [Querying Testnet State](#querying-testnet-state)
  + [Sending Transactions](#sending-transactions)

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
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.