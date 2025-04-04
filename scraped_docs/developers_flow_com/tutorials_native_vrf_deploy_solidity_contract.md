# Source: https://developers.flow.com/tutorials/native-vrf/deploy-solidity-contract

Deploy a Solidity Contract Using Cadence | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [AI Plus Flow](/tutorials/ai-plus-flow)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

  + [Secure Randomness with Commit-Reveal in Cadence](/tutorials/native-vrf/commit-reveal-cadence)
  + [Deploy a Solidity Contract Using Cadence](/tutorials/native-vrf/deploy-solidity-contract)

* [Native VRF](/tutorials/native-vrf)
* Deploy a Solidity Contract Using Cadence

On this page

# Deploy a Solidity Contract using Cadence

## Why Solidity And Cadence?[​](#why-solidity-and-cadence "Direct link to Why Solidity And Cadence?")

Solidity powers Ethereum's vast ecosystem, with a deep library of contracts like ERC721s for NFTs and a huge developer base. Deploying Solidity contracts on Flow's EVM layer leverages Flow's consensus for lower fees, quicker transactions, and slick asset handling, while giving you access to additional tools, including native VRF.

Imagine gaming NFTs minted cheaper, DeFi logic ported without rewrites, or Ethereum projects tapping Flow's scalable, user-first design. Flow EVM runs Solidity natively, and Cadence bridges the gap—letting you reuse trusted contracts while unlocking Flow's edge.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Deploy a Solidity contract on Flow EVM using Cadence
* Call functions on this contract from the Cadence side

## Prerequisites:[​](#prerequisites "Direct link to Prerequisites:")

* NodeJs and NPM (must be installed - follow [this guide](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm))
* Go
* Flow Command Line Interface (Flow CLI) (must be installed - follow [this guide](https://developers.flow.com/tools/flow-cli/install))
* Remix (can be accessed online - available at [Remix](https://remix.ethereum.org/))
* Overflow (must be installed - install via Go with `go get github.com/bjartek/overflow/v2`)
* Cadence Owned Account (COA) (must be created - follow [this guide](https://developers.flow.com/evm/cadence/interacting-with-coa) to set up)

For this guide, we're using Remix for Solidity contract compilation and Overflow for running Cadence transactions on Flow EVM. To deploy a Solidity contract using Cadence, you'll need a Cadence Owned Account; the guide linked above explains how to create one.

## High-Level Walkthrough[​](#high-level-walkthrough "Direct link to High-Level Walkthrough")

At a high level, this guide walks you through deploying a Solidity contract on the Flow blockchain's EVM layer using Cadence in three main steps:

1. Compile the Solidity Contract: You'll start by taking a Solidity contract (like an ERC721 for NFTs) and compiling it into bytecode using Remix, an online Ethereum development tool. This bytecode is the machine-readable version of your contract, ready to be deployed.
2. Deploy to Flow EVM with Cadence: Next, you'll set up a local environment with tools like Overflow and the Flow CLI. Using a Cadence transaction, you'll deploy the bytecode to Flow's EVM layer via a Cadence Owned Account (COA), bridging the two ecosystems seamlessly.
3. Interact from Cadence: Finally, you'll use a Cadence script to call a function on your deployed Solidity contract—like minting an NFT—demonstrating how Cadence can interact with Ethereum-style logic on Flow.

This process leverages Ethereum's robust contract library and Flow's efficient, user-friendly blockchain, opening up a world of cross-platform possibilities—all in a few straightforward steps.

## Step 1: Compile the Solidity Contract[​](#step-1-compile-the-solidity-contract "Direct link to Step 1: Compile the Solidity Contract")

Start by compiling your Solidity contract to get its bytecode. For this example, use OpenZeppelin's ERC721 contract for tracking game items. Here's how to do it in Remix:

1. Open Remix: Go to [Remix](https://remix.ethereum.org/) in your browser.
2. Create a New File: In the Remix file explorer, click the "+" button and name the file (e.g., `GameItem.sol`).
3. Paste the Contract Code: Copy the OpenZeppelin ERC721 contract code (e.g., from [this example](https://developers.flow.com/evm/cadence/interacting-with-coa)) and paste it into the new file.
4. Compile the Contract:
   * Select the appropriate Solidity compiler version (e.g., 0.8.x) in the "Solidity Compiler" tab.
   * Click "Compile GameItem.sol".
5. Copy the Bytecode:
   * Go to the "Compilation Details" (or "Bytecode" section after compilation).
   * Copy the "object" field under the bytecode section.

![Remix Screenshot](/assets/images/remix1-9f34bbe8a66a9e37b23083cdf570e993.png)

6. Save the Bytecode:
   * From your project's root directory, create a folder named `bytecode`.
   * Inside it, create a file called `GameItem.js`.
   * Paste the bytecode into `GameItem.js` as a string (e.g., `module.exports = "0x..."`).

Here's the Cadence transaction we'll use later to deploy this bytecode on Flow EVM:

`_15

import "EVM"

_15

_15

transaction(code: String, pathId: Int) {

_15

let coa: auth(EVM.Deploy) &EVM.CadenceOwnedAccount

_15

_15

prepare(signer: auth(Storage) &Account) {

_15

let coaPath = StoragePath(identifier: signer.address.toString().concat("EVM_").concat(pathId.toString()))!

_15

self.coa = signer.storage.borrow<auth(EVM.Deploy) &EVM.CadenceOwnedAccount>(

_15

from: coaPath) ?? panic("Could not borrow reference to the COA!")

_15

}

_15

_15

execute {

_15

self.coa.deploy(code: code.decodeHex(), gasLimit: 15000000, value: EVM.Balance(attoflow: 0))

_15

}

_15

}`

## Step 2: Set Up Your Environment and Deploy the Contract[​](#step-2-set-up-your-environment-and-deploy-the-contract "Direct link to Step 2: Set Up Your Environment and Deploy the Contract")

To run the transactions and tests, we'll use [Overflow](https://github.com/bjartek/overflow%5D). Follow these steps to set up and deploy:

1. Initialize a Go Project:
   * Open your terminal and navigate to your project's root directory.
   * Run: `go mod init flow/tutorials` to create a Go module.
2. Install Overflow:
   * Run: `go get github.com/bjartek/overflow/v2` to install the Overflow package.
3. Create the Task File:
   * In the root directory, create a folder called `tasks`.
   * Inside `tasks`, create a file named `main.go`.
   * Paste the following Go code into `main.go`:

`_41

package main

_41

_41

import (

_41

"fmt"

_41

"io/ioutil"

_41

"log"

_41

. "github.com/bjartek/overflow/v2"

_41

"github.com/fatih/color"

_41

)

_41

_41

func readJSFile(filePath string) (string, error) {

_41

content, err := ioutil.ReadFile(filePath)

_41

if err != nil {

_41

return "", err

_41

}

_41

return string(content), nil

_41

}

_41

_41

func main() {

_41

filePath := "bytecode/GameItem.js"

_41

jsContent, err := readJSFile(filePath)

_41

if err != nil {

_41

log.Fatalf("Error reading JavaScript file: %v", err)

_41

}

_41

o := Overflow(

_41

WithGlobalPrintOptions(),

_41

WithNetwork("testnet"),

_41

)

_41

_41

color.Red("Should be able to create a COA")

_41

o.Tx("create_COA",

_41

WithSigner("gamer"),

_41

).Print()

_41

_41

color.Cyan("Deploy a Solidity contract to Random's COA")

_41

o.Tx("deploy_sol_contract",

_41

WithSigner("gamer"),

_41

WithArg("code", jsContent),

_41

WithArg("pathId", 0),

_41

).Print()

_41

}`

4. Run the Deployment:
   * From the terminal, navigate to the root directory.
   * Run: `go run ./tasks/main.go`.
   * This will:
     + Create a Cadence Owned Account (COA) for the "gamer" account.
     + Deploy the Solidity contract using the bytecode from `GameItem.js`.
5. Verify the Deployment:
   * Check the terminal output for the deployed contract address (e.g., `0xb93cB988D0722E17B67A5E169a47FB6F3A4dea1b`).
   * Visit the [Flow EVM Testnet Scanner](https://evm-testnet.flowscan.io/) and search for the address to confirm the deployment.

![Remix Screenshot](/assets/images/remix3-c4a3cc393ebec12a2635aa51c49922d0.png)

Note: The "gamer" account (e.g., `0xb995271139c0126f`) is a Testnet account. The `pathId` (set to `0`) corresponds to the COA slot. If you've created multiple COAs, increment `pathId` (e.g., `1`, `2`) accordingly.

## Step 3: Call a Function on the Deployed Contract[​](#step-3-call-a-function-on-the-deployed-contract "Direct link to Step 3: Call a Function on the Deployed Contract")

Now, let's call the `awardItem` function from the deployed ERC721 contract using this Cadence script:

1. Cadence Script Preparation:
   Use the following Cadence script to call the contract function:

`_23

import "EVM"

_23

_23

access(all)

_23

fun main(hexEncodedAddress: String, address: Address, pathId: UInt64): [AnyStruct] {

_23

let account = getAuthAccount<auth(Storage) &Account>(address)

_23

let coaPath = StoragePath(identifier: address.toString().concat("EVM_").concat(pathId.toString()))!

_23

let coa = account.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(

_23

from: coaPath

_23

) ?? panic("Could not borrow reference to the COA!")

_23

let addressBytes = hexEncodedAddress.decodeHex().toConstantSized<[UInt8; 20]>()!

_23

_23

let callResult = coa.call(

_23

to: EVM.EVMAddress(bytes: addressBytes),

_23

data: EVM.encodeABIWithSignature(

_23

"awardItem(address,string)",

_23

[EVM.addressFromString("000000000000000000000002A16A68E971e4670B"), "{name: gamerz}"]

_23

),

_23

gasLimit: 15000000,

_23

value: EVM.Balance(attoflow: 0)

_23

)

_23

_23

return EVM.decodeABI(types: [Type<UInt256>()], data: callResult.data)

_23

}`

2. Update the Go File:
   Open `tasks/main.go` and add the following code at the end of the `main` function (replace the `hexEncodedAddress` with your deployed contract address):

`_10

color.Cyan("Mint a game item from the Solidity contract")

_10

o.Script("call_sol_function",

_10

WithArg("hexEncodedAddress", "b93cB988D0722E17B67A5E169a47FB6F3A4dea1b"),

_10

WithArg("address", "gamer"),

_10

WithArg("pathId", 0),

_10

).Print()`

3. Run the Script:

   * In the terminal, run: `go run ./tasks/main.go` again.
   * This executes the Cadence script, calling `awardItem` to mint an NFT.
4. Check the Result:

   * The terminal will display the token ID of the newly minted NFT (e.g., a UInt256 value).
   * See the screenshot below for an example output:

![Result Screenshot](/assets/images/remix4-59dc99cddcc539c11ff438139b75f025.png)

The terminal output shows the unique token ID that was generated when minting the game item through the Solidity contract using Cadence.

info

The `awardItem` function is called with a test address and a string parameter. In a real-world scenario, you would replace these with actual wallet addresses and more meaningful metadata.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Deploying a Solidity contract within a Cadence environment on the Flow blockchain is not only feasible but also presents an exciting opportunity for you to harness the strengths of both programming languages. Throughout this guide, you've navigated the critical steps involved in the deployment process, from compiling your Solidity contract using Remix to executing transactions with Overflow and Cadence scripts. By completing this guide, you've achieved the following:

* Deployed a Solidity contract on Flow EVM using Cadence: You compiled and deployed your Solidity contract to Flow's EVM layer via a Cadence transaction.
* Called functions from Cadence: You used a Cadence script to mint an NFT by invoking the `awardItem` function on your deployed contract.

As blockchain technology continues to evolve, adopting these best practices is crucial for fostering a secure and trustworthy ecosystem. This empowers you to innovate while staying true to the core principles of decentralization and fairness.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/native-vrf/deploy-solidity-contract.md)

Last updated on **Mar 28, 2025** by **Jordan Ribbink**

[Previous

Secure Randomness with Commit-Reveal in Cadence](/tutorials/native-vrf/commit-reveal-cadence)

###### Rate this page

😞😐😊

* [Why Solidity And Cadence?](#why-solidity-and-cadence)
* [Objectives](#objectives)
* [Prerequisites:](#prerequisites)
* [High-Level Walkthrough](#high-level-walkthrough)
* [Step 1: Compile the Solidity Contract](#step-1-compile-the-solidity-contract)
* [Step 2: Set Up Your Environment and Deploy the Contract](#step-2-set-up-your-environment-and-deploy-the-contract)
* [Step 3: Call a Function on the Deployed Contract](#step-3-call-a-function-on-the-deployed-contract)
* [Conclusion](#conclusion)

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