# Source: https://developers.flow.com/tools/flow-cli/super-commands

Super Commands | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)
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
* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
* Super Commands

On this page

# Super Commands

Flow CLI Super commands are set of commands that can be used during development of your dApp to greatly simplify the workflow. The result is you can focus on writing the contracts and the commands will take care of the rest.

## Init[​](#init "Direct link to Init")

The initial command to start your new Flow project is flow init. It will ask you a few questions about how you'd like to configure your project and then create the necessary files and folders, set up the configuration file, and install any core contract dependencies you might need.

During the initialization process, `flow init` will prompt you if you want to install any core smart contracts (e.g. `NonFungibleToken`) and set them up in your project. If you choose to install core contracts, the CLI will use the [Dependency Manager](/tools/flow-cli/dependency-manager) under the hood to automatically install any required smart contract dependencies.

> Note: If you just want the `flow.json` configured without creating any folders or files, you can run `flow init --config-only`.

Running the command:

`_10

> flow init $PROJECT_NAME`

Will create the following folders and files:

* `/contracts` folder should contain all your Cadence contracts,
* `/scripts` folder should contain all your Cadence scripts,
* `/transactions` folder should contain all your Cadence transactions,
* `/tests` folder should contain all your Cadence tests,
* `flow.json` is a configuration file for your project, which will be automatically maintained.

### Using Scaffolds[​](#using-scaffolds "Direct link to Using Scaffolds")

Based on the purpose of your project you can select from a list of available scaffolds.
You can access the scaffolds by simply using the `--scaffold` flag like so:

`_10

> flow init $PROJECT_NAME --scaffold`

If you'd like to skip the interactive mode of selecting a scaffold, use the `--scaffold-id` flag with a known ID:

`_10

> flow init $PROJECT_NAME --scaffold-id=1`

The list of scaffolds will continuously grow, and you are welcome to contribute to that.
You can contribute by creating your own scaffold repository which can then be added to the scaffold
list by [following instructions here](https://github.com/onflow/flow-cli/blob/master/CONTRIBUTING.md#adding-a-scaffold).

## Testing[​](#testing "Direct link to Testing")

`flow init` will also have created an example test file in the `/tests` folder. You can run the tests by using the `flow test` command.

## Import Schema[​](#import-schema "Direct link to Import Schema")

You can simply import your contracts by name. We have introducted a new way to import your contracts. This will simply your workflow.

The new import schema format looks like:

`_10

import "{name of the contract}"`

Example:

`_10

import "HelloWorld"`

This will automatically import the contract you have created in your project with the same name and
save the configuration in flow.json. It doesn't matter if the contract has been deployed on a non-default account.

## Learn More[​](#learn-more "Direct link to Learn More")

To learn more about next steps following the initial setup, check out the following links:

* [Depedency Manager](/tools/flow-cli/dependency-manager): Lets you install and manage your contract dependencies with CLI commands.
* [Manage Configuration](/tools/flow-cli/flow.json/manage-configuration): Learn how to manage your project configuration file.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/super-commands.md)

Last updated on **Apr 3, 2025** by **Brian Doyle**

[Previous

Install Instructions](/tools/flow-cli/install)[Next

Get an Account](/tools/flow-cli/accounts/get-accounts)

###### Rate this page

😞😐😊

* [Init](#init)
  + [Using Scaffolds](#using-scaffolds)
* [Testing](#testing)
* [Import Schema](#import-schema)
* [Learn More](#learn-more)

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