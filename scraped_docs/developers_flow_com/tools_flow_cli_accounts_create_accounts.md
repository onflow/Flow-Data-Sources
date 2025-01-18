# Source: https://developers.flow.com/tools/flow-cli/accounts/create-accounts




Create an Account | Flow Developer Portal





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
* Create an Account
On this page
# Create an Account

The Flow CLI provides a command to submit an account creation
transaction to any Flow Access API. There are two options how to create an account, you can use the
interactive mode which guides you through the process and creates the account for you or by using
the manual process which requires a pre-existing account on the network you chose.

## Interactive Mode[​](#interactive-mode "Direct link to Interactive Mode")

Creating the account in interactive mode prompts you for an account name and network selection.
After you enter the required information the account will be created for you and saved to `flow.json`.
If account creation is done on testnet or mainnet the account key will be saved to a separate key file,
which will also be put in `.gitignore`. You can [read more about key security here](/tools/flow-cli/flow.json/security).

💡 *Please note that the account creation process can take up to a minute so please be patient.*

 `_11flow accounts create_11_11Enter an account name: mike_11✔ Testnet_11_11🎉 New account created with address 0x77e6ae4c8c2f1dd6 and name mike on Testnet network._11_11Here’s a summary of all the actions that were taken:_11 - Added the new account to flow.json._11 - Saved the private key to mike.pkey._11 - Added mike.pkey to .gitignore.`
## Manual Mode[​](#manual-mode "Direct link to Manual Mode")

Manual mode requires you to have a pre-existing account on the network which you will have to provide as a signer.
That account must be added to `flow.json` for the command to work. You also have to generate a key pair, we
suggest using the `flow keys generate` command, [which you can read more about here](/tools/flow-cli/keys/generate-keys).

 `_15# Create an account on Flow Testnet_15> flow accounts create \_15 --key a69c6986e846ba6d0....1397f5904cd319c3e01e96375d5777f1a47010 \_15 --signer my-testnet-account _15_15Address 0x01cf0e2f2f715450_15Balance 10000000_15Keys 1_15_15Key 0 Public Key a69c6986e846ba6d0....1397f5904cd319c3e01e96375d5777f1a47010_15 Weight 1000_15 Signature Algorithm ECDSA_P256_15 Hash Algorithm SHA3_256_15_15Contracts Deployed: 0`

In the above example, the `flow.json` file would look something like this:

 `_10{_10 "accounts": {_10 "my-testnet-account": {_10 "address": "a2c4941b5f3c7151",_10 "key": "12c5dfde...bb2e542f1af710bd1d40b2"_10 }_10 }_10}`
## Flags[​](#flags "Direct link to Flags")

### Public Key[​](#public-key "Direct link to Public Key")

* Flag: `--key`
* Valid inputs: a hex-encoded public key in raw form.

Specify the public key that will be added to the new account
upon creation.

### Key Weight[​](#key-weight "Direct link to Key Weight")

* Flag: `--key-weight`
* Valid inputs: number between 0 and 1000
* Default: 1000

Specify the weight of the public key being added to the new account.

When opting to use this flag, you must specify a `--key-weight` flag for each public `--key` flag provided.

### Public Key Signature Algorithm[​](#public-key-signature-algorithm "Direct link to Public Key Signature Algorithm")

* Flag: `--sig-algo`
* Valid inputs: `"ECDSA_P256", "ECDSA_secp256k1"`
* Default: `"ECDSA_P256"`

Specify the ECDSA signature algorithm for the provided public key.
This option can only be used together with the `--key` flag.

Flow supports the secp256k1 and P-256 curves.

### Public Key Hash Algorithm[​](#public-key-hash-algorithm "Direct link to Public Key Hash Algorithm")

* Flag: `--hash-algo`
* Valid inputs: `"SHA2_256", "SHA3_256"`
* Default: `"SHA3_256"`

Specify the hash algorithm that will be paired with the public key
upon account creation.

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in `flow.json`.

Specify the name of the account that will be used to sign the transaction
and pay the account creation fee.

### Contract[​](#contract "Direct link to Contract")

* Flag: `--contract`
* Valid inputs: String with format `name:filename`, where `name` is
  name of the contract as it is defined in the contract source code
  and `filename` is the filename of the contract source code.

Specify one or more contracts to be deployed during account creation.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/accounts/create-accounts.md)Last updated on **Dec 20, 2024** by **Brian Doyle**[PreviousGet an Account](/tools/flow-cli/accounts/get-accounts)[NextDeploy a Contract](/tools/flow-cli/accounts/account-add-contract)
###### Rate this page

😞😐😊

* [Interactive Mode](#interactive-mode)
* [Manual Mode](#manual-mode)
* [Flags](#flags)
  + [Public Key](#public-key)
  + [Key Weight](#key-weight)
  + [Public Key Signature Algorithm](#public-key-signature-algorithm)
  + [Public Key Hash Algorithm](#public-key-hash-algorithm)
  + [Signer](#signer)
  + [Contract](#contract)
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
* [Flowdiver Mainnet](https://flowdiver.io/)
* [Flowdiver Testnet](https://testnet.flowdiver.io/)
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

