# Source: https://developers.flow.com/tools/flow-cli/flow.json/security

Security | Flow Developer Portal



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

    - [Initialize Configuration](/tools/flow-cli/flow.json/initialize-configuration)
    - [Configuration](/tools/flow-cli/flow.json/configuration)
    - [Manage Configuration](/tools/flow-cli/flow.json/manage-configuration)
    - [Security](/tools/flow-cli/flow.json/security)
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
* Flow.json
* Security

On this page

# Security

The managing of accounts and private keys is intrinsically dangerous.
We must take extra precautions to not expose private key data when using
the CLI.

The Flow CLI provides several options to secure private account data.

⚠️ Warning: please be careful when using private keys in configuration files.
Never commit private key data to source control.
If private key data must be kept in text, we suggest using a separate file
that is not checked into source control (e.g. excluded with `.gitignore`).

### Private Account Configuration File[​](#private-account-configuration-file "Direct link to Private Account Configuration File")

Storing an account key to a separate file which is not checked into source control (e.g. excluded with `.gitignore`)
can be the first step towards better security.

#### Main configuration file[​](#main-configuration-file "Direct link to Main configuration file")

`_11

...

_11

"accounts": {

_11

"my-testnet-account": {

_11

"address": "3ae53cb6e3f42a79",

_11

"key": {

_11

"type": "file",

_11

"location": "./my-testnet-account.key"

_11

}

_11

}

_11

}

_11

...`

#### Separate account key file[​](#separate-account-key-file "Direct link to Separate account key file")

⚠️ Put this file in `.gitignore`

The `my-testnet-account.key` file only contains the hex-encoded private key.

`_10

334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111`

---

#### Private configuration file[​](#private-configuration-file "Direct link to Private configuration file")

⚠️ Put this file in `.gitignore`:

`_10

// flow.testnet.json

_10

{

_10

"accounts": {

_10

"my-testnet-account": {

_10

"address": "3ae53cb6e3f42a79",

_10

"key": "334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_10

}

_10

}

_10

}`

### Store Configuration in Environment Variables[​](#store-configuration-in-environment-variables "Direct link to Store Configuration in Environment Variables")

You can use environment variables for values that should be kept private (e.g. private keys, addresses).

See example below:

`_10

PRIVATE_KEY=key flow project deploy`

`_11

// flow.json

_11

{

_11

...

_11

"accounts": {

_11

"my-testnet-account": {

_11

"address": "3ae53cb6e3f42a79",

_11

"key": "$PRIVATE_KEY"

_11

}

_11

}

_11

...

_11

}`

### Private Dotenv File[​](#private-dotenv-file "Direct link to Private Dotenv File")

The CLI will load environment variables defined in the `.env` file in the active directory, if one exists.
These variables can be substituted inside the `flow.json`,
just like any other environment variable.

⚠️ You should never commit `.env` to source control,
especially if it contains sensitive information
like a private key.

Example `.env` file:

`_10

PRIVATE_KEY=123`

### Composing Multiple Configuration Files[​](#composing-multiple-configuration-files "Direct link to Composing Multiple Configuration Files")

You can merge multiple configuration files like so:

`_10

flow project deploy -f main.json -f private.json`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/flow.json/security.md)

Last updated on **Feb 19, 2025** by **Brian Doyle**

[Previous

Manage Configuration](/tools/flow-cli/flow.json/manage-configuration)[Next

Get Block](/tools/flow-cli/get-flow-data/get-blocks)

###### Rate this page

😞😐😊

* [Private Account Configuration File](#private-account-configuration-file)
* [Store Configuration in Environment Variables](#store-configuration-in-environment-variables)
* [Private Dotenv File](#private-dotenv-file)
* [Composing Multiple Configuration Files](#composing-multiple-configuration-files)

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