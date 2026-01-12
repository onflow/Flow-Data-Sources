# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup

Cadence Environment Setup | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            - [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)- [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)- [Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)- [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)+ [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)+ [Emulator Fork Testing](/blockchain-development-tutorials/cadence/emulator-fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)* Cadence Environment Setup

On this page

# Cadence Environment Setup

This comprehensive tutorial will guide you through how to set up your complete development environment, deploy your first smart contract, and learn the fundamentals of Flow development. You'll work hands-on with the Flow CLI, local emulator, and a real smart contract to build practical skills from day one.

Flow is a blockchain built for the next generation of apps, games, and digital assets. With its unique multi-role architecture and resource-oriented programming language Cadence, Flow allows developers to create secure, composable, and scalable applications. This tutorial focuses on getting you productive with Flow's developer tools as quickly as possible.

## What you'll learn[​](#what-youll-learn "Direct link to What you'll learn")

After you complete this tutorial, you'll be able to:

* **Set up a complete Flow development environment** with CLI tools and VSCode integration.
* **Create and manage Flow projects** with the Flow CLI and understand project structure.
* **Deploy and interact with smart contracts** on the local Flow emulator.
* **Execute scripts and transactions** to read from and modify blockchain state.
* **Understand Flow's account model** and how contracts are deployed to account storage.
* **Navigate the Flow ecosystem** and know where to find help and resources.

## What you'll build[​](#what-youll-build "Direct link to What you'll build")

You'll work with a `Counter` contract, a simple but comprehensive example that demonstrates core Flow development patterns. This contract maintains a count value and provides functions to increment, decrement, and read the current count. By the end of this tutorial, you'll have:

* A fully functional local Flow development environment.
* A deployed Counter contract that runs on your local emulator.
* Scripts to query the contract's state.
* Transactions to modify the contract's state.
* Knowledge of how to extend this foundation for more complex applications.

**Time Commitment:** Approximately 30-45 minutes

**Prerequisites:**

* Basic command line familiarity
* Code editor (VSCode recommended)
* `Node.js` installed (for future frontend development)

---

### Install Flow CLI[​](#install-flow-cli "Direct link to Install Flow CLI")

The [Flow Command Line Interface](/build/tools/flow-cli) (CLI) is a set of tools that developers can use to interact with the Flow blockchain. Developers can manage accounts, send transactions, deploy smart contracts, run the emulator, and more. This quickstart will get you familiar with its main concepts and functionality.

The first thing you'll need to do is install the Flow CLI. If you have [homebrew](https://brew.sh/) installed, run:

`_10

brew install flow-cli`

**For other operating systems,** refer to the [installation guide](/build/tools/flow-cli/install) for detailed instructions.

**Verify Installation:**

`_10

flow version`

You will see output showing your Flow CLI version.

### Install VSCode extension[​](#install-vscode-extension "Direct link to Install VSCode extension")

Install the [Flow Cadence VSCode Extension](https://marketplace.visualstudio.com/items?itemName=onflow.cadence) from the marketplace. This extension provides:

* Syntax highlighting for Cadence.
* Code completion and IntelliSense.
* Error checking and diagnostics.
* Integrated development tools.

## Create your first project[​](#create-your-first-project "Direct link to Create your first project")

Navigate to your desired development directory and create a new Flow project:

`_10

flow init`

When prompted:

1. **Project name:** Enter your preferred project name.
2. Select `Basic Cadence project (no dependencies)`.

The `flow init` command creates:

* **`flow.json`**: Central configuration file that contains accounts, contracts, deployments, and network settings.
* **`emulator-account.pkey`**: Private key for the default emulator account.
* **`cadence/`**: Directory structure for your Cadence code:
  + `contracts/`: Smart contract files
  + `scripts/`: Read-only blockchain queries
  + `transactions/`: State-changing operations
  + `tests/`: Contract test files

Navigate into your project directory:

`_10

cd your-flow-project-name`

info

For additional details on how `flow.json` is configured, review the [configuration docs](/build/tools/flow-cli/flow.json/configuration).

### Start the Flow emulator[​](#start-the-flow-emulator "Direct link to Start the Flow emulator")

The emulator is a local version of the Flow blockchain that you can use to test your contracts and scripts. It's a great way to develop and test your contracts locally - before you try them on the `testnet` or `mainnet`.

Before we deploy, let's open a new terminal window and run the emulator. From the root of your project directory, where your `emulator-account.pkey` and `flow.json` files are located, run:

`_10

flow emulator start`

Keep this terminal running. The emulator provides:

* Local blockchain environment.
* Fast transaction processing.
* No real-world costs.
* Complete Flow feature set.

## Your first contract[​](#your-first-contract "Direct link to Your first contract")

Now let's examine, deploy, and interact with the Counter contract that was created in your project.

### Examine the Counter contract[​](#examine-the-counter-contract "Direct link to Examine the Counter contract")

Open `cadence/contracts/Counter.cdc` in your editor. Let's break down this contract:

`_31

access(all) contract Counter {

_31

_31

access(all) var count: Int

_31

_31

// Event to be emitted when the counter is incremented

_31

access(all) event CounterIncremented(newCount: Int)

_31

_31

// Event to be emitted when the counter is decremented

_31

access(all) event CounterDecremented(newCount: Int)

_31

_31

init() {

_31

self.count = 0

_31

}

_31

_31

// Public function to increment the counter

_31

access(all) fun increment() {

_31

self.count = self.count + 1

_31

emit CounterIncremented(newCount: self.count)

_31

}

_31

_31

// Public function to decrement the counter

_31

access(all) fun decrement() {

_31

self.count = self.count - 1

_31

emit CounterDecremented(newCount: self.count)

_31

}

_31

_31

// Public function to get the current count

_31

view access(all) fun getCount(): Int {

_31

return self.count

_31

}

_31

}`

**Key components:**

* **Contract Declaration**: `access(all) contract Counter` creates a public contract named Counter.
* **State Variable**: `access(all) var count: Int` stores the counter value, accessible to everyone.
* **Events**: `CounterIncremented` and `CounterDecremented` notify listeners when changes occur.
* **Initializer**: `init()` sets the initial count to 0 when the contract is deployed.
* **Public Functions**:
  + `increment()`: Increases count by 1 and emits an event
  + `decrement()`: Decreases count by 1 and emits an event
  + `getCount()`: Returns the current count (read-only, marked with `view`)

### Create and configure deployment account[​](#create-and-configure-deployment-account "Direct link to Create and configure deployment account")

When you create a project, you'll see that a `Counter` contract was added to your [`flow.json`](/build/tools/flow-cli/flow.json/configuration) configuration file, but it's not set up for deployment yet. We could deploy it to the automatically created `emulator-account`, but for this example, lets also create a new account on the emulator to deploy it to.

info

**Reminder**: On Flow Cadence, contracts are deployed to the storage of the account that deploys them.

Leave your emulator running, and open a second terminal. Run the following command:

`_10

flow accounts create`

When prompted:

1. **Account name:** Enter `test-account`
2. **Network:** Select `Emulator`

This adds the new account to your `flow.json` configuration file.

After you've created you accounts, then you can view all your accounts on the with the Flow CLI with:

`_24

📋 Account Status Across Networks

_24

_24

This shows which networks your configured accounts are accessible on:

_24

🌐 Network 🟢 Local (running) 🔴 Local (stopped) ✓ Found ✗ Error

_24

─────────────────────────────────────────────────────

_24

_24

🟢 emulator

_24

✓ default (f3fcd2c1a78f5eee): 0.00100000 FLOW

_24

✓ emulator-account (f8d6e0586b0a20c7): 999999999.99300000 FLOW

_24

✓ test-account (e03daebed8ca0615): 0.00100000 FLOW

_24

_24

🌐 mainnet

_24

No accounts found

_24

_24

🌐 testnet

_24

No accounts found

_24

_24

🟢 testing

_24

✓ default (f3fcd2c1a78f5eee): 0.00100000 FLOW

_24

✓ emulator-account (f8d6e0586b0a20c7): 999999999.99300000 FLOW

_24

✓ test-account (e03daebed8ca0615): 0.00100000 FLOW

_24

_24

_24

💡 Tip: To fund testnet accounts, run: flow accounts fund`

This is a great tool to visualize your different accounts and balances while you develop..

### Configure contract deployment[​](#configure-contract-deployment "Direct link to Configure contract deployment")

To deploy the `Counter` contract to the emulator, you'll need to add it to your project configuration. To do this, run:

`_10

flow config add deployment`

Follow the prompts:

1. **Network:** Select `emulator`
2. **Account:** Select `test-account`
3. **Contract:** Select `Counter`
4. **Deploy more contracts:** Select `no`

This configures your `flow.json` to deploy the Counter contract to your test account on the emulator.

### Deploy the contract[​](#deploy-the-contract "Direct link to Deploy the contract")

To deploy the `Counter` contract to the emulator, run:

`_10

flow project deploy`

You'll see output similar to:

`_10

Deploying 1 contracts for accounts: test-account

_10

_10

Counter -> 0x179b6b1cb6755e31 (a98c155fe7afc8eb2af5551748759b08a80a0ae85d1b09f92f1afc293c61ca98)

_10

_10

🎉 All contracts deployed successfully`

That's it! You've just deployed your first contract to the Flow Emulator.

### Verify deployment with a script[​](#verify-deployment-with-a-script "Direct link to Verify deployment with a script")

Scripts are used to read data from the Flow blockchain. There is no state modification. Let's verify the deployment by reading the counter value. Run the included script:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc`

You should see:

`_10

Result: 0`

This confirms your contract is deployed and functional. The counter starts at zero (0), as defined in the contract's `init()` function.

If we wanted to generate a new script, we could run:

`_10

flow generate script ScriptName`

info

For more information about generating Cadence files, see the [Generating Cadence Boilerplate](https://developers.flow.com/build/tools/flow-cli/generate) documentation.

**You'll usually want to use these commands instead of adding files manually!**

tip

To learn more about writing scripts, check out the docs for [basic scripts](https://developers.flow.com/build/cadence/basics/scripts).

### Execute transactions[​](#execute-transactions "Direct link to Execute transactions")

Now let's increment the counter with a transaction:

`_10

flow transactions send cadence/transactions/IncrementCounter.cdc`

By default, this uses the `emulator-account` to sign the transaction and the emulator network. If you want to use your `test-account` account, you can specify the `--signer` flag with the account name. The command would look like this:

`_10

flow transactions send cadence/transactions/IncrementCounter.cdc --signer test-account`

The transaction output shows detailed information including:

* Transaction ID and block information.
* Status confirmation (`✅ SEALED`).
* Events emitted (including `CounterIncremented`).

`_33

Transaction ID: 9cc7ac4d3d5239016965aba89b9692d3401a48a090d1ad1a8d9ef9cfca685e6e

_33

_33

Block ID b8537860b0fc9ca8b3195b121e762502f9a220874b605d6a810998e8b62321a3

_33

Block Height 3

_33

Status ✅ SEALED

_33

ID 9cc7ac4d3d5239016965aba89b9692d3401a48a090d1ad1a8d9ef9cfca685e6e

_33

Payer f8d6e0586b0a20c7

_33

Authorizers [f8d6e0586b0a20c7]

_33

_33

Proposal Key:

_33

Address f8d6e0586b0a20c7

_33

Index 0

_33

Sequence 1

_33

_33

No Payload Signatures

_33

_33

Envelope Signature 0: f8d6e0586b0a20c7

_33

Signatures (minimized, use --include signatures)

_33

_33

Events:

_33

Index 0

_33

Type A.179b6b1cb6755e31.Counter.CounterIncremented

_33

Tx ID 9cc7ac4d3d5239016965aba89b9692d3401a48a090d1ad1a8d9ef9cfca685e6e

_33

Values

_33

- newCount (Int): 1

_33

_33

_33

_33

Code (hidden, use --include code)

_33

_33

Payload (hidden, use --include payload)

_33

_33

Fee Events (hidden, use --include fee-events)`

Run the script to check the counter again. You'll see that it has incremented:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc`

`_10

Result: 1`

tip

To learn more about writing transactions, read the docs for [basic transactions](https://developers.flow.com/build/cadence/basics/transactions).

## Conclusion[​](#conclusion "Direct link to Conclusion")

You've successfully established a solid foundation for building on Flow. Let's recap what you've accomplished and learned. Through this hands-on tutorial, you've successfully built a complete Flow development foundation:

✅ **Complete Flow development environment**

* Flow CLI installed and configured for project management.
* Local Flow emulator running and ready for development.
* Project creation and management workflow with `flow init`.

✅ **Smart contract deployment skills**

* Counter contract successfully deployed to your local emulator.
* Account creation and contract deployment configuration mastered.

✅ **Blockchain interactions**

* Scripts to query contract state (read blockchain data).
* Transactions to modify contract state (write to blockchain).
* Real-time interaction with blockchain data through CLI commands.

### Resources for continued learning[​](#resources-for-continued-learning "Direct link to Resources for continued learning")

As you continue your Flow development journey:

* **[Flow Discord Community](https://discord.com/invite/flow)**: Connect with other developers, get help, and share your projects.
* **[Cadence Language Reference](https://cadence-lang.org)**: Deep dive into Flow's programming language features and best practices.
* **[Flow GitHub](https://github.com/onflow)**: Explore open source tools, examples, and contribute to the ecosystem.

The foundation you've built today will serve you well as you explore Flow's capabilities and build applications that take advantage of blockchain's unique properties: permanence, transparency, and decentralization.

Welcome to the Flow developer community—you're ready to build the future of digital experiences!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)[Next

Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)

###### Rate this page

😞😐😊

Copy as Markdown

* [What you'll learn](#what-youll-learn)* [What you'll build](#what-youll-build)
    + [Install Flow CLI](#install-flow-cli)+ [Install VSCode extension](#install-vscode-extension)* [Create your first project](#create-your-first-project)
      + [Start the Flow emulator](#start-the-flow-emulator)* [Your first contract](#your-first-contract)
        + [Examine the Counter contract](#examine-the-counter-contract)+ [Create and configure deployment account](#create-and-configure-deployment-account)+ [Configure contract deployment](#configure-contract-deployment)+ [Deploy the contract](#deploy-the-contract)+ [Verify deployment with a script](#verify-deployment-with-a-script)+ [Execute transactions](#execute-transactions)* [Conclusion](#conclusion)
          + [Resources for continued learning](#resources-for-continued-learning)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.