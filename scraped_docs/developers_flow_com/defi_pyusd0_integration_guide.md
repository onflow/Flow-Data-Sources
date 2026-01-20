# Source: https://developers.flow.com/defi/pyusd0-integration-guide

PYUSD0 Integration Guide | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Defi](/defi)* [Build with Forte ↙](/defi/forte)* [DeFi Contracts Mainnet](/defi/defi-contracts-mainnet)* [DeFi Contracts Testnet](/defi/defi-contracts-testnet)* [Cross-chain swaps on Flow EVM](/defi/cross-chain-swaps)* [Add Token To MetaMask](/defi/add-token-to-metamask)* [Band Oracle](/defi/band-oracle)* [Stablecoins & Bridges FAQ](/defi/faq)* [PYUSD0 Integration](/defi/pyusd0-integration-guide)

* * PYUSD0 Integration

On this page

# PYUSD0 Integration Guide

## Overview[​](#overview "Direct link to Overview")

This guide is for developers and protocols integrating PYUSD0 on Flow EVM. PYUSD0 is an OFT (Omnichain Fungible Token) deployed via LayerZero, replacing USDF as the canonical USD stablecoin on Flow.

## Contract Addresses[​](#contract-addresses "Direct link to Contract Addresses")

### Flow EVM Mainnet[​](#flow-evm-mainnet "Direct link to Flow EVM Mainnet")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Address|  |  |  |  | | --- | --- | --- | --- | | [PYUSD0](https://evm.flowscan.io/token/0x99aF3EeA856556646C98c8B9b2548Fe815240750) `0x99af3eea856556646c98c8b9b2548fe815240750`| [Migration Pool (USDF/PYUSD0)](https://evm.flowscan.io/token/0x6ddDFa511A940cA3fD5Ec7F6a4f23947cA30f030?tab=contract) `0x6ddDFa511A940cA3fD5Ec7F6a4f23947cA30f030` | | | | | |

### Flow Cadence Mainnet[​](#flow-cadence-mainnet "Direct link to Flow Cadence Mainnet")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Token Name Contract Address Contract Name|  |  |  | | --- | --- | --- | | [PYUSD0](https://www.flowscan.io/contract/A.1e4aa0b87d10b141.EVMVMBridgedToken_99af3eea856556646c98c8b9b2548fe815240750) `0x1e4aa0b87d10b141` `EVMVMBridgedToken_99af3eea856556646c98c8b9b2548fe815240750` | | | | | |

### Testnet[​](#testnet "Direct link to Testnet")

**No official PYUSD0 testnet deployment.** For local testing, deploy the PYUSD contract directly:

* [Paxos PYUSD Contract](https://github.com/paxosglobal/paxos-token-contracts/blob/master/contracts/stablecoins/PYUSD.sol)
* This gives you a functionally equivalent token you can mint/control for testing.

### **Deprecated (USDF)**[​](#deprecated-usdf "Direct link to deprecated-usdf")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Address Status|  |  |  | | --- | --- | --- | | USDF `0x2aaBea2058b5aC2D339b163C6Ab6f2b6d53aabED` Deprecating | | | | | |

## **Token Specifications**[​](#token-specifications "Direct link to token-specifications")

`_10

Name: PYUSD0

_10

Symbol: PYUSD0

_10

Decimals: 6

_10

Standard: ERC-20 + LayerZero OFT

_10

Backing: 1:1 PYUSD (PayPal USD)`

---

## **Code Examples**[​](#code-examples "Direct link to code-examples")

Visit [the GitHub Repository](https://github.com/onflow/flow-bridge-app/tree/main/ethereum-oapp) for code examples on bridging PYUSD0 via LayerZero OFT.

## **Migration Path for Existing USDF Integrations**[​](#migration-path-for-existing-usdf-integrations "Direct link to migration-path-for-existing-usdf-integrations")

1. **Add PYUSD0 support** alongside USDF
2. **Update defaults** to use PYUSD0 instead of USDF
3. **Communicate to users** about migration timeline
4. **Deprecate USDF** after grace period

[Edit this page](https://github.com/onflow/docs/tree/main/docs/defi/pyusd0-integration-guide.md)

Last updated on **Jan 19, 2026** by **bz**

[Previous

Stablecoins & Bridges FAQ](/defi/faq)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Contract Addresses](#contract-addresses)
    + [Flow EVM Mainnet](#flow-evm-mainnet)+ [Flow Cadence Mainnet](#flow-cadence-mainnet)+ [Testnet](#testnet)+ [**Deprecated (USDF)**](#deprecated-usdf)* [**Token Specifications**](#token-specifications)* [**Code Examples**](#code-examples)* [**Migration Path for Existing USDF Integrations**](#migration-path-for-existing-usdf-integrations)

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