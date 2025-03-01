# Source: https://developers.flow.com/tools/flow-cli/get-flow-data/get-events

Get Events | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

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
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/get-flow-data/get-events.md)

Last updated on **Feb 22, 2025** by **bz**

[Previous

Get Block](/tools/flow-cli/get-flow-data/get-blocks)[Next

Get Collection](/tools/flow-cli/get-flow-data/get-collections)

###### Rate this page

😞😐😊

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