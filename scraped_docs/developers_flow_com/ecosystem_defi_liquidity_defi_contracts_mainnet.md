# Source: https://developers.flow.com/ecosystem/defi-liquidity/defi-contracts-mainnet

DeFi Contracts on Flow Mainnet | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Ecosystem Index](/ecosystem)* [Developer Support Hub](/ecosystem/developer-support-hub)

    * [Flow Block Explorers](/ecosystem/block-explorers)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Data Indexers](/ecosystem/data-indexers)* [Developer Profile](/ecosystem/developer-profile)* [Wallets](/ecosystem/wallets)* [DeFi & Liquidity](/ecosystem/defi-liquidity)

                + [Build with Forte ↙](/ecosystem/defi-liquidity/forte)+ [DeFi Contracts Mainnet](/ecosystem/defi-liquidity/defi-contracts-mainnet)+ [DeFi Contracts Testnet](/ecosystem/defi-liquidity/defi-contracts-testnet)+ [Cross-chain swaps on Flow EVM](/ecosystem/defi-liquidity/cross-chain-swaps)+ [Add Token To MetaMask](/ecosystem/defi-liquidity/add-token-to-metamask)+ [Stablecoins & Bridges FAQ](/ecosystem/defi-liquidity/faq)+ [Band Oracle](/ecosystem/defi-liquidity/band-oracle)* [Faucets](/ecosystem/faucets)* [Bridges](/ecosystem/bridges)* [Collectibles & NFTs](/ecosystem/collectibles)* [Community Projects](/ecosystem/projects)* [Auditors](/ecosystem/auditors)

* * [DeFi & Liquidity](/ecosystem/defi-liquidity)* DeFi Contracts Mainnet

On this page

# DeFi Contracts on Flow Mainnet

Flow is a Layer 1 blockchain that supports EVM equivalency, offering two environments Flow EVM and Flow Cadence. Fungible and non-fungible tokens can seamlessly transfer between these environments via the native VM token bridge. As a result, many tokens have both a Flow EVM mainnet contract address and a Flow Cadence mainnet contract address, allowing developers to choose their preferred environment.

Below is a list of commonly used DeFi contracts on Flow Mainnet:

[Switch to DeFi Contracts on Testnet](/ecosystem/defi-liquidity/defi-contracts-testnet)

## Stablecoins & Wrapped Assets[​](#stablecoins--wrapped-assets "Direct link to Stablecoins & Wrapped Assets")

#### Flow EVM Mainnet[​](#flow-evm-mainnet "Direct link to Flow EVM Mainnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Token Name Flow EVM Mainnet Address|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [WFLOW](https://evm.flowscan.io/token/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e) `0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e`| [USDC (stgUSDC)](https://evm.flowscan.io/token/0xF1815bd50389c46847f0Bda824eC8da914045D14) `0xF1815bd50389c46847f0Bda824eC8da914045D14`| [USDT (stgUSDT)](https://evm.flowscan.io/token/0x674843C06FF83502ddb4D37c2E09C01cdA38cbc8) `0x674843C06FF83502ddb4D37c2E09C01cdA38cbc8`| [USDF (USD Flow)](https://evm.flowscan.io/token/0x2aaBea2058b5aC2D339b163C6Ab6f2b6d53aabED) `0x2aaBea2058b5aC2D339b163C6Ab6f2b6d53aabED`| [USDC.e (Celer)](https://evm.flowscan.io/token/0x7f27352D5F83Db87a5A3E00f4B07Cc2138D8ee52) `0x7f27352D5F83Db87a5A3E00f4B07Cc2138D8ee52`| [stFlow (Increment Staked FLOW)](https://evm.flowscan.io/token/0x5598c0652B899EB40f169Dd5949BdBE0BF36ffDe) `0x5598c0652B899EB40f169Dd5949BdBE0BF36ffDe`| [ankrFLOWEVM (Ankr Staked FLOW)](https://evm.flowscan.io/token/0x1b97100eA1D7126C4d60027e231EA4CB25314bdb) `0x1b97100eA1D7126C4d60027e231EA4CB25314bdb`| [WETH](https://evm.flowscan.io/token/0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590) `0x2F6F07CDcf3588944Bf4C42aC74ff24bF56e7590`| [cbBTC](https://evm.flowscan.io/token/0xA0197b2044D28b08Be34d98b23c9312158Ea9A18) `0xA0197b2044D28b08Be34d98b23c9312158Ea9A18` | | | | | | | | | | | | | | | | | | | |

#### Flow Cadence Mainnet[​](#flow-cadence-mainnet "Direct link to Flow Cadence Mainnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Token Name Flow Cadence Mainnet Address Flow Cadence Contract Name|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [FLOW](https://www.flowscan.io/ft/token/A.1654653399040a61.FlowToken.Vault) `0x1654653399040a61` FlowToken|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [USDC (stgUSDC)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_f1815bd50389c46847f0bda824ec8da914045d14.Vault) `0x1e4aa0b87d10b141` EVMVMBridgedToken\_f1815bd50389c46847f0bda824ec8da914045d14|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [USDT (stgUSDT)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_674843c06ff83502ddb4d37c2e09c01cda38cbc8.Vault) `0x1e4aa0b87d10b141` EVMVMBridgedToken\_674843c06ff83502ddb4d37c2e09c01cda38cbc8|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [USDF (USD Flow)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_2aabea2058b5ac2d339b163c6ab6f2b6d53aabed.Vault) `0x1e4aa0b87d10b141` EVMVMBridgedToken\_2aabea2058b5ac2d339b163c6ab6f2b6d53aabed|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [USDC.e (Celer)](https://flowscan.io/ft/token/A.f1ab99c82dee3526.USDCFlow.Vault) `0xf1ab99c82dee3526` USDCFlow|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [stFlow (Increment Staked FLOW)](https://flowscan.io/ft/token/A.d6f80565193ad727.stFlowToken.Vault) `0xd6f80565193ad727` stFlowToken|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [ankrFLOWEVM (Ankr Staked FLOW)](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_1b97100ea1d7126c4d60027e231ea4cb25314bdb.Vault) `0x1e4aa0b87d10b141` EVMVMBridgedToken\_1b97100ea1d7126c4d60027e231ea4cb25314bdb|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [WETH](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_2f6f07cdcf3588944bf4c42ac74ff24bf56e7590.Vault) `0x1e4aa0b87d10b141` EVMVMBridgedToken\_2f6f07cdcf3588944bf4c42ac74ff24bf56e7590|  |  |  | | --- | --- | --- | | [cbBTC](https://flowscan.io/ft/token/A.1e4aa0b87d10b141.EVMVMBridgedToken_a0197b2044d28b08be34d98b23c9312158ea9a18.Vault) `0x1e4aa0b87d10b141` EVMVMBridgedToken\_a0197b2044d28b08be34d98b23c9312158ea9a18 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

#### Flow Cadence Testnet[​](#flow-cadence-testnet "Direct link to Flow Cadence Testnet")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Token Name Flow Cadence Testnet Address Flow Cadence Contract Name|  |  |  | | --- | --- | --- | | [USDF (Mock)](https://testnet.flowscan.io/ft/token/A.b7ace0a920d2c37d.EVMVMBridgedToken_2aabea2058b5ac2d339b163c6ab6f2b6d53aabed.Vault) `0xb7ace0a920d2c37d` EVMVMBridgedToken\_2aabea2058b5ac2d339b163c6ab6f2b6d53aabed | | | | | |

## AMMs & DEXs[​](#amms--dexs "Direct link to AMMs & DEXs")

#### Flow EVM Mainnet[​](#flow-evm-mainnet-1 "Direct link to Flow EVM Mainnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Flow EVM Mainnet Address Docs|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [StableKittyFactoryNG.sol (KittyPunch)](https://evm.flowscan.io/address/0x4412140D52C1F5834469a061927811Abb6026dB7?tab=contract) `0x4412140D52C1F5834469a061927811Abb6026dB7` [Docs](https://kittypunch.gitbook.io/kittypunch-docs)| [TwoKittyFactory.sol (KittyPunch)](https://evm.flowscan.io/address/0xf0E48dC92f66E246244dd9F33b02f57b0E69fBa9?tab=contract) `0xf0E48dC92f66E246244dd9F33b02f57b0E69fBa9` [Docs](https://kittypunch.gitbook.io/kittypunch-docs)| [TriKittyFactory.sol (KittyPunch)](https://evm.flowscan.io/address/0xebd098c60b1089f362AC9cfAd9134CBD29408226?tab=contract) `0xebd098c60b1089f362AC9cfAd9134CBD29408226` [Docs](https://kittypunch.gitbook.io/kittypunch-docs)| [KittyRouterNgPoolsOnly.sol (KittyPunch)](https://evm.flowscan.io/address/0x87048a97526c4B66b71004927D24F61DEFcD6375?tab=contract) `0x87048a97526c4B66b71004927D24F61DEFcD6375` [Docs](https://kittypunch.gitbook.io/kittypunch-docs)| [PunchSwapV2Router02.sol (KittyPunch)](https://evm.flowscan.io/address/0xf45AFe28fd5519d5f8C1d4787a4D5f724C0eFa4d?tab=contract) `0xf45AFe28fd5519d5f8C1d4787a4D5f724C0eFa4d` [Docs](https://kittypunch.gitbook.io/kittypunch-docs)| [PunchSwapV2Factory.sol (KittyPunch)](https://evm.flowscan.io/address/0x29372c22459a4e373851798bFd6808e71EA34A71?tab=contract) `0x29372c22459a4e373851798bFd6808e71EA34A71` [Docs](https://kittypunch.gitbook.io/kittypunch-docs)| [TrenchesTokensBuyer.sol (KittyPunch)](https://evm.flowscan.io/address/0x6D0e081Acc28eA9ee6b7fD293eC03F97147b026d?tab=contract) `0x6D0e081Acc28eA9ee6b7fD293eC03F97147b026d` [Docs](https://kittypunch.gitbook.io/kittypunch-docs) | | | | | | | | | | | | | | | | | | | | | | | |

#### Flow Cadence Mainnet[​](#flow-cadence-mainnet-1 "Direct link to Flow Cadence Mainnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Flow Cadence Mainnet Address [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager) Docs|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [SwapFactory (IncrementFi)](https://flowscan.io/contract/A.b063c16cac85dbd1.SwapFactory) `0xb063c16cac85dbd1` [Docs](https://docs.increment.fi/)| [SwapPair (IncrementFi)](https://flowscan.io/contract/A.ecbda466e7f191c7.SwapPair) `0xecbda466e7f191c7` [Docs](https://docs.increment.fi/)| [SwapError (IncrementFi)](https://flowscan.io/contract/A.b78ef7afa52ff906.SwapError) `0xb78ef7afa52ff906` [Docs](https://docs.increment.fi/)| [SwapInterfaces (IncrementFi)](https://flowscan.io/contract/A.b78ef7afa52ff906.SwapInterfaces) `0xb78ef7afa52ff906` [Docs](https://docs.increment.fi/)| [SwapConfig (IncrementFi)](https://flowscan.io/contract/A.b78ef7afa52ff906.SwapConfig) `0xb78ef7afa52ff906` [Docs](https://docs.increment.fi/)| [SwapRouter (IncrementFi)](https://flowscan.io/contract/A.a6850776a94e6551.SwapRouter) `0xa6850776a94e6551` [Docs](https://docs.increment.fi/) | | | | | | | | | | | | | | | | | | | | | | | | | | | |

## Bridges & Cross-Chain Messaging[​](#bridges--cross-chain-messaging "Direct link to Bridges & Cross-Chain Messaging")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bridge / Protocol Reference Docs|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Stargate Bridge ([stargate.finance](https://stargate.finance/bridge?srcChain=ethereum&srcToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&dstChain=flow&dstToken=0xF1815bd50389c46847f0Bda824eC8da914045D14)) [Mainnet Contracts](https://stargateprotocol.gitbook.io/stargate/v2-developer-docs/technical-reference/mainnet-contracts#flow)| Hyperlane Bridge ([trump.hyperlane.xyz](https://trump.hyperlane.xyz/)) [Mainnet Contracts](https://docs.hyperlane.xyz/docs/reference/addresses/mailbox-addresses)| Flow Bridge ([bridge.flow.com](https://bridge.flow.com/)) [Superbridge Docs](https://docs.superbridge.app/)| Celer cBridge ([cbridge.celer.network](https://cbridge.celer.network/1/747/USDC-intermediary)) [Celer cBridge Docs](https://cbridge-docs.celer.network/tutorial/flow-cadence-bridging-guide)| DeBridge ([app.debridge.finance](https://app.debridge.finance/)) [DeBridge Contracts](https://docs.debridge.finance/dln-the-debridge-liquidity-network-protocol/deployed-contracts)| Relay ([relay.link](https://relay.link/bridge)) [Relay Contracts](https://docs.relay.link/resources/contract-addresses)| LayerZero [Mainnet Contracts](https://docs.layerzero.network/v1/developers/evm/technical-reference/deployed-contracts?chains=flow)| Axelar [Axelar Docs](https://docs.axelar.dev/validator/external-chains/flow/) | | | | | | | | | | | | | | | | | |

## Omni Fungible Tokens (PYUSD → USDF)[​](#omni-fungible-tokens-pyusd--usdf "Direct link to Omni Fungible Tokens (PYUSD → USDF)")

#### Solana Mainnet[​](#solana-mainnet "Direct link to Solana Mainnet")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Contract Address|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | PYUSD Program ID `28EyPNAi9BMTvGuCaQrptMXjpWUi7wx8SxAFVoSZxSXe`| PYUSD Mint `2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo`| PYUSD Mint Authority `22mKJkKjGEQ3rampp5YKaSsaYZ52BUkcnUN6evXGsXzz`| PYUSD Escrow `6z3QyVS36nQ9fk2YvToxqJqXqtAFsSijqgHxpzKyG5xn`| PYUSD OFT Store `2KUb8dcZR9LyrSg4RdkQx91xX6mPQLpS1MEo6gwfvLZk` | | | | | | | | | | | |

#### Ethereum Mainnet[​](#ethereum-mainnet "Direct link to Ethereum Mainnet")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Name Contract Address|  |  |  |  | | --- | --- | --- | --- | | PYUSD Token `0x6c3ea9036406852006290770BEdFcAbA0e23A0e8`| PYUSD Locker `0xFA0e06B54986ad96DE87a8c56Fea76FBD8d493F8` | | | | | |

## Oracles[​](#oracles "Direct link to Oracles")

#### Flow EVM Mainnet[​](#flow-evm-mainnet-2 "Direct link to Flow EVM Mainnet")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Name Flow EVM Mainnet Address|  |  |  |  | | --- | --- | --- | --- | | [ERC1967Proxy.sol (Pyth)](https://evm.flowscan.io/address/0x2880aB155794e7179c9eE2e38200202908C17B43?tab=contract) `0x2880aB155794e7179c9eE2e38200202908C17B43`| [ERC1967Proxy.sol (Stork)](https://evm.flowscan.io/address/0xacC0a0cF13571d30B4b8637996F5D6D774d4fd62?tab=contract) `0xacC0a0cF13571d30B4b8637996F5D6D774d4fd62` | | | | | |

#### Flow Cadence Mainnet[​](#flow-cadence-mainnet-2 "Direct link to Flow Cadence Mainnet")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Flow Cadence Mainnet Address [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager) Docs|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [PublicPriceOracle.cdc (IncrementFi)](https://flowscan.io/contract/A.ec67451f8a58216a.PublicPriceOracle) `0xec67451f8a58216a` [Docs](https://docs.increment.fi/)| [BandOracle.cdc (Band) Protocol](https://flowscan.io/contract/A.6801a6222ebf784a.BandOracle) `0x6801a6222ebf784a` [Docs](/ecosystem/defi-liquidity/band-oracle) | | | | | | | | | | | |

## Ethereum Attestation Service[​](#ethereum-attestation-service "Direct link to Ethereum Attestation Service")

More information can be found on the Credora docs site for [EAS on Flow](https://credora.gitbook.io/eas-for-flow).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Name Flow EVM Mainnet Address|  |  |  |  | | --- | --- | --- | --- | | [SchemaRegistry.sol (Ethereum Attestation Service)](https://evm.flowscan.io/address/0xB0cF748a05AEA8D59e15834446CFC95bcFF510F0?tab=contract) `0xB0cF748a05AEA8D59e15834446CFC95bcFF510F0`| [EAS.sol (Ethereum Attestation Service)](https://evm.flowscan.io/address/0xc6376222F6E009A705a34dbF1dF72fEf8efB3964?tab=contract) `0xc6376222F6E009A705a34dbF1dF72fEf8efB3964` | | | | | |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/ecosystem/defi-liquidity/defi-contracts-mainnet.md)

Last updated on **Oct 29, 2025** by **bz**

[Previous

Build with Forte ↙](/ecosystem/defi-liquidity/forte)[Next

DeFi Contracts Testnet](/ecosystem/defi-liquidity/defi-contracts-testnet)

###### Rate this page

😞😐😊

Copy as Markdown

* [Stablecoins & Wrapped Assets](#stablecoins--wrapped-assets)* [AMMs & DEXs](#amms--dexs)* [Bridges & Cross-Chain Messaging](#bridges--cross-chain-messaging)* [Omni Fungible Tokens (PYUSD → USDF)](#omni-fungible-tokens-pyusd--usdf)* [Oracles](#oracles)* [Ethereum Attestation Service](#ethereum-attestation-service)

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