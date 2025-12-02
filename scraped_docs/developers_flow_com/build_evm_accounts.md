# Source: https://developers.flow.com/build/evm/accounts

Accounts | Flow Developer Portal



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

* * Solidity (EVM)* Accounts

On this page

info

Are you a Cadence developer looking for information about Accounts on Cadence? If so, check out the Cadence specific documentation [here](/build/cadence/basics/accounts)

# Accounts

There are three types of accounts used for Flow EVM.

1. **Externally Owned Accounts (EOA)**: EOAs are controlled by private individuals using cryptographic keys and can initiate transactions directly. They are the primary account type for users to interact with the blockchain, holding and sending cryptocurrency or calling smart contract functions.
2. **Contract Accounts**: These accounts hold smart contract code and are governed by this code's logic. Unlike EOAs, Contract Accounts do not initiate transactions on their own but can execute transactions in response to calls they receive from EOAs or other contracts.
3. **Cadence Owned Accounts (COA)**: This is an account type unique to Flow EVM. These accounts are managed by [Cadence resources](https://cadence-lang.org/docs/language/resources) and can be used to interact with the Flow EVM from within the Cadence environment.

EOAs and Contract accounts function the same as on other EVM networks. Users may interact with these accounts using the standard EVM JSON-RPC API ([see endpoints here](/build/evm/using)). You can read more about EOAs and Contract accounts on the [Ethereum docs](https://ethereum.org/developers/docs/accounts).

However, in order to leverage all the features of Cadence, developers will need to utilize Cadence Owned Accounts.

danger

🚨🚨🚨 **ASSET LOSS RISK** 🚨🚨🚨

Cadence-Owned Accounts, easily identifiable by the leading zeroes (`0x00000000000000000000000`) **only exist on Flow**. The keys to these addresses are generated in a way that is not compatible with other networks.

As a result, any assets sent to one of these addresses on another network **will be lost permanently!**

We're working with major wallet providers to block such transfers, and recommend that all app and wallet developers do the same.

## Cadence Owned Accounts[​](#cadence-owned-accounts "Direct link to Cadence Owned Accounts")

A Cadence Owned Account (COA) is a natively supported EVM smart contract wallet type that allows a Cadence resource to own and control an EVM address. This native wallet type provides the primitives needed to bridge or control assets across Flow EVM and Cadence facilitating composability between environments.

![Account-Model](/assets/images/flow-evm-account-model-7567031c5e01c0dbc96a4d2f4b80f42b.png)

### Why use COAs?[​](#why-use-coas "Direct link to Why use COAs?")

COAs create powerful new opportunities to improve the UX, functionality and utility of EVM applications by taking advantage of Cadence. Key benefits include:

* **Enhanced Composability**: Applications written in Solidity can be extended and composed upon within Cadence. This allows developers to build upon existing EVM applications and deliver a more feature-rich user experience.
* **Atomic Interactions**: Developers are able to execute multiple EVM transactions atomically from a COA. This is particularly useful for applications that require multiple transactions to be executed within a single block, or require all prior transactions' state changes to revert if a single transaction in the batch fails. This is not possible natively using EOAs or with `UserOperations` when using the ERC-4337 standard; in both cases each individual transaction is distinct and cannot be reverted back once state has changed.
* **Native Account Abstraction**: COAs are controlled by Cadence resources, which are in turn owned by Flow accounts. [Flow accounts](/build/evm/accounts) have built-in support for multi-signature authentication, key rotation, and account recovery. As a Cadence resource, COAs naturally inherit [these features](/build/cadence/advanced-concepts/account-abstraction).
* **Fine-Grained Access Control**: As Cadence resources, access to a COA can be governed by more sophisticated policies than those available with basic EVM accounts. By utilizing powerful Cadence access control primitives such as [capabilities and entitlements](https://cadence-lang.org/docs/language/access-control), developers can restrict who is able to interact with a COA and what actions they are permitted to perform.

### Differences from Traditional EVM Accounts[​](#differences-from-traditional-evm-accounts "Direct link to Differences from Traditional EVM Accounts")

COAs are smart contracts that are deployed to, and are fully accessible within, Flow EVM. However, unlike traditional EVM accounts (e.g. EOAs or smart contract accounts), COAs are owned by a Cadence resource. This means that COAs can be created and controlled natively within the Cadence execution environment.

Unlike EOAs, COAs do not have an associated key, but are assigned a 20-byte EVM address upon creation from Cadence. This address is based on the UUID of the Cadence resource and is prefixed with `0x000000000000000000000002`. This address determines the location of the COA smart contract deployment and is the EVM address that is used to interact with the COA.

A COA may instantiate transactions itself (where the COA's EVM address acts as `tx.origin`). This behaviour differs from other EVM environments, where only externally owned accounts (EOAs) may instantiate transactions.

Because COAs are owned by Cadence resources, an EVM transaction is not required to trigger a transaction from a COA (e.g. a transaction to make a call to `execute` or EIP-4337's `validateUserOpMethod`). Instead, call transactions may be triggered directly from the Cadence resource that owns the COA. By invoking the `call` method on this resource, a transaction event will be emitted within the EVM environment.

### More Information[​](#more-information "Direct link to More Information")

To learn how to create and interact with COAs in Cadence, see the guide for [Interacting with COAs from Cadence](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa).

For more information about Cadence Owned Accounts, see the [Flow EVM Support FLIP](https://github.com/onflow/flips/pull/225/files)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/evm/accounts.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Fees](/build/evm/fees)[Next

Tools](/build/tools)

###### Rate this page

😞😐😊

Copy as Markdown

* [Cadence Owned Accounts](#cadence-owned-accounts)
  + [Why use COAs?](#why-use-coas)+ [Differences from Traditional EVM Accounts](#differences-from-traditional-evm-accounts)+ [More Information](#more-information)

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