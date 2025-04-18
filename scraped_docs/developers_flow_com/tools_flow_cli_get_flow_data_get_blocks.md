# Source: https://developers.flow.com/tools/flow-cli/get-flow-data/get-blocks

Get Block | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
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

    - [Get Block](/tools/flow-cli/get-flow-data/get-blocks)
    - [Get Events](/tools/flow-cli/get-flow-data/get-events)
    - [Get Collection](/tools/flow-cli/get-flow-data/get-collections)
    - [Network Status](/tools/flow-cli/get-flow-data/get-status)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Flow CLI](/tools/flow-cli)
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

Flow [account address](/build/basics/accounts) (prefixed with `0x` or not).

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/get-flow-data/get-blocks.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Security](/tools/flow-cli/flow.json/security)[Next

Get Events](/tools/flow-cli/get-flow-data/get-events)

###### Rate this page

😞😐😊

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
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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