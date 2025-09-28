# Source: https://developers.flow.com/build/tools/flow-cli/get-flow-data/get-events

Get Events | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/quickstart)

  + [Quickstart ↙](/build/cadence/quickstart)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Basics](/build/cadence/basics/network-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [EVM Wallet Setup](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
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
* Get Events

On this page

# Get Events

Use the event command to fetch a single or multiple events in a specific range of blocks.
You can provide start and end block height range, but also specify number of the latest blocks to
be used to search for specified event. Events are fetched concurrently by using multiple workers which
optionally you can also control by specifying the flags.

`_10

flow events get <event_name>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

Get the event by name `A.0b2a3299cc857e29.TopShot.Deposit` from the last 20 blocks on mainnet.

`_25

> flow events get A.0b2a3299cc857e29.TopShot.Deposit --last 20 --network mainnet

_25

_25

Events Block #12913388:

_25

Index 2

_25

Type A.0b2a3299cc857e29.TopShot.Deposit

_25

Tx ID 0a1e6cdc4eeda0e23402193d7ad5ba01a175df4c08f48fa7ac8d53e811c5357c

_25

Values

_25

id (UInt64) 3102159

_25

to ({}?) 24214cf0faa7844d

_25

_25

Index 2

_25

Type A.0b2a3299cc857e29.TopShot.Deposit

_25

Tx ID 1fa5e64dcdc8ed5dad87ba58207ee4c058feb38fa271fff659ab992dc2ec2645

_25

Values

_25

id (UInt64) 5178448

_25

to ({}?) 26c96b6c2c31e419

_25

_25

Index 9

_25

Type A.0b2a3299cc857e29.TopShot.Deposit

_25

Tx ID 262ab3996bdf98f5f15804c12b4e5d4e89c0fa9b71d57be4d7c6e8288c507c4a

_25

Values

_25

id (UInt64) 1530408

_25

to ({}?) 2da5c6d1a541971b

_25

_25

...`

Get two events `A.1654653399040a61.FlowToken.TokensDeposited`
and `A.1654653399040a61.FlowToken.TokensWithdrawn` in the block height range on mainnet.

`_34

> flow events get \

_34

A.1654653399040a61.FlowToken.TokensDeposited \

_34

A.1654653399040a61.FlowToken.TokensWithdrawn \

_34

--start 11559500 --end 11559600 --network mainnet

_34

_34

Events Block #17015045:

_34

Index 0

_34

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_34

Tx ID 6dcf60d54036acb52b2e01e69890ce34c3146849998d64364200e4b21e9ac7f1

_34

Values

_34

- amount (UFix64): 0.00100000

_34

- from (Address?): 0x9e06eebf494e2d78

_34

_34

Index 1

_34

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_34

Tx ID 6dcf60d54036acb52b2e01e69890ce34c3146849998d64364200e4b21e9ac7f1

_34

Values

_34

- amount (UFix64): 0.00100000

_34

- from (Never?): nil

_34

_34

Events Block #17015047:

_34

Index 0

_34

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_34

Tx ID 24979a3c0203f514f7f5822cc8ae7046e24f25d4a775bef697a654898fb7673e

_34

Values

_34

- amount (UFix64): 0.00100000

_34

- from (Address?): 0x18eb4ee6b3c026d2

_34

_34

Index 1

_34

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_34

Tx ID 24979a3c0203f514f7f5822cc8ae7046e24f25d4a775bef697a654898fb7673e

_34

Values

_34

- amount (UFix64): 0.00100000

_34

- from (Never?): nil`

## Arguments[​](#arguments "Direct link to Arguments")

### Event Name[​](#event-name "Direct link to Event Name")

* Name: `event_name`
* Valid Input: String

Fully-qualified identifier for the events.
You can provide multiple event names separated by a space.

## Flags[​](#flags "Direct link to Flags")

### Start[​](#start "Direct link to Start")

* Flag: `--start`
* Valid inputs: valid block height

Specify the start block height used alongside the end flag.
This will define the lower boundary of the block range.

### End[​](#end "Direct link to End")

* Flag: `--end`
* Valid inputs: valid block height

Specify the end block height used alongside the start flag.
This will define the upper boundary of the block range.

### Last[​](#last "Direct link to Last")

* Flag: `--last`
* Valid inputs: number
* Default: `10`

Specify the number of blocks relative to the last block. Ignored if the
start flag is set. Used as a default if no flags are provided.

### Batch[​](#batch "Direct link to Batch")

* Flag: `--batch`
* Valid inputs: number
* Default: `25`

Number of blocks each worker will fetch.

### Workers[​](#workers "Direct link to Workers")

* Flag: `--workers`
* Valid inputs: number
* Default: `10`

Number of workers to use when fetching events concurrently.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/get-flow-data/get-events.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Get Block](/build/tools/flow-cli/get-flow-data/get-blocks)[Next

Get Collection](/build/tools/flow-cli/get-flow-data/get-collections)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Event Name](#event-name)
* [Flags](#flags)
  + [Start](#start)
  + [End](#end)
  + [Last](#last)
  + [Batch](#batch)
  + [Workers](#workers)
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

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
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