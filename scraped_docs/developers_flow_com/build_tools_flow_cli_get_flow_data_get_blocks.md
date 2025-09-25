# Source: https://developers.flow.com/build/tools/flow-cli/get-flow-data/get-blocks

Get Block | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)
    - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

      * [Get Block](/build/tools/flow-cli/get-flow-data/get-blocks)
      * [Get Events](/build/tools/flow-cli/get-flow-data/get-events)
      * [Get Collection](/build/tools/flow-cli/get-flow-data/get-collections)
      * [Network Status](/build/tools/flow-cli/get-flow-data/get-status)
    - [Utils](/build/tools/flow-cli/utils/signature-generate)
    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)
    - [Running Cadence Tests](/build/tools/flow-cli/tests)
    - [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)
    - [Cadence Linter](/build/tools/flow-cli/lint)
    - [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)
    - [Data Collection](/build/tools/flow-cli/data-collection)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Flow CLI](/build/tools/flow-cli)
* Flow Entities
* Get Block

On this page

# Get Block

The Flow CLI provides a command to fetch any block from the Flow network.

`_10

flow blocks get <block_id|latest|block_height>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_10

flow blocks get 12884163 --host access.mainnet.nodes.onflow.org:9000 --include transactions`

### Example response[​](#example-response "Direct link to Example response")

`_27

Block ID 2fb7571a6ccf02f3ac42f27c14ce0a4cb119060e4fbd7af36fd51894465e7002

_27

Prent ID 1c5a6267ba9512e141e4e90630cb326cecfbf6113818487449efeb37fc98ca18

_27

Timestamp 2021-03-19 17:46:15.973305066 +0000 UTC

_27

Height 12884163

_27

Status Sealed

_27

Total Seals 2

_27

Total Collections 8

_27

Collection 0: 3e694588e789a72489667a36dd73104dea4579bcd400959d47aedccd7f930eeb

_27

Transaction 0: acc2ae1ff6deb2f4d7663d24af6ab1baf797ec264fd76a745a30792f6882093b

_27

Transaction 1: ae8bfbc85ce994899a3f942072bfd3455823b1f7652106ac102d161c17fcb55c

_27

Transaction 2: 70c4d39d34e654173c5c2746e7bb3a6cdf1f5e6963538d62bad2156fc02ea1b2

_27

Transaction 3: 2466237b5eafb469c01e2e5f929a05866de459df3bd768cde748e068c81c57bf

_27

Collection 1: e93f2bd988d66288c7e1ad991dec227c6c74b8039a430e43896ad94cf8feccce

_27

Transaction 0: 4d790300722b646e7ed3e2c52675430d7ccf2efd1d93f106b53bc348df601af6

_27

Collection 2: c7d93b80ae55809b1328c686f6a8332e8e15083ab32f8b3105c4d910646f54bf

_27

Transaction 0: 95c4efbb30f86029574d6acd7df04afe6108f6fd610d823dfd398c80cfa5e842

_27

Collection 3: 1a4f563b48aaa38f3a7e867c89422e0bd84887de125e8f48ba147f4ee58ddf0d

_27

Transaction 0: fbcc99326336d4dbb4cbc01a3b9b85cfcdcdc071b3d0e01ee88ecd144444600b

_27

Collection 4: 01000c7773cc3c22cba6d8917a2486dc7a1a1842dd7fb7c0e87e63c22bb14abe

_27

Transaction 0: a75097639b434044de0122d3a28620e093f277fa715001e80a035568e118c59f

_27

Collection 5: 6f2b08f9673545a2e61e954feb8d55d2a3ef2b3cef7a8d2f8de527bc42d92c28

_27

Transaction 0: 8ea63d397bd07a25db3f06fb9785dbf09bc652159f68a84c55ea2be606ada1e9

_27

Collection 6: 13b5c48252930824a8c6e846470763582cacdacb772c1e9c584adefced6724b2

_27

Transaction 0: 8ba57a92311367189a89a59bcb3c32192387fefca9bde493e087bc0d479186a8

_27

Transaction 1: 8ab1d99702ccf31b6f4b3acd2580dddd440f08bc07acab4884337c0c593a8f69

_27

Collection 7: bf90fdd2761b8f37565af60fc38165dd09edf0671fdd35b37f718a7eb45e804f

_27

Transaction 0: b92a14c0802183719efed00363d31076d7e50f41a6207781cf34d39c822bbacb`

## Arguments[​](#arguments "Direct link to Arguments")

### Query[​](#query "Direct link to Query")

* Name: `<block_id|latest|block_height>`
* Valid Input: Block ID, `latest` or block height

Specify the block to retrieve by block ID or block height.

## Arguments[​](#arguments-1 "Direct link to Arguments")

### Address[​](#address "Direct link to Address")

* Name: `address`
* Valid Input: Flow account address

Flow [account address](/build/cadence/basics/accounts) (prefixed with `0x` or not).

## Flags[​](#flags "Direct link to Flags")

### Events[​](#events "Direct link to Events")

* Flag: `--events`
* Valid inputs: Valid event name

List events of this type for the block.

### Include[​](#include "Direct link to Include")

* Flag: `--include`
* Valid inputs: `transactions`

Include additional values in the response.

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used to sign the transaction.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/get-flow-data/get-blocks.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Security](/build/tools/flow-cli/flow.json/security)[Next

Get Events](/build/tools/flow-cli/get-flow-data/get-events)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
  + [Example response](#example-response)
* [Arguments](#arguments)
  + [Query](#query)
* [Arguments](#arguments-1)
  + [Address](#address)
* [Flags](#flags)
  + [Events](#events)
  + [Include](#include)
  + [Signer](#signer)
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

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

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
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.