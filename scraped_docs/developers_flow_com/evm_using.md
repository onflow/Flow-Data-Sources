# Source: https://developers.flow.com/evm/using




Using Flow EVM | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Networks](/evm/networks)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Data Indexers](/evm/data-indexers)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)
* [Clients](/evm/clients/ethers)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)


* Using Flow EVM
On this page
# Using Flow

## EVM Wallets[​](#evm-wallets "Direct link to EVM Wallets")

Applications deployed to Flow EVM will work with popular EVM-compatible wallets such as [MetaMask](https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn), all you need to do is add the correct [RPC endpoint](/evm/networks) as a custom network.

### [MetaMask](https://metamask.io)[​](#metamask "Direct link to metamask")

Manual method: Add Flow EVM as a custom network to MetaMask:

1. Open the MetaMask browser extension
2. Open the network selection dropdown menu by clicking the dropdown button at the top of the extension
3. Click the **`Add network`** button
4. Click **`Add a network manually`**
5. In the **`Add a network manually`** dialog that appears, enter the following information:

| Name | Value |
| --- | --- |
| Network Name | Flow EVM |
| Description | The public RPC url for Flow Mainnet |
| RPC Endpoint | <https://mainnet.evm.nodes.onflow.org> |
| Chain ID | 747 |
| Currency Symbol | FLOW |
| Block Explorer | <https://evm.flowscan.io/> |

6. Tap the Save button to save Flow EVM as a network.

You should now be able to connect to the Flow EVM by selecting it from the network selection dropdown menu.

To additionally add the Flow EVM Testnet to MetaMask, follow the same steps as above, but use the following information:

| Name | Value |
| --- | --- |
| Network Name | Flow EVM Testnet |
| Description | The public RPC url for Flow Testnet |
| RPC Endpoint | <https://testnet.evm.nodes.onflow.org> |
| Chain ID | 545 |
| Currency Symbol | FLOW |
| Block Explorer | <https://evm-testnet.flowscan.io> |

Use the [Flow Testnet Faucet](https://faucet.flow.com/fund-account) to fund your account for testing.

## Flow Native Wallets[​](#flow-native-wallets "Direct link to Flow Native Wallets")

### [Flow Wallet](https://wallet.flow.com)[​](#flow-wallet "Direct link to flow-wallet")

Flow Wallet is available on [Android](https://play.google.com/store/apps/details?id=io.outblock.lilico&hl=en_US&gl=US) and [iOS](https://apps.apple.com/ca/app/flow-core/id1644169603), with desktop support using the Flow Wallet [Chrome extension](https://chromewebstore.google.com/detail/flow-reference-wallet/hpclkefagolihohboafpheddmmgdffjm). In addition to being able to transact in both EVM and Cadence environments, Flow Wallet will also allow you to view and move assets between EVM and Cadence, making it possible to manage all your assets in one place.

To use the Flow Wallet Chrome extension:

1. Open the Flow Wallet browser extension and create your account.
2. Connect to an app using Flow Wallet.

## EVM Specification[​](#evm-specification "Direct link to EVM Specification")

* Flow EVM is a virtual EVM-based blockchain using the latest EVM byte-code interpreter `Geth v1.13`
* Utilizes `FLOW` token for transactions, with balances denominated in `Atto-FLOW` (1 `FLOW` = 10^18 `Atto-FLOW`)
* The [EVM Gateway](https://github.com/onflow/flow-evm-gateway) exposes the standard EVM API (Ethereum JSON-RPC)
* Read more about the implementation in [FLIP 223: EVM integration interface](https://github.com/onflow/flips/blob/main/protocol/20231116-evm-support.md)

## JSON-RPC Methods[​](#json-rpc-methods "Direct link to JSON-RPC Methods")

| Method | Status | Notes |
| --- | --- | --- |
| [web3\_clientVersion](https://ethereum.org/en/developers/docs/apis/json-rpc/#web3_clientversion) | ✅ |  |
| [web3\_sha3](https://ethereum.org/en/developers/docs/apis/json-rpc/#web3_sha3) | ✅ |  |
| [net\_listening](https://ethereum.org/en/developers/docs/apis/json-rpc/#net_listening) | ✅ |  |
| [net\_peerCount](https://ethereum.org/en/developers/docs/apis/json-rpc/#net_peercount) | ✅ |  |
| [net\_version](https://ethereum.org/en/developers/docs/apis/json-rpc/#net_version) | ✅ |  |
| [eth\_accounts](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_accounts) | 🚧 | Unsupported |
| [eth\_blockNumber](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_blocknumber) | ✅ |  |
| [eth\_call](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_call) | ✅ |  |
| [eth\_chainId](https://eips.ethereum.org/EIPS/eip-695) | ✅ |  |
| [eth\_coinbase](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_coinbase) | ✅ |  |
| [eth\_estimateGas](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_estimategas) | ✅ |  |
| [eth\_gasPrice](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gasprice) | ✅ |  |
| [eth\_getBalance](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getbalance) | ✅ |  |
| [eth\_getBlockByHash](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblockbyhash) | ✅ |  |
| [eth\_getBlockByNumber](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblockbynumber) | ✅ |  |
| [eth\_getBlockTransactionCountByHash](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblocktransactioncountbyhash) | ✅ |  |
| [eth\_getBlockTransactionCountByNumber](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblocktransactioncountbynumber) | ✅ |  |
| [eth\_getBlockReceipts] | ✅ |  |
| [eth\_getCode](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getcode) | ✅ |  |
| [eth\_getFilterChanges](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getfilterchanges) | ✅ |  |
| [eth\_getFilterLogs](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getfilterlogs) | ✅ |  |
| [eth\_getLogs](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getlogs) | ✅ |  |
| [eth\_getProof](https://eips.ethereum.org/EIPS/eip-1186) | 🚧 | Unsupported |
| [eth\_getStorageAt](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getstorageat) | ✅ |  |
| [eth\_getTransactionByBlockHashAndIndex](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionbyblockhashandindex) | ✅ |  |
| [eth\_getTransactionByBlockNumberAndIndex](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionbyblocknumberandindex) | ✅ |  |
| [eth\_getTransactionByHash](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionbyhash) | ✅ |  |
| [eth\_getTransactionCount](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactioncount) | ✅ |  |
| [eth\_getTransactionReceipt](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionreceipt) | ✅ |  |
| [eth\_getUncleByBlockHashAndIndex](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclebyblockhashandindex) | ✅ |  |
| [eth\_getUncleByBlockNumberAndIndex](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclebyblocknumberandindex) | ✅ |  |
| [eth\_getUncleCountByBlockHash](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclecountbyblockhash) | ✅ |  |
| [eth\_getUncleCountByBlockNumber](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclecountbyblocknumber) | ✅ |  |
| [eth\_newBlockFilter](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_newblockfilter) | ✅ |  |
| [eth\_newFilter](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_newfilter) | ✅ |  |
| [eth\_newPendingTransactionFilter](https://openethereum.github.io/JSONRPC-eth-module.html#eth_newpendingtransactionfilter) | ✅ |  |
| [eth\_sendRawTransaction](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_sendrawtransaction) | ✅ |  |
| [eth\_sendTransaction](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_sendtransaction) | 🚧 | Unsupported |
| [eth\_sign](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_sign) | 🚧 | Unsupported |
| [eth\_signTransaction](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_signtransaction) | 🚧 | Unsupported |
| [eth\_syncing](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_syncing) | ✅ |  |
| [eth\_uninstallFilter](https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_uninstallfilter) | ✅ |  |
| [eth\_maxPriorityFeePerGas] | ✅ |  |
| [eth\_feeHistory] | ✅ |  |
| [debug\_traceTransaction] | ✅ |  |
| [debug\_traceBlockByNumber] | ✅ |  |
| [debug\_traceBlockByHash] | ✅ |  |
| [debug\_traceCall] | ✅ |  |

**Legend**: ❌ = not supported. 🚧 = work in progress. ✅ = supported.

Read more about the [EVM Gateway](https://github.com/onflow/flow-evm-gateway) on Flow and how it implements the Ethereum JSON-RPC API.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/using.mdx)Last updated on **Feb 18, 2025** by **Brian Doyle**[PreviousHow it Works](/evm/how-it-works)[NextNetworks](/evm/networks)
###### Rate this page

😞😐😊

* [EVM Wallets](#evm-wallets)
  + [MetaMask](#metamask)
* [Flow Native Wallets](#flow-native-wallets)
  + [Flow Wallet](#flow-wallet)
* [EVM Specification](#evm-specification)
* [JSON-RPC Methods](#json-rpc-methods)
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

