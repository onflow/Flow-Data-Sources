# Source: https://developers.flow.com/build/tools/flow-cli/deployment/deploy-project-contracts

Deploy a Project | Flow Developer Portal



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

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                    - [Keys](/build/tools/flow-cli/keys/generate-keys)

                      - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                        * [Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)* [Deploy a Project](/build/tools/flow-cli/deployment/deploy-project-contracts)- [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                          - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                            - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                              - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Deploy Project* Deploy a Project

On this page

# Deploy a Project

`_10

flow project deploy`

This command automatically deploys your project's contracts based on the configuration defined in your `flow.json` file.

info

Use Flow CLI commands to configure your project rather than manually edit `flow.json`.

Before you use this command, read about how to
[configure project contracts and deployment targets](/build/tools/flow-cli/deployment/project-contracts) with CLI commands.

## Example usage[​](#example-usage "Direct link to Example usage")

`_10

> flow project deploy --network=testnet

_10

_10

Deploying 2 contracts for accounts: my-testnet-account

_10

_10

NonFungibleToken -> 0x8910590293346ec4

_10

KittyItems -> 0x8910590293346ec4

_10

_10

✨ All contracts deployed successfully`

info

The `flow.json` configuration shown below is created automatically when you use CLI commands. You should use `flow config add contract` and `flow config add deployment` to configure your project rather than manually edit the file. See [Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts) for details.

Your `flow.json` file might look something like this:

`_13

{

_13

...

_13

"contracts": {

_13

"NonFungibleToken": "./cadence/contracts/NonFungibleToken.cdc",

_13

"KittyItems": "./cadence/contracts/KittyItems.cdc"

_13

},

_13

"deployments": {

_13

"testnet": {

_13

"my-testnet-account": ["KittyItems", "NonFungibleToken"]

_13

}

_13

},

_13

...

_13

}`

Here's a sketch of the contract source files:

NonFungibleToken.cdc

`_10

access(all) contract NonFungibleToken {

_10

// ...

_10

}`

KittyItems.cdc

`_10

import "NonFungibleToken"

_10

_10

access(all) contract KittyItems {

_10

// ...

_10

}`

## Initialization arguments[​](#initialization-arguments "Direct link to Initialization arguments")

To deploy contracts that take initialization arguments, you must add those arguments to the deployment configuration.

info

For basic deployments, use `flow config add deployment` to configure your contracts. Initialization arguments are an advanced feature that may require you to manually edit `flow.json` after the basic deployment is configured with CLI commands.

You can specify each deployment as an object that contains
`name` and `args` keys that specify arguments to be
used during the deployment. Example:

`_16

{

_16

"deployments": {

_16

"testnet": {

_16

"my-testnet-account": [

_16

"NonFungibleToken",

_16

{

_16

"name": "Foo",

_16

"args": [

_16

{ "type": "String", "value": "Hello World" },

_16

{ "type": "UInt32", "value": "10" }

_16

]

_16

}

_16

]

_16

}

_16

}

_16

}`

danger

⚠️ **Never** put raw private keys in `flow.json`. Always use `.pkey` files for key storage. Before you proceed, we recommend that you read the [Flow CLI security guidelines](/build/tools/flow-cli/flow.json/security)
to learn about the best practices for private key storage.

## Dependency resolution[​](#dependency-resolution "Direct link to Dependency resolution")

The `deploy` command attempts to resolve the import statements in all contracts being deployed.

After the dependencies are found, the CLI will deploy the contracts in a deterministic order such that no contract is deployed until all of its dependencies are deployed. The command will return an error if no such ordering exists due to one or more cyclic dependencies.

In the example above, `NonFungibleToken` will always be deployed before `KittyItems` since `KittyItems` imports `NonFungibleToken`.

## Address replacement[​](#address-replacement "Direct link to Address replacement")

After it resolves all dependencies, the `deploy` command rewrites each contract so that its dependencies are imported from their *target addresses* rather than their source file location.

The rewritten versions are then deployed to their respective targets, which leaves the original contract files unchanged.

### Contracts that import from other contracts[​](#contracts-that-import-from-other-contracts "Direct link to Contracts that import from other contracts")

In the example above, the `KittyItems` contract would be rewritten like this:

KittyItems.cdc

`_10

import NonFungibleToken from 0xf8d6e0586b0a20c7

_10

_10

access(all) contract KittyItems {

_10

// ...

_10

}`

### Contracts that import from dependencies[​](#contracts-that-import-from-dependencies "Direct link to Contracts that import from dependencies")

When your contracts import from the `dependencies` section, the deploy command uses the network-specific aliases defined in those dependencies.

**Example `flow.json` with dependencies:**

`_35

{

_35

"contracts": {

_35

"ExampleConnectors": {

_35

"source": "cadence/contracts/ExampleConnectors.cdc",

_35

"aliases": {

_35

"testing": "0000000000000007"

_35

}

_35

}

_35

},

_35

"dependencies": {

_35

"FlowToken": {

_35

"source": "mainnet://1654653399040a61.FlowToken",

_35

"hash": "cefb25fd19d9fc80ce02896267eb6157a6b0df7b1935caa8641421fe34c0e67a",

_35

"aliases": {

_35

"emulator": "0ae53cb6e3f42a79",

_35

"mainnet": "1654653399040a61",

_35

"testnet": "7e60df042a9c0868"

_35

}

_35

},

_35

"FungibleToken": {

_35

"source": "mainnet://f233dcee88fe0abe.FungibleToken",

_35

"hash": "23c1159cf99b2b039b6b868d782d57ae39b8d784045d81597f100a4782f0285b",

_35

"aliases": {

_35

"emulator": "ee82856bf20e2aa6",

_35

"mainnet": "f233dcee88fe0abe",

_35

"testnet": "9a0766d93b6608b7"

_35

}

_35

}

_35

},

_35

"deployments": {

_35

"testnet": {

_35

"testnet-account": ["ExampleConnectors"]

_35

}

_35

}

_35

}`

**Original contract source:**

ExampleConnectors.cdc

`_10

import "FungibleToken"

_10

import "FlowToken"

_10

_10

access(all) contract ExampleConnectors {

_10

// ...

_10

}`

**Rewritten for testnet deployment:**

ExampleConnectors.cdc

`_10

import FungibleToken from 0x9a0766d93b6608b7

_10

import FlowToken from 0x7e60df042a9c0868

_10

_10

access(all) contract ExampleConnectors {

_10

// ...

_10

}`

**Rewritten for mainnet deployment:**

ExampleConnectors.cdc

`_10

import FungibleToken from 0xf233dcee88fe0abe

_10

import FlowToken from 0x1654653399040a61

_10

_10

access(all) contract ExampleConnectors {

_10

// ...

_10

}`

The deploy command automatically uses the addresses from the `dependencies` section's aliases for the target network. Notice how the addresses change based on the network—testnet uses `0x9a0766d93b6608b7` for `FungibleToken`, while mainnet uses `0xf233dcee88fe0abe`. Contracts in the `dependencies` section are not deployed—they're assumed to already exist on the network at the addresses specified in their aliases.

## Merge multiple configuration files[​](#merge-multiple-configuration-files "Direct link to Merge multiple configuration files")

You can use the `-f` flag multiple times to merge several configuration files.

If there is an overlap in any of the fields in the configuration between two or more configuration files, the value of the overlapped field in the configuration that results will come from the configuration file that is on the further right order in the list of configuration files specified in the `-f` flag.

danger

**Never** put raw private keys in `flow.json`. Always use `.pkey` files for key storage.

info

Use `flow config add account` to create accounts in your main `flow.json` file. The merging feature is useful to separate sensitive account information into a separate file that you can exclude from version control.

**Example usage:**

`_10

flow project deploy -f flow.json -f private.json`

**Example configuration files:**

flow.json

`_18

{

_18

"accounts": {

_18

"admin-account": {

_18

"address": "f8d6e0586b0a20c7",

_18

"key": {

_18

"type": "file",

_18

"location": "admin-account.pkey"

_18

}

_18

},

_18

"test-account": {

_18

"address": "f8d6e0586b0a20c8",

_18

"key": {

_18

"type": "file",

_18

"location": "test-account.pkey"

_18

}

_18

}

_18

}

_18

}`

private.json

`_11

{

_11

"accounts": {

_11

"admin-account": {

_11

"address": "f1d6e0586b0a20c7",

_11

"key": {

_11

"type": "file",

_11

"location": "admin-account-private.pkey"

_11

}

_11

}

_11

}

_11

}`

When you use multiple configuration files with overlapping fields, the rightmost file takes precedence.
In this example, the merged configuration that results will be:

`_18

{

_18

"accounts": {

_18

"admin-account": {

_18

"address": "f1d6e0586b0a20c7",

_18

"key": {

_18

"type": "file",

_18

"location": "admin-account-private.pkey"

_18

}

_18

},

_18

"test-account": {

_18

"address": "f8d6e0586b0a20c8",

_18

"key": {

_18

"type": "file",

_18

"location": "test-account.pkey"

_18

}

_18

}

_18

}

_18

}`

**Security best practice:** Ensure `.pkey` files are added to `.gitignore` to prevent accidentally committing private keys to version control.

## Flags[​](#flags "Direct link to Flags")

### Allow updates[​](#allow-updates "Direct link to Allow updates")

* Flag: `--update`
* Valid inputs: `true`, `false`
* Default: `false`

Indicate whether to overwrite and upgrade current contracts. The system will only overwrite contracts that are different from current contracts.

### Show update diff[​](#show-update-diff "Direct link to Show update diff")

* Flag: `--show-diff`
* Valid inputs: `true`, `false`
* Default: `false`

Shows a diff to approve before an update between deployed contract and new contract updates.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be used to execute the command. This flag overrides any host defined by the `--network` flag.

### Network key[​](#network-key "Direct link to Network key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be used to create a secure GRPC client when executing the command.

### Network[​](#network "Direct link to Network")

* Flag: `--network`
* Short Flag: `-n`
* Valid inputs: the name of a network defined in the configuration (`flow.json`)
* Default: `emulator`

Specify which network you want the command to use for execution.

### Filter[​](#filter "Direct link to Filter")

* Flag: `--filter`
* Short Flag: `-x`
* Valid inputs: a case-sensitive name of the result property.

Specify any property name from the result you want to return as the only value.

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify the format of the command results.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: a path in the current filesystem.

Specify the filename where you want the result to be saved

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see during command execution.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: a path in the current filesystem.
* Default: `flow.json`

Specify the path to the `flow.json` configuration file.
You can use the `-f` flag multiple times to merge
several configuration files.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/deployment/deploy-project-contracts.md)

Last updated on **Dec 10, 2025** by **cshannon1218**

[Previous

Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)[Next

Execute a Script](/build/tools/flow-cli/scripts/execute-scripts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example usage](#example-usage)* [Initialization arguments](#initialization-arguments)* [Dependency resolution](#dependency-resolution)* [Address replacement](#address-replacement)
        + [Contracts that import from other contracts](#contracts-that-import-from-other-contracts)+ [Contracts that import from dependencies](#contracts-that-import-from-dependencies)* [Merge multiple configuration files](#merge-multiple-configuration-files)* [Flags](#flags)
            + [Allow updates](#allow-updates)+ [Show update diff](#show-update-diff)+ [Host](#host)+ [Network key](#network-key)+ [Network](#network)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version Check](#version-check)

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