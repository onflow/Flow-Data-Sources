# Source: https://developers.flow.com/tools/flow-cli/deployment/deploy-project-contracts

Deploy a Project | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Deploy Project* Deploy a Project

On this page

# Deploy a Project

`_10

flow project deploy`

This command automatically deploys your project's contracts based on the
configuration defined in your `flow.json` file.

Before using this command, read about how to
[configure project contracts and deployment targets](/build/tools/flow-cli/deployment/project-contracts).

## Example Usage[​](#example-usage "Direct link to Example Usage")

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

In the example above, your `flow.json` file might look something like this:

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

import NonFungibleToken from "./NonFungibleToken.cdc"

_10

_10

access(all) contract KittyItems {

_10

// ...

_10

}`

## Initialization Arguments[​](#initialization-arguments "Direct link to Initialization Arguments")

Deploying contracts that take initialization arguments
can be achieved with adding those arguments to the configuration.

Each deployment can be specified as an object containing
`name` and `args` key specifying arguments to be
used during the deployment. Example:

`_14

...

_14

"deployments": {

_14

"testnet": {

_14

"my-testnet-account": [

_14

"NonFungibleToken", {

_14

"name": "Foo",

_14

"args": [

_14

{ "type": "String", "value": "Hello World" },

_14

{ "type": "UInt32", "value": "10" }

_14

]

_14

}]

_14

}

_14

}

_14

...`

⚠️ Warning: before proceeding,
we recommend reading the [Flow CLI security guidelines](/build/tools/flow-cli/flow.json/security)
to learn about the best practices for private key storage.

## Dependency Resolution[​](#dependency-resolution "Direct link to Dependency Resolution")

The `deploy` command attempts to resolve the import statements in all contracts being deployed.

After the dependencies are found, the CLI will deploy the contracts in a deterministic order
such that no contract is deployed until all of its dependencies are deployed.
The command will return an error if no such ordering exists due to one or more cyclic dependencies.

In the example above, `Foo` will always be deployed before `Bar`.

## Address Replacement[​](#address-replacement "Direct link to Address Replacement")

After resolving all dependencies, the `deploy` command rewrites each contract so
that its dependencies are imported from their *target addresses* rather than their
source file location.

The rewritten versions are then deployed to their respective targets,
leaving the original contract files unchanged.

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

## Merging Multiple Configuration Files[​](#merging-multiple-configuration-files "Direct link to Merging Multiple Configuration Files")

You can use the `-f` flag multiple times to merge several configuration files.

If there is an overlap in any of the fields in the configuration between two or more configuration files, the value of
the overlapped field in the resulting configuration will come from the configuration file that is on the further right
order in the list of configuration files specified in the -f flag

Let's look at an example of `deploy` commands with multiple configuration files below

flow.json

`_12

{

_12

"accounts": {

_12

"admin-account": {

_12

"address": "f8d6e0586b0a20c7",

_12

"key": "21c5dfdeb0ff03a7a73ef39788563b62c89adea67bbb21ab95e5f710bd1d40b7"

_12

},

_12

"test-account": {

_12

"address": "f8d6e0586b0a20c8",

_12

"key": "52d5dfdeb0ff03a7a73ef39788563b62c89adea67bbb21ab95e5f710bd1d51c9"

_12

}

_12

}

_12

}`

private.json

`_10

{

_10

"accounts":{

_10

"admin-account":{

_10

"address":"f1d6e0586b0a20c7",

_10

"key":"3335dfdeb0ff03a7a73ef39788563b62c89adea67bbb21ab95e5f710bd1d40b7"

_10

}

_10

}

_10

}`

In the example above, when we try to use the `deploy` command with multiple configuration files and there is an overlap
in the `admin-account` account in `accounts` field of the configuration, the resulting configuration will be like this

> flow project deploy -f flow.json -f private.json

`_12

{

_12

"accounts":{

_12

"admin-account":{

_12

"address":"f1d6e0586b0a20c7",

_12

"key":"3335dfdeb0ff03a7a73ef39788563b62c89adea67bbb21ab95e5f710bd1d40b7"

_12

},

_12

"test-account":{

_12

"address":"f8d6e0586b0a20c8",

_12

"key":"52d5dfdeb0ff03a7a73ef39788563b62c89adea67bbb21ab95e5f710bd1d51c9"

_12

}

_12

}

_12

}`

## Flags[​](#flags "Direct link to Flags")

### Allow Updates[​](#allow-updates "Direct link to Allow Updates")

* Flag: `--update`
* Valid inputs: `true`, `false`
* Default: `false`

Indicate whether to overwrite and upgrade existing contracts. Only contracts with difference with existing contracts
will be overwritten.

### Show Update Diff[​](#show-update-diff "Direct link to Show Update Diff")

* Flag: `--show-diff`
* Valid inputs: `true`, `false`
* Default: `false`

Shows a diff to approve before updating between deployed contract and new contract updates.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be
used to execute the command. This flag overrides
any host defined by the `--network` flag.

### Network Key[​](#network-key "Direct link to Network Key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be
used to create a secure GRPC client when executing the command.

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

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)[Next

Execute a Script](/build/tools/flow-cli/scripts/execute-scripts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)* [Initialization Arguments](#initialization-arguments)* [Dependency Resolution](#dependency-resolution)* [Address Replacement](#address-replacement)* [Merging Multiple Configuration Files](#merging-multiple-configuration-files)* [Flags](#flags)
            + [Allow Updates](#allow-updates)+ [Show Update Diff](#show-update-diff)+ [Host](#host)+ [Network Key](#network-key)+ [Network](#network)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version Check](#version-check)

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