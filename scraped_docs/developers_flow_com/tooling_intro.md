# Source: https://developers.flow.com/tooling/intro

Flow CLI | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                      - [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* Flow CLI

On this page

# Flow CLI

The **Flow Command Line Interface (CLI)** is a powerful tool that enables developers to seamlessly interact with the Flow blockchain across various environments, including testnet, mainnet, and local development using the Flow Emulator. Designed for ease of use, the Flow CLI simplifies common blockchain tasks such as managing accounts and contract dependencies, sending transactions, querying chain state, deploying smart contracts, and much more.

With Flow CLI, developers can:

* **Initialize Projects**: Quickly set up new Flow projects using the `flow init` command, which creates the necessary files and directories, sets up your project configuration, and installs any core contract dependencies.
* **Manage Contract Dependencies**: Use the [Dependency Manager](/build/tools/flow-cli/dependency-manager) to install and manage smart contract dependencies effortlessly, simplifying the integration of external contracts into your project.
* **Manage Accounts**: Create and manage Flow accounts, configure keys, and handle account-related operations.
* **Send Transactions**: Build, sign, and submit transactions to the Flow network, allowing for contract interaction and fund transfers.
* **Query Chain State**: Retrieve data from the Flow blockchain, including account balances, event logs, and the status of specific transactions.
* **Deploy Smart Contracts**: Easily deploy and update Cadence smart contracts on any Flow environment (emulator, testnet, or mainnet).
* **Use the Emulator:** Set up a local Flow blockchain instance with the Flow emulator to test and debug smart contracts in a development environment before deploying them on the network.
* **Test with Fork Mode**: Use [fork testing](/build/tools/flow-cli/fork-testing) to run tests and development environments against a local copy of mainnet or testnet state, giving you access to real contracts and data without affecting production.
* **Interact with the [Flow Access API](/http-api)**: Automate complex workflows using configuration files and command-line scripting, which allows for greater flexibility in continuous integration (CI) or custom development tools.
* **Access Flow’s Tooling Ecosystem**: Integrate Flow CLI with other developer tools like the [Cadence Extension for VSCode](https://marketplace.visualstudio.com/items?itemName=onflow.cadence) to enhance your development experience.

The Flow CLI is essential for developers looking to build, test, and maintain decentralized applications on the Flow blockchain efficiently, offering a feature-rich, user-friendly interface for both beginners and experienced blockchain developers.

## Installation[​](#installation "Direct link to Installation")

Follow [these steps](/build/tools/flow-cli/install) to install the Flow CLI on
macOS, Linux, and Windows.

## Create Your First Project[​](#create-your-first-project "Direct link to Create Your First Project")

Get started by running:

`_10

flow init`

The `flow init` command gets you up and running with a new project setup in one command. Choose from scaffolds for scheduled transactions, DeFi actions, stablecoins, and more, or start with a basic Cadence project.

To learn more about Flow CLI commands and how to use them, please refer to the [Commands documentation](/build/tools/flow-cli/commands).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/index.md)

Last updated on **Dec 16, 2025** by **Jordan Ribbink**

[Previous

Flow Emulator](/build/tools/emulator)[Next

Install Instructions](/build/tools/flow-cli/install)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)* [Create Your First Project](#create-your-first-project)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.