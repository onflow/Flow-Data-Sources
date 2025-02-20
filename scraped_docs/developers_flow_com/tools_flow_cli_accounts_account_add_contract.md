# Source: https://developers.flow.com/tools/flow-cli/accounts/account-add-contract




Deploy a Contract | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
    - [Get an Account](/tools/flow-cli/accounts/get-accounts)
    - [Create an Account](/tools/flow-cli/accounts/create-accounts)
    - [Deploy a Contract](/tools/flow-cli/accounts/account-add-contract)
    - [Update a Contract](/tools/flow-cli/accounts/account-update-contract)
    - [Remove a Contract](/tools/flow-cli/accounts/account-remove-contract)
    - [Account Staking Info](/tools/flow-cli/accounts/account-staking-info)
    - [Funding a Testnet Account](/tools/flow-cli/accounts/account-fund)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* [Flow CLI](/tools/flow-cli)
* Accounts
* Deploy a Contract
On this page
# Deploy a Contract

Deploy a new contract to a Flow account using the Flow CLI.

 `_10flow accounts add-contract <filename> [<argument> <argument>...] [flags]`

⚠️ Deprecation notice: using name argument in adding contract command will be deprecated soon.

 `_10flow accounts add-contract <name> <filename> [<argument> <argument>...] [flags]`
## Example Usage[​](#example-usage "Direct link to Example Usage")

 `_18> flow accounts add-contract ./FungibleToken.cdc_18_18Contract 'FungibleToken' deployed to the account 0xf8d6e0586b0a20c7_18_18Address 0xf8d6e0586b0a20c7_18Balance 99999999999.70000000_18Keys 1_18_18Key 0 Public Key 640a5a359bf3536d15192f18d872d57c98a96cb871b92b70cecb0739c2d5c37b4be12548d3526933c2cda9b0b9c69412f45ffb6b85b6840d8569d969fe84e5b7_18 Weight 1000_18 Signature Algorithm ECDSA_P256_18 Hash Algorithm SHA3_256_18 Revoked false_18 Sequence Number 6_18 Index 0_18_18Contracts Deployed: 1_18Contract: 'FungibleToken'`

**Testnet Example**

 `_18> flow accounts add-contract ./FungibleToken.cdc --signer alice --network testnet_18_18Contract 'FungibleToken' deployed to the account 0xf8d6e0586b0a20c7_18_18Address 0xf8d6e0586b0a20c7_18Balance 99999999999.70000000_18Keys 1_18_18Key 0 Public Key 640a5a359bf3536d15192f18d872d57c98a96cb871b92b70cecb0739c2d5c37b4be12548d3526933c2cda9b0b9c69412f45ffb6b85b6840d8569d969fe84e5b7_18 Weight 1000_18 Signature Algorithm ECDSA_P256_18 Hash Algorithm SHA3_256_18 Revoked false_18 Sequence Number 6_18 Index 0_18_18Contracts Deployed: 1_18Contract: 'FungibleToken'`

*Make sure alice account is defined in flow.json*

## Arguments[​](#arguments "Direct link to Arguments")

### Name[​](#name "Direct link to Name")

* Name: `name`
* Valid inputs: any string value.

Name of the contract as it is defined in the contract source code.

⚠️ Deprecation notice: use filename argument only, no need to use name argument.

### Filename[​](#filename "Direct link to Filename")

* Name: `filename`
* Valid inputs: a path in the current filesystem.

Path to the file containing the contract source code.

### Arguments[​](#arguments-1 "Direct link to Arguments")

* Name: `argument`
* Valid inputs: valid [cadence values](https://cadencelang.dev/docs/1.0/json-cadence-spec)
  matching argument type in transaction code.

Input arguments values matching corresponding types in the source code and passed in the same order.

Example:

 `_10> flow accounts add-contract ./contract.cdc Hello 2`

Transaction code:

 `_10access(all) contract HelloWorld {_10 init(a:String, b:Int) {_10 }_10}`
## Flags[​](#flags "Direct link to Flags")

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used to sign the transaction.

### Arguments JSON[​](#arguments-json "Direct link to Arguments JSON")

* Flag: `--args-json`
* Valid inputs: arguments in JSON-Cadence form.
* Example: `flow accounts add-contract ./tx.cdc '[{"type": "String", "value": "Hello"}]'`

Arguments passed to the Cadence transaction in Cadence JSON format.
Cadence JSON format contains `type` and `value` keys and is
[documented here](https://cadencelang.dev/docs/1.0/json-cadence-spec).

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `contracts`

Specify fields to include in the result output. Applies only to the text output.

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
* Valid inputs: the name of a network defined in the configuration (`flow.json`).
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/accounts/account-add-contract.md)Last updated on **Feb 6, 2025** by **Brian Doyle**[PreviousCreate an Account](/tools/flow-cli/accounts/create-accounts)[NextUpdate a Contract](/tools/flow-cli/accounts/account-update-contract)
###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Name](#name)
  + [Filename](#filename)
  + [Arguments](#arguments-1)
* [Flags](#flags)
  + [Signer](#signer)
  + [Arguments JSON](#arguments-json)
  + [Include Fields](#include-fields)
  + [Host](#host)
  + [Network Key](#network-key)
  + [Network](#network)
  + [Filter](#filter)
  + [Output](#output)
  + [Save](#save)
  + [Log](#log)
  + [Configuration](#configuration)
  + [Version Check](#version-check)
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

