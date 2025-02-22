# Source: https://developers.flow.com/ecosystem/defi-liquidity/defi-contracts




DeFi Contracts on Flow | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Ecosystem](/ecosystem)
* [Wallets](/ecosystem/wallets)
* [Flow Block Explorers](/ecosystem/block-explorers)
* [Developer Profile](/ecosystem/developer-profile)
* [DeFi & Liquidity](/ecosystem/defi-liquidity)
  + [DeFi Contracts](/ecosystem/defi-liquidity/defi-contracts)
  + [Stablecoins & Bridges FAQ](/ecosystem/defi-liquidity/faq)
* [Bridges](/ecosystem/bridges)
* [Community Projects](/ecosystem/projects)
* [VCs & Funds](/ecosystem/vcs-and-funds)
* [Faucets](/ecosystem/faucets)
* [Grants](/ecosystem/grants)
* [Hackathons](/ecosystem/hackathons)
* [Auditors](/ecosystem/auditors)
* [Ecosystem Overview](/ecosystem/overview)


* [DeFi & Liquidity](/ecosystem/defi-liquidity)
* DeFi Contracts
On this page
# DeFi Contracts on Flow

Flow is a Layer 1 blockchain that supports EVM equivalency, offering two environments Flow EVM and Flow Cadence. Fungible and non-fungible tokens can seamlessly transfer between these environments via the native VM token bridge. As a result, many tokens have both a Flow EVM mainnet contract address and a Flow Cadence mainnet contract address, allowing developers to choose their preferred environment.

Below is a list of commonly used DeFi contracts on Flow:

## Stablecoins & Wrapped Assets[​](#stablecoins--wrapped-assets "Direct link to Stablecoins & Wrapped Assets")

#### Flow EVM Mainnet[​](#flow-evm-mainnet "Direct link to Flow EVM Mainnet")

| Token Name | Flow EVM Mainnet Address |
| --- | --- |
| [WFLOW](https://evm.flowscan.io/token/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e) | `0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e` |
| [USDC (stgUSDC)](https://evm.flowscan.io/token/0xF1815bd50389c46847f0Bda824eC8da914045D14) | `0xF1815bd50389c46847f0Bda824eC8da914045D14` |
| [USDT (stgUSDT)](https://evm.flowscan.io/token/0x674843C06FF83502ddb4D37c2E09C01cdA38cbc8) | `0x674843C06FF83502ddb4D37c2E09C01cdA38cbc8` |
| [USDF (USD Flow)](https://evm.flowscan.io/token/0x2aaBea2058b5aC2D339b163C6Ab6f2b6d53aabED) | `0x2aaBea2058b5aC2D339b163C6Ab6f2b6d53aabED` |
| [USDC.e (Celer)](https://evm.flowscan.io/token/0x7f27352D5F83Db87a5A3E00f4B07Cc2138D8ee52) | `0x7f27352D5F83Db87a5A3E00f4B07Cc2138D8ee52` |
| [stFlow (Increment Staked FLOW)](https://evm.flowscan.io/token/0x5598c0652B899EB40f169Dd5949BdBE0BF36ffDe) | `0x5598c0652B899EB40f169Dd5949BdBE0BF36ffDe` |
| [ankrFLOWEVM (Ankr Staked FLOW)](https://evm.flowscan.io/token/0x1b97100eA1D7126C4d60027e231EA4CB25314bdb) | `0x1b97100eA1D7126C4d60027e231EA4CB25314bdb` |
| [WETH](https://evm.flowscan.io/token/0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590) | `0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590` |
| [cbBTC](https://evm.flowscan.io/token/0xA0197b2044D28b08Be34d98b23c9312158Ea9A18) | `0xA0197b2044D28b08Be34d98b23c9312158Ea9A18` |

#### Flow Cadence Mainnet[​](#flow-cadence-mainnet "Direct link to Flow Cadence Mainnet")

| Token Name | Flow Cadence Mainnet Address |
| --- | --- |
| [FLOW](https://www.flowscan.io/ft/token/A.1654653399040a61.FlowToken.Vault) | `0x1654653399040a61` |
| [USDC (stgUSDC)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_f1815bd50389c46847f0bda824ec8da914045d14.Vault) | `EVMVMBridgedToken_f1815bd50389c46847f0bda824ec8da914045d14` |
| [USDT (stgUSDT)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_674843c06ff83502ddb4d37c2e09c01cda38cbc8.Vault) | `EVMVMBridgedToken_674843c06ff83502ddb4d37c2e09c01cda38cbc8` |
| [USDF (USD Flow)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_2aabea2058b5ac2d339b163c6ab6f2b6d53aabed.Vault) | `EVMVMBridgedToken_2aabea2058b5ac2d339b163c6ab6f2b6d53aabed` |
| [USDC.e (Celer)](https://flowscan.io/ft/token/A.f1ab99c82dee3526.USDCFlow.Vault) | `0xf1ab99c82dee3526` |
| [stFlow (Increment Staked FLOW)](https://flowscan.io/ft/token/A.d6f80565193ad727.stFlowToken.Vault) | `0xd6f80565193ad727` |
| [ankrFLOWEVM (Ankr Staked FLOW)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_1b97100ea1d7126c4d60027e231ea4cb25314bdb.Vault) | `EVMVMBridgedToken_1b97100ea1d7126c4d60027e231ea4cb25314bdb` |
| [WETH](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_2f6f07cdcf3588944bf4c42ac74ff24bf56e7590.Vault) | `EVMVMBridgedToken_2f6f07cdcf3588944bf4c42ac74ff24bf56e7590` |
| [cbBTC](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_a0197b2044d28b08be34d98b23c9312158ea9a18.Vault) | `EVMVMBridgedToken_a0197b2044d28b08be34d98b23c9312158ea9a18` |

## AMMs & DEXs[​](#amms--dexs "Direct link to AMMs & DEXs")

#### Flow EVM Mainnet[​](#flow-evm-mainnet-1 "Direct link to Flow EVM Mainnet")

| Contract Name | Flow EVM Mainnet Address |
| --- | --- |
| [StableKittyFactoryNG.sol (KittyPunch)](https://evm.flowscan.io/address/0x4412140D52C1F5834469a061927811Abb6026dB7?tab=contract) | `0x4412140D52C1F5834469a061927811Abb6026dB7` |
| [TwoKittyFactory.sol (KittyPunch)](https://evm.flowscan.io/address/0xf0E48dC92f66E246244dd9F33b02f57b0E69fBa9?tab=contract) | `0xf0E48dC92f66E246244dd9F33b02f57b0E69fBa9` |
| [TriKittyFactory.sol (KittyPunch)](https://evm.flowscan.io/address/0xebd098c60b1089f362AC9cfAd9134CBD29408226?tab=contract) | `0xebd098c60b1089f362AC9cfAd9134CBD29408226` |
| [KittyRouterNgPoolsOnly.sol (KittyPunch)](https://evm.flowscan.io/address/0x87048a97526c4B66b71004927D24F61DEFcD6375?tab=contract) | `0x87048a97526c4B66b71004927D24F61DEFcD6375` |
| [PunchSwapV2Router02.sol (KittyPunch)](https://evm.flowscan.io/address/0xf45AFe28fd5519d5f8C1d4787a4D5f724C0eFa4d?tab=contract) | `0xf45AFe28fd5519d5f8C1d4787a4D5f724C0eFa4d` |
| [PunchSwapV2Factory.sol (KittyPunch)](https://evm.flowscan.io/address/0x29372c22459a4e373851798bFd6808e71EA34A71?tab=contract) | `0x29372c22459a4e373851798bFd6808e71EA34A71` |
| [TrenchesTokensBuyer.sol (KittyPunch)](https://evm.flowscan.io/address/0x6D0e081Acc28eA9ee6b7fD293eC03F97147b026d?tab=contract) | `0x6D0e081Acc28eA9ee6b7fD293eC03F97147b026d` |

#### Flow Cadence Mainnet[​](#flow-cadence-mainnet-1 "Direct link to Flow Cadence Mainnet")

| Contract Name | Flow Cadence Mainnet Address |
| --- | --- |
| [SwapFactory.cdc (IncrementFi)](https://contractbrowser.com/A.b063c16cac85dbd1.SwapFactory) | `0xb063c16cac85dbd1` |
| [SwapPair (IncrementFi)](https://contractbrowser.com/A.ecbda466e7f191c7.SwapPair) | `0xecbda466e7f191c7` |
| [SwapError (IncrementFi)](https://contractbrowser.com/A.b78ef7afa52ff906.SwapError) | `0xb78ef7afa52ff906` |
| [SwapInterfaces (IncrementFi)](https://contractbrowser.com/A.b78ef7afa52ff906.SwapInterfaces) | `0xb78ef7afa52ff906` |
| [SwapConfig (IncrementFi)](https://contractbrowser.com/A.b78ef7afa52ff906.SwapConfig) | `0xb78ef7afa52ff906` |
| [SwapRouter (IncrementFi)](https://contractbrowser.com/A.a6850776a94e6551.SwapRouter) | `0xa6850776a94e6551` |

## Bridges & Cross-Chain Messaging[​](#bridges--cross-chain-messaging "Direct link to Bridges & Cross-Chain Messaging")

| Bridge / Protocol | Reference Docs |
| --- | --- |
| Stargate Bridge ([stargate.finance](https://stargate.finance/bridge?srcChain=ethereum&srcToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&dstChain=flow&dstToken=0xF1815bd50389c46847f0Bda824eC8da914045D14)) | [Mainnet Contracts](https://stargateprotocol.gitbook.io/stargate/v2-developer-docs/technical-reference/mainnet-contracts#flow) |
| Hyperlane Bridge ([trump.hyperlane.xyz](https://trump.hyperlane.xyz/)) | [Mainnet Contracts](https://docs.hyperlane.xyz/docs/reference/addresses/mailbox-addresses) |
| Flow Bridge ([bridge.flow.com](https://bridge.flow.com/)) | [Superbridge Docs](https://docs.superbridge.app/) |
| Celer cBridge ([cbridge.celer.network](https://cbridge.celer.network/1/747/USDC-intermediary)) | [Celer cBridge Docs](https://cbridge-docs.celer.network/tutorial/flow-cadence-bridging-guide) |
| LayerZero | [Mainnet Contracts](https://docs.layerzero.network/v1/developers/evm/technical-reference/deployed-contracts?chains=flow) |
| Axelar | [Axelar Docs](https://docs.axelar.dev/validator/external-chains/flow/) |

## Oracles[​](#oracles "Direct link to Oracles")

#### Flow EVM Mainnet[​](#flow-evm-mainnet-2 "Direct link to Flow EVM Mainnet")

| Contract Name | Flow EVM Mainnet Address |
| --- | --- |
| [ERC1967Proxy.sol (Pyth)](https://evm.flowscan.io/address/0x2880aB155794e7179c9eE2e38200202908C17B43?tab=contract) | `0x2880aB155794e7179c9eE2e38200202908C17B43` |

#### Flow Cadence Mainnet[​](#flow-cadence-mainnet-2 "Direct link to Flow Cadence Mainnet")

| Contract Name | Flow Cadence Mainnet Address |
| --- | --- |
| [PublicPriceOracle.cdc (IncrementFi)](https://contractbrowser.com/A.ec67451f8a58216a.PublicPriceOracle) | `0xec67451f8a58216a` |

## Other[​](#other "Direct link to Other")

| Contract Name | Flow EVM Mainnet Address |
| --- | --- |
| [SchemaRegistry.sol (Ethereum Attestation Service)](https://evm.flowscan.io/address/0xB0cF748a05AEA8D59e15834446CFC95bcFF510F0?tab=contract) | `0xB0cF748a05AEA8D59e15834446CFC95bcFF510F0` |
| [EAS.sol (Ethereum Attestation Service)](https://evm.flowscan.io/address/0xc6376222F6E009A705a34dbF1dF72fEf8efB3964?tab=contract) | `0xc6376222F6E009A705a34dbF1dF72fEf8efB3964` |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/ecosystem/defi-liquidity/defi-contracts.md)Last updated on **Feb 14, 2025** by **bz**[PreviousDeFi & Liquidity](/ecosystem/defi-liquidity)[NextStablecoins & Bridges FAQ](/ecosystem/defi-liquidity/faq)
###### Rate this page

😞😐😊

* [Stablecoins & Wrapped Assets](#stablecoins--wrapped-assets)
* [AMMs & DEXs](#amms--dexs)
* [Bridges & Cross-Chain Messaging](#bridges--cross-chain-messaging)
* [Oracles](#oracles)
* [Other](#other)
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

