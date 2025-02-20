# Source: https://developers.flow.com/tools/flow-cli/transactions/sign-transaction




Sign a Transaction | Flow Developer Portal





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
    - [Send a Transaction](/tools/flow-cli/transactions/send-transactions)
    - [Get a Transaction](/tools/flow-cli/transactions/get-transactions)
    - [Build a Transaction](/tools/flow-cli/transactions/build-transactions)
    - [Build a Complex Transaction](/tools/flow-cli/transactions/complex-transactions)
    - [Sign a Transaction](/tools/flow-cli/transactions/sign-transaction)
    - [Send Signed Transaction](/tools/flow-cli/transactions/send-signed-transactions)
    - [Build a Complex Transaction](/tools/flow-cli/transactions/decode-transactions)
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
* Transactions
* Sign a Transaction
On this page
# Sign a Transaction

The Flow CLI provides a command to sign transactions with options to specify
authorizer accounts, payer accounts and proposer accounts.

Use this functionality in the following order:

1. Use the `build` command to build the transaction.
2. Use this command (`sign`) to sign with each account specified in the build process.
3. Use the `send-signed` command to submit the signed transaction to the Flow network.

 `_10flow transactions sign <built transaction filename>`
## Example Usage[​](#example-usage "Direct link to Example Usage")

 `_41> flow transactions sign ./built.rlp --signer alice \_41 --filter payload --save signed.rlp_41_41Hash b03b18a8d9d30ff7c9f0fdaa80fcaab242c2f36eedb687dd9b368326311fe376_41Payer f8d6e0586b0a20c7_41Authorizers [f8d6e0586b0a20c7]_41_41Proposal Key: _41 Address f8d6e0586b0a20c7_41 Index 0_41 Sequence 6_41_41No Envelope Signatures_41_41Payload Signature 0:_41 Address f8d6e0586b0a20c7_41 Signature b5b1dfed2a899037...164e1b224a7ac924018e7033b68b0df86769dd54_41 Key Index 0_41_41_41Arguments (1):_41 - Argument 0: {"type":"String","value":"Meow"}_41_41_41Code_41_41transaction(greeting: String) {_41 let guest: Address_41_41 prepare(authorizer: &Account) {_41 self.guest = authorizer.address_41 }_41_41 execute {_41 log(greeting.concat(",").concat(self.guest.toString()))_41 }_41}_41_41_41Payload:_41f90184f...a199bfd9b837a11a0885f9104b54014750f5e3e5bfe4a5795968b0df86769dd54c0`
## Arguments[​](#arguments "Direct link to Arguments")

### Built Transaction Filename or Remote Server URL[​](#built-transaction-filename-or-remote-server-url "Direct link to Built Transaction Filename or Remote Server URL")

* Name: `built transaction filename | --from-remote-url <url>`
* Valid inputs: Any filename and path valid on the system or --from-remote-url flag and fully qualified remote server url.

Specify the filename containing valid transaction payload that will be used for signing.
To be used with the `flow transaction build` command.

When --from-remote-url flag is used the value needs to be a fully qualified url to transaction RLP
Example: `flow transaction sign --from-remote-url https://fully/qualified/url --signer alice`

## Flags[​](#flags "Direct link to Flags")

### From Remote Url[​](#from-remote-url "Direct link to From Remote Url")

* Flag: `--from-remote-url`
* Valid input: `http(s)://fully/qualified/server/url`

Specify this flag with a fully qualified url to transaction RLP. The RLP will be fetched from server then signed. The resulting signed RLP is then posted to the remote url. This feature is to support protocol level multiple signature transaction coordination between multiple signers.
Note: --yes flag is not supported and will fail `sign` command when this flag is used. This forces the user to verify the cadence code.

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`, `signatures`

Specify fields to include in the result output. Applies only to the text output.

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used to sign the transaction.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be
used to execute the commands.

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
* Valid inputs: case-sensitive name of the result property.

Specify any property name from the result you want to return as the only value.

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify in which format you want to display the result.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: valid filename

Specify the filename where you want the result to be saved.

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see while command execution.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--conf`
* Short Flag: `-f`
* Valid inputs: valid filename

Specify a filename for the configuration files, you can provide multiple configuration
files by using `-f` flag multiple times.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/transactions/sign-transaction.md)Last updated on **Feb 6, 2025** by **Brian Doyle**[PreviousBuild a Complex Transaction](/tools/flow-cli/transactions/complex-transactions)[NextSend Signed Transaction](/tools/flow-cli/transactions/send-signed-transactions)
###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Built Transaction Filename or Remote Server URL](#built-transaction-filename-or-remote-server-url)
* [Flags](#flags)
  + [From Remote Url](#from-remote-url)
  + [Include Fields](#include-fields)
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

