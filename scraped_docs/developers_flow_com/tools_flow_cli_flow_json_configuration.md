# Source: https://developers.flow.com/tools/flow-cli/flow.json/configuration

Configuration | Flow Developer Portal



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
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Flow CLI](/tools/flow-cli)
* Flow.json
* Configuration

On this page

# Configuration

Flow CLI uses a state called configuration which is stored in a file (usually `flow.json`).

Flow configuration (`flow.json`) file will contain the following properties:

* A `networks` list pre-populated with the Flow emulator, testnet and mainnet connection configuration.
* An `accounts` list pre-populated with the Flow Emulator service account.
* A `deployments` empty object where all [deployment targets](/tools/flow-cli/deployment/project-contracts#define-contract-deployment-targets) can be defined.
* A `contracts` empty object where you [define contracts](/tools/flow-cli/deployment/project-contracts#add-a-contract) you wish to deploy.

## Example Project Configuration[​](#example-project-configuration "Direct link to Example Project Configuration")

`_15

{

_15

"networks": {

_15

"emulator": "127.0.0.1:3569",

_15

"mainnet": "access.mainnet.nodes.onflow.org:9000",

_15

"testnet": "access.devnet.nodes.onflow.org:9000"

_15

},

_15

"accounts": {

_15

"emulator-account": {

_15

"address": "f8d6e0586b0a20c7",

_15

"key": "ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee",

_15

}

_15

},

_15

"deployments": {},

_15

"contracts": {}

_15

}`

## Configuration[​](#configuration "Direct link to Configuration")

Below is an example of a configuration file for a complete Flow project.
We'll walk through each property one by one.

`_55

{

_55

"contracts": {

_55

"NonFungibleToken": "./cadence/contracts/NonFungibleToken.cdc",

_55

"Kibble": "./cadence/contracts/Kibble.cdc",

_55

"KittyItems": "./cadence/contracts/KittyItems.cdc",

_55

"KittyItemsMarket": "./cadence/contracts/KittyItemsMarket.cdc",

_55

"FungibleToken": {

_55

"source": "./cadence/contracts/FungibleToken.cdc",

_55

"aliases": {

_55

"testnet": "9a0766d93b6608b7",

_55

"emulator": "ee82856bf20e2aa6"

_55

}

_55

}

_55

},

_55

_55

"deployments": {

_55

"testnet": {

_55

"admin-account": ["NonFungibleToken"],

_55

"user-account": ["Kibble", "KittyItems", "KittyItemsMarket"]

_55

},

_55

"emulator": {

_55

"emulator-account": [

_55

"NonFungibleToken",

_55

"Kibble",

_55

"KittyItems",

_55

"KittyItemsMarket"

_55

]

_55

}

_55

},

_55

_55

"accounts": {

_55

"admin-account": {

_55

"address": "3ae53cb6e3f42a79",

_55

"key": "12332967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_55

},

_55

"user-account": {

_55

"address": "e2a8b7f23e8b548f",

_55

"key": "22232967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_55

},

_55

"emulator-account": {

_55

"address": "f8d6e0586b0a20c7",

_55

"key": "2eae2f31cb5b756151fa11d82949c634b8f28796a711d7eb1e52cc301ed11111",

_55

}

_55

},

_55

_55

"networks": {

_55

"emulator": "127.0.0.1:3569",

_55

"mainnet": "access.mainnet.nodes.onflow.org:9000",

_55

"testnet": "access.devnet.nodes.onflow.org:9000",

_55

"testnetSecure": {

_55

"Host": "access-001.devnet30.nodes.onflow.org:9001",

_55

"NetworkKey": "ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d"

_55

}

_55

}

_55

}`

### Contracts[​](#contracts "Direct link to Contracts")

Contracts are specified as key-value pairs, where the key is the contract name,
and the value is the location of the Cadence source code.

The advanced format allows us to specify aliases for each network.

#### Simple Format[​](#simple-format "Direct link to Simple Format")

`_10

...

_10

_10

"contracts": {

_10

"NonFungibleToken": "./cadence/contracts/NonFungibleToken.cdc"

_10

}

_10

_10

...`

#### Advanced Format[​](#advanced-format "Direct link to Advanced Format")

Using advanced format we can define `aliases`. Aliases define an address where the contract is already deployed for that specific network.
In the example scenario below the contract `FungibleToken` would be imported from the address `9a0766d93b6608b7` when deploying to testnet network
and address `ee82856bf20e2aa6` when deploying to the Flow emulator.
We can specify aliases for each network we have defined. When deploying to testnet it is always a good idea to specify aliases for all the [common contracts](/build/core-contracts) that have already been deployed to the testnet.

⚠️ If we use an alias for the contract we should not specify it in the `deployment` section for that network.

`_10

...

_10

"FungibleToken": {

_10

"source": "./cadence/contracts/FungibleToken.cdc",

_10

"aliases": {

_10

"testnet": "9a0766d93b6608b7",

_10

"emulator": "ee82856bf20e2aa6"

_10

}

_10

}

_10

...`

Format used to specify advanced contracts is:

`_10

"CONTRACT NAME": {

_10

"source": "CONTRACT SOURCE FILE LOCATION",

_10

"aliases": {

_10

"NETWORK NAME": "ADDRESS ON SPECIFIED NETWORK WITH DEPLOYED CONTRACT"

_10

...

_10

}

_10

}`

### Accounts[​](#accounts "Direct link to Accounts")

The accounts section is used to define account properties such as keys and addresses.
Each account must include a name, which is then referenced throughout the configuration file.

#### Simple Format[​](#simple-format-1 "Direct link to Simple Format")

When using the simple format, simply specify the address for the account, and a single hex-encoded
private key.

`_10

...

_10

_10

"accounts": {

_10

"admin-account": {

_10

"address": "3ae53cb6e3f42a79",

_10

"key": "12332967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_10

}

_10

}

_10

_10

...`

#### Advanced format[​](#advanced-format-1 "Direct link to Advanced format")

The advanced format allows us to define more properties for the account.
We can define the signature algorithm and hashing algorithm, as well as custom key formats.

Please note that we can use `service` for address in case the account is used on `emulator` network as this is a special
value that is defined on the run time to the default service address on the emulator network.

**Example for advanced hex format:**

`_16

...

_16

_16

"accounts": {

_16

"admin-account": {

_16

"address": "service",

_16

"key":{

_16

"type": "hex",

_16

"index": 0,

_16

"signatureAlgorithm": "ECDSA_P256",

_16

"hashAlgorithm": "SHA3_256",

_16

"privateKey": "12332967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_16

}

_16

}

_16

}

_16

_16

...`

You can also use BIP44 to derive keys from a mnemonic. For more details please see the [FLIP](https://github.com/onflow/flips/blob/main/application/20201125-bip-44-multi-account.md)

**Example for BIP44 format:**

`_17

...

_17

_17

"accounts": {

_17

"admin-account": {

_17

"address": "service",

_17

"key":{

_17

"type": "bip44",

_17

"index": 0,

_17

"signatureAlgorithm": "ECDSA_P256",

_17

"hashAlgorithm": "SHA3_256",

_17

"mnemonic": "skull design wagon top faith actor valley crystal subject volcano access join",

_17

"derivationPath": "m/44'/539'/0'/0/0"

_17

}

_17

}

_17

}

_17

_17

...`

Note: Default value for `derivationPath` is `m/44'/539'/0'/0/0` if omitted.

You can also use a key management system (KMS) to sign the transactions. Currently, we only support Google KMS.

**Example for Google KMS format:**

`_14

...

_14

"accounts": {

_14

"admin-account": {

_14

"address": "service",

_14

"key": {

_14

"type": "google-kms",

_14

"index": 0,

_14

"signatureAlgorithm": "ECDSA_P256",

_14

"hashAlgorithm": "SHA3_256",

_14

"resourceID": "projects/flow/locations/us/keyRings/foo/bar/cryptoKeyVersions/1"

_14

}

_14

}

_14

}

_14

...`

You can store the account key to a separate file and provide the file location as part of the key configuration.

**Example for separate key file:**

`_11

...

_11

"accounts": {

_11

"admin-account": {

_11

"address": "service",

_11

"key": {

_11

"type": "file",

_11

"location": "./test.key"

_11

}

_11

}

_11

}

_11

...`

Inside the `test.key` file you should only put the hex key content (e.g. `12332967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111`)

### Deployments[​](#deployments "Direct link to Deployments")

The deployments section defines where the `project deploy` command will deploy specified contracts.
This configuration property acts as the glue that ties together accounts,
contracts and networks, all of which are referenced by name.

In the deployments section we specify the network, account name and list of contracts to be deployed to that account.

Format specifying the deployment is:

`_10

...

_10

"deployments": {

_10

"NETWORK": {

_10

"ACCOUNT NAME": ["CONTRACT NAME"]

_10

}

_10

}

_10

_10

...`

`_22

...

_22

_22

"deployments": {

_22

"emulator": {

_22

"emulator-account": [

_22

"NonFungibleToken",

_22

"Kibble",

_22

"KittyItems",

_22

"KittyItemsMarket"

_22

]

_22

},

_22

"testnet": {

_22

"admin-account": ["NonFungibleToken"],

_22

"user-account": [

_22

"Kibble",

_22

"KittyItems",

_22

"KittyItemsMarket"

_22

]

_22

}

_22

}

_22

_22

...`

### Networks[​](#networks "Direct link to Networks")

Use this section to define networks and connection parameters for that specific network.

Format for networks is:

`_10

...

_10

"networks": {

_10

"NETWORK NAME": "ADDRESS"

_10

}

_10

...`

`_10

...

_10

"networks": {

_10

"NETWORK NAME": {

_10

"host": "ADDRESS",

_10

"key": "ACCESS NODE NETWORK KEY"

_10

}

_10

}

_10

...`

`_13

...

_13

_13

"networks": {

_13

"emulator": "127.0.0.1:3569",

_13

"mainnet": "access.mainnet.nodes.onflow.org:9000",

_13

"testnet": "access.devnet.nodes.onflow.org:9000",

_13

"testnetSecure": {

_13

"host": "access-001.devnet30.nodes.onflow.org:9001",

_13

"key": "ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d"

_13

},

_13

}

_13

_13

...`

### Emulators[​](#emulators "Direct link to Emulators")

The default emulator CLI is automatically configured with name being `"default"` and values of
`serviceAccount`: `"emulator-account"` and `port`: `"3569"`. The default emulator configuration will not show up on
flow.json.

To customize emulator values, add emulator section like the example below:

`_10

...

_10

_10

"emulators": {

_10

"custom-emulator": {

_10

"port": 3600,

_10

"serviceAccount": "emulator-account"

_10

}

_10

}

_10

_10

...`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/flow.json/configuration.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Initialize Configuration](/tools/flow-cli/flow.json/initialize-configuration)[Next

Manage Configuration](/tools/flow-cli/flow.json/manage-configuration)

###### Rate this page

😞😐😊

* [Example Project Configuration](#example-project-configuration)
* [Configuration](#configuration)
  + [Contracts](#contracts)
  + [Accounts](#accounts)
  + [Deployments](#deployments)
  + [Networks](#networks)
  + [Emulators](#emulators)

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