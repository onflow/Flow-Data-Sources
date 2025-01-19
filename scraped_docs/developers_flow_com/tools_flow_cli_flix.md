# Source: https://developers.flow.com/tools/flow-cli/flix




Flow Interaction Templates (FLIX) | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
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
* Flow Interaction Templates (FLIX)
On this page
# Flow Interaction Templates (FLIX)

FLIX helps developers reuse existing Cadence transactions and scripts to easily integrate with existing Cadence smart contracts. Get more information about [Flow Interaction Templates](/build/advanced-concepts/flix)

## Introduction[​](#introduction "Direct link to Introduction")

The Flow CLI provides a `flix` command with a few sub commands `execute` and `package`. Get familiar with Flow Interaction Templates [(FLIX)](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md). FLIX are a standard for distributing Cadence scripts and transactions, and metadata in a way that is consumable by tooling and wallets. FLIX can be audited for correctness and safety by auditors in the ecosystem.

 `_10>flow flix_10execute, generate, package_10_10Usage:_10 flow flix [command]_10_10Available Commands:_10 execute execute FLIX template with a given id, name, local filename, or url_10 generate generate FLIX json template given local Cadence filename_10 package package file for FLIX template fcl-js is default`
### Execute[​](#execute "Direct link to Execute")

The Flow CLI provides a `flix` command to `execute` FLIX. The Cadence being execute in the FLIX can be a transaction or script.

 `_10flow flix execute <query> [<argument> <argument>...] [flags]`
warning

A FLIX template might only support testnet and/or mainnet. Generally, emulator is not supported. This can be the case if the FLIX template relies on contract dependencies.

Queries can be a FLIX `id`, `name`, `url` or `path` to a local FLIX file.

### Execute Usage[​](#execute-usage "Direct link to Execute Usage")

 `_10# Execute a FLIX transaction by name on Testnet_10flow flix execute transfer-flow 5.0 "0x123" --network testnet --signer "testnet-account"`
 `_10# Execute a FLIX script by id on Testnet_10flow flix execute bd10ab0bf472e6b58ecc0398e9b3d1bd58a4205f14a7099c52c0640d9589295f --network testnet`
 `_10# Execute a local FLIX script by path on Testnet_10flow flix execute ./multiply.template.json 2 3 --network testnet`

The Flow CLI provides a `flix` command to `package` up generated plain and simple JavaScript. This JavaScript uses FCL (Flow Client Library) to call the cadence the Flow Interaction Templates (FLIX) is based on.

info

Currently, `flix package` command only supports generating FCL (Flow Client Library) specific JavaScript and TypeScirpt, there are plans to support other languages like golang.


 `_10flow flix package <query> [flags]`
### Generate[​](#generate "Direct link to Generate")

Generate FLIX json file. This command will take in a Cadence file and produce a FLIX json file. There are two ways to provide metadata to populate the FLIX json structure.

* Use `--pre-fill` flag to pass in a pre populated FLIX json structure
* Use `--exclude-networks` flag to specify excluded networks when generating a FLIX templates. Example, `--exclude-networks testnet,mainnet`

warning

When generating a FLIX template, make sure all contract dependencies have been deployed to the supported networks. Add any aliases to your flow.json that will be needed to populate dependencies. Verify all dependencies have been populated after generating.

### Generate Usage[​](#generate-usage "Direct link to Generate Usage")

 `_10# Generate FLIX json file using cadence transaction or script, this example is not using a prefilled json file so will not have associated message metadata _10flow flix generate cadence/transactions/update-helloworld.cdc --save cadence/templates/update-helloworld.template.json`

Example of Cadence simple, no metadata associated

 `_10_10import "HelloWorld"_10access(all) fun main(): String {_10 return HelloWorld.greeting_10}`
### Cadence Doc Pragma:[​](#cadence-doc-pragma "Direct link to Cadence Doc Pragma:")

It's recommended to use pragma to set the metadata for the script or transaction. More information on [Cadence Doc Pragma FLIP](https://github.com/onflow/flips/blob/main/application/20230406-interaction-template-cadence-doc.md)

A pragma is short for "pragmatic information", it's special instructions to convey information to a processor in this case the utility that generates FLIX.

 `_19import "HelloWorld"_19_19#interaction (_19 version: "1.1.0",_19 title: "Update Greeting",_19 description: "Update the greeting on the HelloWorld contract",_19 language: "en-US",_19)_19_19transaction(greeting: String) {_19_19 prepare(acct: &Account) {_19 log(acct.address)_19 }_19_19 execute {_19 HelloWorld.updateGreeting(newGreeting: greeting)_19 }_19}`
info

Cadence v0.42.7 supports additional Cadence pragma functionality that FlIX utility can use to generate FLIX. It will support parameters "title" and "description".

The resulting json metadata is extracted from Cadence Doc Pragma

 `_39{_39 "f_type": "InteractionTemplate",_39 "f_version": "1.1.0",_39 "id": "",_39 "data": {_39 "type": "transaction",_39 "interface": "",_39 "messages": [_39 {_39 "key": "title",_39 "i18n": [_39 {_39 "tag": "en-US",_39 "translation": "Update Greeting"_39 }_39 ]_39 },_39 {_39 "key": "description",_39 "i18n": [_39 {_39 "tag": "en-US",_39 "translation": "Update the greeting on the HelloWorld contract"_39 }_39 ]_39 }_39 ],_39 "cadence": {},_39 "dependencies": [],_39 "parameters": [_39 {_39 "label": "greeting",_39 "index": 0,_39 "type": "String",_39 "messages": []_39 }_39 ]_39 }_39}`

Example of using a prefilled FLIX json file. No need to use Cadence pragma when using a prefilled FLIX json file. This method separates FLIX specific information from the transaction or script Cadence. Use the `flow flix generate` command:

 `_10flow flix generate cadence/scripts/read-helloworld.cdc --pre-fill cadence/templates/read-helloworld.prefill.json --save cadence/templates/read-helloworld.template.json`

Using a pre-filled FLIX template, the cadence can be simple but no metadata accompanies it.

 `_10import "HelloWorld"_10access(all) fun main(): String {_10 return HelloWorld.greeting_10}`

Example of json prefill file with message metadata:

 `_29{_29 "f_type": "InteractionTemplate",_29 "f_version": "1.1.0",_29 "id": "",_29 "data": {_29 "type": "script",_29 "interface": "",_29 "messages": [_29 {_29 "key": "title",_29 "i18n": [_29 {_29 "tag": "en-US",_29 "translation": "Get Greeting"_29 }_29 ]_29 },_29 {_29 "key": "description",_29 "i18n": [_29 {_29 "tag": "en-US",_29 "translation": "Call HelloWorld contract to get greeting"_29 }_29 ]_29 }_29 ]_29 }_29}`

The resulting FLIX json file after generation:

 `_62{_62 "f_type": "InteractionTemplate",_62 "f_version": "1.1.0",_62 "id": "fd9abd34f51741401473eb1cf676b105fed28b50b86220a1619e50d4f80b0be1",_62 "data": {_62 "type": "script",_62 "interface": "",_62 "messages": [_62 {_62 "key": "title",_62 "i18n": [_62 {_62 "tag": "en-US",_62 "translation": "Get Greeting"_62 }_62 ]_62 },_62 {_62 "key": "description",_62 "i18n": [_62 {_62 "tag": "en-US",_62 "translation": "Call HelloWorld contract to get greeting"_62 }_62 ]_62 }_62 ],_62 "cadence": {_62 "body": "import \"HelloWorld\"\naccess(all) fun main(): String {\n return HelloWorld.greeting\n}\n",_62 "network_pins": [_62 {_62 "network": "testnet",_62 "pin_self": "41c4c25562d467c534dc92baba92e0c9ab207628731ee4eb4e883425abda692c"_62 }_62 ]_62 },_62 "dependencies": [_62 {_62 "contracts": [_62 {_62 "contract": "HelloWorld",_62 "networks": [_62 {_62 "network": "testnet",_62 "address": "0xe15193734357cf5c",_62 "dependency_pin_block_height": 137864533,_62 "dependency_pin": {_62 "pin": "aad46badcab3caaeb4f0435625f43e15bb4c15b1d55c74a89e6f04850c745858",_62 "pin_self": "a06b3cd29330a3c22df3ac2383653e89c249c5e773fd4bbee73c45ea10294b97",_62 "pin_contract_name": "HelloWorld",_62 "pin_contract_address": "0xe15193734357cf5c",_62 "imports": []_62 }_62 }_62 ]_62 }_62 ]_62 }_62 ],_62 "parameters": null_62 }_62}`
### Package[​](#package "Direct link to Package")

Queries can be a FLIX `url` or `path` to a local FLIX file. This command leverages [FCL](/tools/clients/fcl-js) which will execute FLIX cadence code. Package files can be generated in JavaScript or TypeScript.

warning

Currently package doesn't support `id`, `name` flix query.

### Package Usage[​](#package-usage "Direct link to Package Usage")

 `_10# Generate packaged code that leverages FCL to call the Cadence transaction code, `--save` flag will save the output to a specific file_10flow flix package transfer-flow --save ./package/transfer-flow.js`
 `_10# Generate package code for a FLIX script using id, since there is no saving file, the result will display in terminal_10flow flix package bd10ab0bf472e6b58ecc0398e9b3d1bd58a4205f14a7099c52c0640d9589295f`
 `_10# Generate package code using local template file to save in a local file _10flow flix package ./multiply.template.json --save ./multiply.js`
 `_10# Generate package code using local template file to save in a local typescript file _10flow flix package ./multiply.template.json --lang ts --save ./multiply.ts`
### Example Package Output[​](#example-package-output "Direct link to Example Package Output")

 `_10flow flix package https://flix.flow.com/v1/templates\?name\=transfer-flow`
 `_25_25/**_25 This binding file was auto generated based on FLIX template v1.0.0. _25 Changes to this file might get overwritten._25 Note fcl version 1.3.0 or higher is required to use templates. _25**/_25_25import * as fcl from "@onflow/fcl"_25const flixTemplate = "https://flix.flow.com/v1/templates?name=transfer-flow"_25_25/**_25* Transfer tokens from one account to another_25* @param {Object} Parameters - parameters for the cadence_25* @param {string} Parameters.amount - The amount of FLOW tokens to send: UFix64_25* @param {string} Parameters.to - The Flow account the tokens will go to: Address_25* @returns {Promise<string>} - returns a promise which resolves to the transaction id_25*/_25export async function transferTokens({amount, to}) {_25 const transactionId = await fcl.mutate({_25 template: flixTemplate,_25 args: (arg, t) => [arg(amount, t.UFix64), arg(to, t.Address)]_25 });_25_25 return transactionId_25}`
 `_10# Generate TypeScript version of package file _10flow flix package https://flix.flow.com/v1/templates?name=transfer-flow --lang ts`
 `_29_29/**_29 This binding file was auto generated based on FLIX template v1.1.0. _29 Changes to this file might get overwritten._29 Note fcl version 1.9.0 or higher is required to use templates. _29**/_29_29import * as fcl from "@onflow/fcl"_29const flixTemplate = "https://flix.flow.com/v1/templates?name=transfer-flow"_29_29interface TransferTokensParams {_29 amount: string; // The amount of FLOW tokens to send_29 to: string; // The Flow account the tokens will go to_29}_29_29/**_29* transferTokens: Transfer tokens from one account to another_29* @param string amount - The amount of FLOW tokens to send_29* @param string to - The Flow account the tokens will go to_29* @returns {Promise<string>} - Returns a promise that resolves to the transaction ID_29*/_29export async function transferTokens({amount, to}: TransferTokensParams): Promise<string> {_29 const transactionId = await fcl.mutate({_29 template: flixTemplate,_29 args: (arg, t) => [arg(amount, t.UFix64), arg(to, t.Address)]_29 });_29_29 return transactionId_29}`
warning

Notice that fcl v1.9.0 is needed to use FLIX v1.1 templates

## Resources[​](#resources "Direct link to Resources")

To find out more about FLIX, see the [read the FLIP](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md).

For a list of all templates, check out the [FLIX template repository](https://github.com/onflow/flow-interaction-template-service/tree/master/templates).

To generate a FLIX, see the [FLIX CLI readme](https://github.com/onflow/flow-interaction-template-tools/tree/master/cli).

## Arguments[​](#arguments "Direct link to Arguments")

* Name: `argument`
* Valid input: valid [FLIX](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md)

Input argument value matching corresponding types in the source code and passed in the same order.
You can pass a `nil` value to optional arguments by executing the flow FLIX execute script like this: `flow flix execute template.json nil`.

## Flags[​](#flags "Direct link to Flags")

### Arguments JSON[​](#arguments-json "Direct link to Arguments JSON")

* Flag: `--args-json`
* Valid inputs: arguments in JSON-Cadence form.
* Example: `flow flix execute template.script.json '[{"type": "String", "value": "Hello World"}]'`

Arguments passed to the Cadence script in the Cadence JSON format.
Cadence JSON format contains `type` and `value` keys and is
[documented here](https://cadencelang.dev/docs/1.0/json-cadence-spec).

## Pre Fill[​](#pre-fill "Direct link to Pre Fill")

* Flag: `--pre-fill`
* Valid inputs: a json file in the FLIX json structure [FLIX json format](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md)

## Block Height[​](#block-height "Direct link to Block Height")

* Flag: `--block-height`
* Valid inputs: a block height number

## Block ID[​](#block-id "Direct link to Block ID")

* Flag: `--block-id`
* Valid inputs: a block ID

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used to sign the transaction.

### Proposer[​](#proposer "Direct link to Proposer")

* Flag: `--proposer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used as proposer in the transaction.

### Payer[​](#payer "Direct link to Payer")

* Flag: `--payer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used as payer in the transaction.

### Authorizer[​](#authorizer "Direct link to Authorizer")

* Flag: `--authorizer`
* Valid inputs: the name of a single or multiple comma-separated accounts defined in the configuration (`flow.json`)

Specify the name of the account(s) that will be used as authorizer(s) in the transaction. If you want to provide multiple authorizers separate them using commas (e.g. `alice,bob`)

### Gas Limit[​](#gas-limit "Direct link to Gas Limit")

* Flag: `--gas-limit`
* Valid inputs: an integer greater than zero.
* Default: `1000`

Specify the gas limit for this transaction.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/flix.md)Last updated on **Dec 24, 2024** by **Navid TehraniFar**[PreviousCadence Linter](/tools/flow-cli/lint)[NextCadence Boilerplate](/tools/flow-cli/boilerplate)
###### Rate this page

😞😐😊

* [Introduction](#introduction)
  + [Execute](#execute)
  + [Execute Usage](#execute-usage)
  + [Generate](#generate)
  + [Generate Usage](#generate-usage)
  + [Cadence Doc Pragma:](#cadence-doc-pragma)
  + [Package](#package)
  + [Package Usage](#package-usage)
  + [Example Package Output](#example-package-output)
* [Resources](#resources)
* [Arguments](#arguments)
* [Flags](#flags)
  + [Arguments JSON](#arguments-json)
* [Pre Fill](#pre-fill)
* [Block Height](#block-height)
* [Block ID](#block-id)
  + [Signer](#signer)
  + [Proposer](#proposer)
  + [Payer](#payer)
  + [Authorizer](#authorizer)
  + [Gas Limit](#gas-limit)
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

