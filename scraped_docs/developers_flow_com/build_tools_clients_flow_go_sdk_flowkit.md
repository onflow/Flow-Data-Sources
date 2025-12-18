# Source: https://developers.flow.com/build/tools/clients/flow-go-sdk/flowkit

Flow Project Configuration | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        - [Flow Go SDK](/build/tools/clients/flow-go-sdk)

                          * [Flow Project Configuration](/build/tools/clients/flow-go-sdk/flowkit)* [Migration Guide v0.25.0](/build/tools/clients/flow-go-sdk/migration-v0.25.0)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Go SDK](/build/tools/clients/flow-go-sdk)* Flow Project Configuration

On this page

# Flowkit Go Tutorial: Working with Flow Project State

## Introduction[​](#introduction "Direct link to Introduction")

**Flowkit** is a Go package for interacting with the Flow blockchain in the context of `flow.json` configuration files. It provides APIs for managing Flow projects, including:

* Loading and managing project configuration (`flow.json`)
* Resolving import statements in Cadence contracts, scripts, and transactions
* Deploying contracts to different networks (emulator, testnet, mainnet)
* Managing accounts, networks, and deployments
* Executing scripts and building transactions with proper import resolution

Flowkit is the core package used by the Flow CLI and can be integrated into any Go application that needs to interact with Flow projects.

## Installation[​](#installation "Direct link to Installation")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Go 1.25.0 or higher
* A Flow project with a `flow.json` configuration file

### Install the Package[​](#install-the-package "Direct link to Install the Package")

Add Flowkit to your Go module:

`_10

go get github.com/onflow/flowkit/v2`

This will install Flowkit v2 and all its dependencies.

### Import in Your Code[​](#import-in-your-code "Direct link to Import in Your Code")

`_10

import (

_10

"github.com/onflow/flowkit/v2"

_10

"github.com/onflow/flowkit/v2/config"

_10

"github.com/onflow/flowkit/v2/project"

_10

"github.com/spf13/afero"

_10

)`

## Loading Project State[​](#loading-project-state "Direct link to Loading Project State")

The first step when working with Flowkit is loading your project's state from `flow.json`.

### Basic Usage[​](#basic-usage "Direct link to Basic Usage")

`_18

package main

_18

_18

import (

_18

"log"

_18

"github.com/onflow/flowkit/v2"

_18

"github.com/spf13/afero"

_18

)

_18

_18

func main() {

_18

// Load flow.json from the current directory

_18

state, err := flowkit.Load([]string{"flow.json"}, afero.Afero{Fs: afero.NewOsFs()})

_18

if err != nil {

_18

log.Fatalf("Failed to load project state: %v", err)

_18

}

_18

_18

// Now you can work with the project state

_18

log.Println("Project state loaded successfully!")

_18

}`

### Creating a New Project State[​](#creating-a-new-project-state "Direct link to Creating a New Project State")

If you need to create a new project from scratch:

`_10

// Initialize an empty state

_10

state, err := flowkit.Init(afero.Afero{Fs: afero.NewOsFs()})

_10

if err != nil {

_10

log.Fatalf("Failed to initialize state: %v", err)

_10

}`

### Accessing State Components[​](#accessing-state-components "Direct link to Accessing State Components")

The `State` object provides access to all project configuration:

`_14

// Get all contracts

_14

contracts := state.Contracts()

_14

_14

// Get all networks

_14

networks := state.Networks()

_14

_14

// Get all accounts

_14

accounts := state.Accounts()

_14

_14

// Get all deployments

_14

deployments := state.Deployments()

_14

_14

// Get the underlying config

_14

config := state.Config()`

## Working with Contracts[​](#working-with-contracts "Direct link to Working with Contracts")

Contracts are Cadence smart contracts defined in your project.

### Getting Contract Information[​](#getting-contract-information "Direct link to Getting Contract Information")

`_13

// Get a contract by name

_13

contract, err := state.Contracts().ByName("MyContract")

_13

if err != nil {

_13

log.Fatalf("Contract not found: %v", err)

_13

}

_13

_13

log.Printf("Contract: %s\n", contract.Name)

_13

log.Printf("Location: %s\n", contract.Location)

_13

_13

// Get all contract names

_13

for _, c := range *state.Contracts() {

_13

log.Printf("Available contract: %s\n", c.Name)

_13

}`

### Getting Deployment Contracts for a Network[​](#getting-deployment-contracts-for-a-network "Direct link to Getting Deployment Contracts for a Network")

When deploying or executing code, you often need contracts with their target addresses:

`_16

import "github.com/onflow/flowkit/v2/config"

_16

_16

// Get all contracts configured for deployment on testnet

_16

contracts, err := state.DeploymentContractsByNetwork(config.TestnetNetwork)

_16

if err != nil {

_16

log.Fatalf("Failed to get deployment contracts: %v", err)

_16

}

_16

_16

// Each contract includes deployment information

_16

for _, contract := range contracts {

_16

log.Printf("Contract: %s\n", contract.Name)

_16

log.Printf(" Location: %s\n", contract.Location())

_16

log.Printf(" Target Account: %s\n", contract.AccountAddress)

_16

log.Printf(" Account Name: %s\n", contract.AccountName)

_16

log.Printf(" Code Size: %d bytes\n", len(contract.Code()))

_16

}`

## Working with Networks[​](#working-with-networks "Direct link to Working with Networks")

Flowkit supports multiple networks including emulator, testnet, and mainnet.

### Available Networks[​](#available-networks "Direct link to Available Networks")

`_10

import "github.com/onflow/flowkit/v2/config"

_10

_10

// Predefined networks

_10

emulator := config.EmulatorNetwork // Local emulator

_10

testnet := config.TestnetNetwork // Flow testnet

_10

mainnet := config.MainnetNetwork // Flow mainnet

_10

_10

log.Printf("Emulator: %s\n", emulator.Host)

_10

log.Printf("Testnet: %s\n", testnet.Host)

_10

log.Printf("Mainnet: %s\n", mainnet.Host)`

### Getting Networks from State[​](#getting-networks-from-state "Direct link to Getting Networks from State")

`_11

// Get all networks defined in flow.json

_11

networks := state.Networks()

_11

_11

// Get a specific network by name

_11

testnet, err := networks.ByName("testnet")

_11

if err != nil {

_11

log.Fatalf("Network not found: %v", err)

_11

}

_11

_11

log.Printf("Network: %s\n", testnet.Name)

_11

log.Printf("Host: %s\n", testnet.Host)`

### Adding or Updating Networks[​](#adding-or-updating-networks "Direct link to Adding or Updating Networks")

`_14

import "github.com/onflow/flowkit/v2/config"

_14

_14

// Add a custom network

_14

networks := state.Networks()

_14

networks.AddOrUpdate(config.Network{

_14

Name: "custom-network",

_14

Host: "localhost:3570",

_14

})

_14

_14

// Save the updated configuration

_14

err := state.SaveDefault()

_14

if err != nil {

_14

log.Fatalf("Failed to save state: %v", err)

_14

}`

### Getting Network-Specific Aliases[​](#getting-network-specific-aliases "Direct link to Getting Network-Specific Aliases")

Network aliases map contract names/locations to their deployed addresses on specific networks:

`_10

import "github.com/onflow/flowkit/v2/config"

_10

_10

// Get aliases for testnet

_10

aliases := state.AliasesForNetwork(config.TestnetNetwork)

_10

_10

// aliases is a map[string]string of location/name -> address

_10

for location, address := range aliases {

_10

log.Printf("%s deployed at %s on testnet\n", location, address)

_10

}`

## Resolving Imports with ImportReplacer[​](#resolving-imports-with-importreplacer "Direct link to Resolving Imports with ImportReplacer")

The `ImportReplacer` resolves import statements in Cadence contracts, scripts, and transactions by replacing relative file paths and contract names with their deployed blockchain addresses.

### Basic Usage[​](#basic-usage-1 "Direct link to Basic Usage")

When you have a Cadence program with imports like `import "Kibble"`, you need to resolve these to blockchain addresses:

`` _37

import "github.com/onflow/flowkit/v2/project"

_37

import "github.com/onflow/flowkit/v2/config"

_37

_37

// Get contracts for your target network

_37

contracts, err := state.DeploymentContractsByNetwork(config.TestnetNetwork)

_37

if err != nil {

_37

log.Fatal(err)

_37

}

_37

_37

// Create an import replacer with your project's contracts

_37

importReplacer := project.NewImportReplacer(contracts, nil)

_37

_37

// Parse your Cadence program

_37

code := []byte(`

_37

import "Kibble"

_37

import "FungibleToken"

_37

_37

transaction {

_37

prepare(signer: &Account) {

_37

// ...

_37

}

_37

}

_37

`)

_37

_37

program, err := project.NewProgram(code, nil, "")

_37

if err != nil {

_37

log.Fatalf("Failed to parse program: %v", err)

_37

}

_37

_37

// Replace imports with deployed addresses

_37

resolvedProgram, err := importReplacer.Replace(program)

_37

if err != nil {

_37

log.Fatalf("Failed to resolve imports: %v", err)

_37

}

_37

_37

// The resolved program now has addresses instead of file paths

_37

log.Printf("Resolved code:\n%s", string(resolvedProgram.Code())) ``

### Integration with Project State[​](#integration-with-project-state "Direct link to Integration with Project State")

The most common pattern is to use network-specific aliases from your project state:

`_33

// Load project state and get network-specific contracts and aliases

_33

state, err := flowkit.Load([]string{"flow.json"}, afero.Afero{Fs: afero.NewOsFs()})

_33

if err != nil {

_33

log.Fatal(err)

_33

}

_33

_33

// Choose your target network

_33

network := config.TestnetNetwork

_33

_33

// Get contracts for this network

_33

contracts, err := state.DeploymentContractsByNetwork(network)

_33

if err != nil {

_33

log.Fatal(err)

_33

}

_33

_33

// Use network-specific aliases for address mapping

_33

importReplacer := project.NewImportReplacer(

_33

contracts,

_33

state.AliasesForNetwork(network),

_33

)

_33

_33

// Parse and resolve your program

_33

program, err := project.NewProgram(scriptCode, nil, "script.cdc")

_33

if err != nil {

_33

log.Fatalf("Failed to parse program: %v", err)

_33

}

_33

resolvedProgram, err := importReplacer.Replace(program)

_33

if err != nil {

_33

log.Fatalf("Failed to resolve imports: %v", err)

_33

}

_33

_33

// Use the resolved program for execution

_33

log.Printf("Ready to execute:\n%s", string(resolvedProgram.Code()))`

## Working with Accounts[​](#working-with-accounts "Direct link to Working with Accounts")

Accounts represent Flow blockchain accounts used for signing transactions and deploying contracts.

### Getting Account Information[​](#getting-account-information "Direct link to Getting Account Information")

`_25

import "github.com/onflow/flow-go-sdk"

_25

_25

accounts := state.Accounts()

_25

_25

// Get account by name

_25

account, err := accounts.ByName("emulator-account")

_25

if err != nil {

_25

log.Fatalf("Account not found: %v", err)

_25

}

_25

_25

log.Printf("Account: %s\n", account.Name)

_25

log.Printf("Address: %s\n", account.Address)

_25

_25

// Get all account names

_25

names := accounts.Names()

_25

for _, name := range names {

_25

log.Printf("Available account: %s\n", name)

_25

}

_25

_25

// Get account by address

_25

addr := flow.HexToAddress("0xf8d6e0586b0a20c7")

_25

account, err = accounts.ByAddress(addr)

_25

if err != nil {

_25

log.Fatalf("Account not found by address: %v", err)

_25

}`

### Getting the Emulator Service Account[​](#getting-the-emulator-service-account "Direct link to Getting the Emulator Service Account")

`_10

// Get the emulator's default service account

_10

serviceAccount, err := state.EmulatorServiceAccount()

_10

if err != nil {

_10

log.Fatalf("Failed to get service account: %v", err)

_10

}

_10

_10

log.Printf("Service account address: %s\n", serviceAccount.Address)`

## Working with Deployments[​](#working-with-deployments "Direct link to Working with Deployments")

Deployments define which contracts should be deployed to which accounts on specific networks.

### Getting Deployment Information[​](#getting-deployment-information "Direct link to Getting Deployment Information")

`_20

deployments := state.Deployments()

_20

_20

// Get all deployments for a network

_20

testnetDeployments := deployments.ByNetwork("testnet")

_20

_20

for _, deployment := range testnetDeployments {

_20

log.Printf("Account: %s\n", deployment.Account)

_20

log.Printf("Network: %s\n", deployment.Network)

_20

log.Printf("Contracts:\n")

_20

_20

for _, contract := range deployment.Contracts {

_20

log.Printf(" - %s\n", contract.Name)

_20

}

_20

}

_20

_20

// Get deployment for specific account and network

_20

deployment := deployments.ByAccountAndNetwork("my-account", "testnet")

_20

if deployment != nil {

_20

log.Printf("Found deployment: %d contracts\n", len(deployment.Contracts))

_20

}`

## Complete Example[​](#complete-example "Direct link to Complete Example")

Here's a complete example that ties everything together:

`` _71

package main

_71

_71

import (

_71

"log"

_71

_71

"github.com/onflow/flowkit/v2"

_71

"github.com/onflow/flowkit/v2/config"

_71

"github.com/onflow/flowkit/v2/project"

_71

"github.com/spf13/afero"

_71

)

_71

_71

func main() {

_71

// 1. Load project state

_71

state, err := flowkit.Load([]string{"flow.json"}, afero.Afero{Fs: afero.NewOsFs()})

_71

if err != nil {

_71

log.Fatalf("Failed to load state: %v", err)

_71

}

_71

_71

// 2. Choose target network

_71

network := config.TestnetNetwork

_71

log.Printf("Using network: %s\n", network.Name)

_71

_71

// 3. Get deployment contracts for the network

_71

contracts, err := state.DeploymentContractsByNetwork(network)

_71

if err != nil {

_71

log.Fatalf("Failed to get contracts: %v", err)

_71

}

_71

_71

log.Printf("Found %d contracts for deployment\n", len(contracts))

_71

for _, contract := range contracts {

_71

log.Printf(" - %s -> %s\n", contract.Name, contract.AccountAddress)

_71

}

_71

_71

// 4. Get network aliases

_71

aliases := state.AliasesForNetwork(network)

_71

log.Printf("Network has %d aliases\n", len(aliases))

_71

_71

// 5. Create import replacer

_71

importReplacer := project.NewImportReplacer(contracts, aliases)

_71

_71

// 6. Resolve imports in a script

_71

scriptCode := []byte(`

_71

import "Kibble"

_71

import "FungibleToken"

_71

_71

access(all) fun main(): String {

_71

return "Hello, Flow!"

_71

}

_71

`)

_71

_71

program, err := project.NewProgram(scriptCode, nil, "script.cdc")

_71

if err != nil {

_71

log.Fatalf("Failed to parse program: %v", err)

_71

}

_71

resolvedProgram, err := importReplacer.Replace(program)

_71

if err != nil {

_71

log.Fatalf("Failed to resolve imports: %v", err)

_71

}

_71

_71

log.Printf("Resolved script:\n%s\n", string(resolvedProgram.Code()))

_71

_71

// 7. Get account for signing

_71

account, err := state.Accounts().ByName("testnet-account")

_71

if err != nil {

_71

log.Fatalf("Failed to get account: %v", err)

_71

}

_71

_71

log.Printf("Using account: %s (%s)\n", account.Name, account.Address)

_71

_71

log.Println("Setup complete! Ready to interact with Flow.")

_71

} ``

## Conclusion[​](#conclusion "Direct link to Conclusion")

Flowkit provides a powerful and flexible API for managing Flow projects in Go. By understanding how to work with project state, contracts, networks, and import resolution, you can build robust applications that interact with the Flow blockchain.

The import replacer is particularly critical for ensuring your Cadence code works correctly across different networks by automatically resolving contract imports to their deployed addresses.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/flow-go-sdk/flowkit.md)

Last updated on **Nov 4, 2025** by **Jordan Ribbink**

[Previous

Flow Go SDK](/build/tools/clients/flow-go-sdk)[Next

Migration Guide v0.25.0](/build/tools/clients/flow-go-sdk/migration-v0.25.0)

###### Rate this page

😞😐😊

Copy as Markdown

* [Introduction](#introduction)* [Installation](#installation)
    + [Prerequisites](#prerequisites)+ [Install the Package](#install-the-package)+ [Import in Your Code](#import-in-your-code)* [Loading Project State](#loading-project-state)
      + [Basic Usage](#basic-usage)+ [Creating a New Project State](#creating-a-new-project-state)+ [Accessing State Components](#accessing-state-components)* [Working with Contracts](#working-with-contracts)
        + [Getting Contract Information](#getting-contract-information)+ [Getting Deployment Contracts for a Network](#getting-deployment-contracts-for-a-network)* [Working with Networks](#working-with-networks)
          + [Available Networks](#available-networks)+ [Getting Networks from State](#getting-networks-from-state)+ [Adding or Updating Networks](#adding-or-updating-networks)+ [Getting Network-Specific Aliases](#getting-network-specific-aliases)* [Resolving Imports with ImportReplacer](#resolving-imports-with-importreplacer)
            + [Basic Usage](#basic-usage-1)+ [Integration with Project State](#integration-with-project-state)* [Working with Accounts](#working-with-accounts)
              + [Getting Account Information](#getting-account-information)+ [Getting the Emulator Service Account](#getting-the-emulator-service-account)* [Working with Deployments](#working-with-deployments)
                + [Getting Deployment Information](#getting-deployment-information)* [Complete Example](#complete-example)* [Conclusion](#conclusion)

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