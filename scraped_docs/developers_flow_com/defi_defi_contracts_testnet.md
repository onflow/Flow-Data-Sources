# Source: https://developers.flow.com/defi/defi-contracts-testnet

DeFi Contracts on Flow Testnet | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Defi](/defi)* [Build with Forte ↙](/defi/forte)* [DeFi Contracts Mainnet](/defi/defi-contracts-mainnet)* [DeFi Contracts Testnet](/defi/defi-contracts-testnet)* [Cross-chain swaps on Flow EVM](/defi/cross-chain-swaps)* [Add Token To MetaMask](/defi/add-token-to-metamask)* [Band Oracle](/defi/band-oracle)* [Stablecoins & Bridges FAQ](/defi/faq)* [PYUSD0 Integration](/defi/pyusd0-integration-guide)

* * DeFi Contracts Testnet

On this page

# DeFi Contracts on Flow Testnet

Flow is a Layer 1 blockchain that supports EVM equivalency, offering two environments Flow EVM and Flow Cadence. Fungible and non-fungible tokens can seamlessly transfer between these environments via the native VM token bridge. As a result, many tokens have both a Flow EVM mainnet contract address and a Flow Cadence mainnet contract address, allowing developers to choose their preferred environment.

Below is a list of commonly used DeFi contracts on Flow Testnet:

[Switch to DeFi Contracts on Mainnet](/defi/defi-contracts-mainnet)

## Stablecoins & Wrapped Assets[​](#stablecoins--wrapped-assets "Direct link to Stablecoins & Wrapped Assets")

#### Flow EVM Testnet[​](#flow-evm-testnet "Direct link to Flow EVM Testnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Token EVM Testnet Address How to Get|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | FLOW (native, non-erc20) — [Faucet](https://faucet.flow.com/fund-account)| [WFLOW](https://evm-testnet.flowscan.io/address/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e) `0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e` [Swap](https://flowswap.io/swap?chain=flow-testnet&inputCurrency=NATIVE&outputCurrency=0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e)| [MOET](https://evm-testnet.flowscan.io/address/0x51f5cc5f50afb81e8f23c926080fa38c3024b238) `0x51f5cc5f50afb81e8f23c926080fa38c3024b238` [Swap](https://flowswap.io/swap?chain=flow-testnet&inputCurrency=NATIVE&outputCurrency=0x51F5cC5f50afB81e8F23C926080FA38C3024b238)| [MockUSDC](https://evm-testnet.flowscan.io/address/0xd431955D55a99EF69BEb96BA34718d0f9fBc91b1) `0xd431955D55a99EF69BEb96BA34718d0f9fBc91b1` [Swap](https://flowswap.io/swap?chain=flow-testnet&inputCurrency=NATIVE&outputCurrency=0xd431955D55a99EF69BEb96BA34718d0f9fBc91b1)| [mUSDC](https://evm-testnet.flowscan.io/address/0x4154d5B0E2931a0A1E5b733f19161aa7D2fc4b95) `0x4154d5B0E2931a0A1E5b733f19161aa7D2fc4b95` [Swap](https://flowswap.io/swap?chain=flow-testnet&inputCurrency=NATIVE&outputCurrency=0x4154d5B0E2931a0A1E5b733f19161aa7D2fc4b95)| [PYUSD0](https://evm-testnet.flowscan.io/address/0xd7d43ab7b365f0d0789aE83F4385fA710FfdC98F) `0xd7d43ab7b365f0d0789aE83F4385fA710FfdC98F` [Swap](https://flowswap.io/swap?chain=flow-testnet&inputCurrency=NATIVE&outputCurrency=0xd7d43ab7b365f0d0789aE83F4385fA710FfdC98F)| [USD Flow](https://evm-testnet.flowscan.io/address/0xf2E5A325f7D678DA511E66B1c0Ad7D5ba4dF93D3) `0xf2E5A325f7D678DA511E66B1c0Ad7D5ba4dF93D3` —|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [USDC.e](https://evm-testnet.flowscan.io/address/0x9B7550D337bB449b89C6f9C926C3b976b6f4095b) `0x9B7550D337bB449b89C6f9C926C3b976b6f4095b` —|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [ankrFLOW](https://evm-testnet.flowscan.io/address/0xe132751AB5A14ac0bD3Cb40571a9248Ee7a2a9EA) `0xe132751AB5A14ac0bD3Cb40571a9248Ee7a2a9EA` —|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [ankrFLOWEVM](https://evm-testnet.flowscan.io/address/0x8E3DC6E937B560ce6a1Aaa78AfC775228969D16c) `0x8E3DC6E937B560ce6a1Aaa78AfC775228969D16c` —|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [ETHf](https://evm-testnet.flowscan.io/address/0x059A77239daFa770977DD9f1E98632C3E4559848) `0x059A77239daFa770977DD9f1E98632C3E4559848` [Mint](https://evm-testnet.flowscan.io/address/0x059A77239daFa770977DD9f1E98632C3E4559848?tab=read_write_contract#0x40c10f19)| [BTCf](https://evm-testnet.flowscan.io/address/0x208d09d2a6Dd176e3e95b3F0DE172A7471C5B2d6) `0x208d09d2a6Dd176e3e95b3F0DE172A7471C5B2d6` [Mint](https://evm-testnet.flowscan.io/address/0x208d09d2a6Dd176e3e95b3F0DE172A7471C5B2d6?tab=read_write_contract#0x40c10f19)| [cbBTC](https://evm-testnet.flowscan.io/address/0x30F44C64725727F2001E6C1eF6e6CE9c7aB91dC3) `0x30F44C64725727F2001E6C1eF6e6CE9c7aB91dC3` [Mint](https://evm-testnet.flowscan.io/address/0x30F44C64725727F2001E6C1eF6e6CE9c7aB91dC3?tab=read_write_contract#0x40c10f19) | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

#### Flow Cadence Testnet[​](#flow-cadence-testnet "Direct link to Flow Cadence Testnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Token Cadence Testnet Address Cadence Contract Name|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [FLOW](https://testnet.flowscan.io/contract/A.7e60df042a9c0868.FlowToken?tab=deployments) `0x7e60df042a9c0868` `FlowToken`| [MOET](https://testnet.flowscan.io/contract/A.d27920b6384e2a78.MOET?tab=deployments) `0xd27920b6384e2a78` `MOET`| [USDC](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_d431955d55a99ef69beb96ba34718d0f9fbc91b1?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_d431955d55a99ef69beb96ba34718d0f9fbc91b1`| [mUSDC](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_4154d5b0e2931a0a1e5b733f19161aa7d2fc4b95?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_4154d5b0e2931a0a1e5b733f19161aa7d2fc4b95`| [USDF (Mock)](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_d7d43ab7b365f0d0789ae83f4385fa710ffdc98f?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_d7d43ab7b365f0d0789ae83f4385fa710ffdc98f`| [USDF (PYUSD)](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_f2e5a325f7d678da511e66b1c0ad7d5ba4df93d3?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_f2e5a325f7d678da511e66b1c0ad7d5ba4df93d3`| [USDC.e (Celer)](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_9b7550d337bb449b89c6f9c926c3b976b6f4095b?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_9b7550d337bb449b89c6f9c926c3b976b6f4095b`| [ankrFLOWEVM](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_8e3dc6e937b560ce6a1aaa78afc775228969d16c?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_8e3dc6e937b560ce6a1aaa78afc775228969d16c`| [WETH](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_059a77239dafa770977dd9f1e98632c3e4559848?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_059a77239dafa770977dd9f1e98632c3e4559848`| [WBTC](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_208d09d2a6dd176e3e95b3f0de172a7471c5b2d6?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_208d09d2a6dd176e3e95b3f0de172a7471c5b2d6`| [cbBTC](https://testnet.flowscan.io/contract/A.dfc20aee650fcbdf.EVMVMBridgedToken_30f44c64725727f2001e6c1ef6e6ce9c7ab91dc3?tab=deployments) `0xdfc20aee650fcbdf` `EVMVMBridgedToken_30f44c64725727f2001e6c1ef6e6ce9c7ab91dc3` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

## Vaults[​](#vaults "Direct link to Vaults")

#### Flow EVM Testnet[​](#flow-evm-testnet-1 "Direct link to Flow EVM Testnet")

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Address|  |  |  |  | | --- | --- | --- | --- | | [MockTauVault](https://evm-testnet.flowscan.io/address/0x72104434BEc686B47a72bCa9b998624238BD2Ffb) `0x72104434BEc686B47a72bCa9b998624238BD2Ffb`| [MockYieldVault](https://evm-testnet.flowscan.io/address/0x217aAC9594EcB6d3f6667A214CF579dd29ce78dd) `0x217aAC9594EcB6d3f6667A214CF579dd29ce78dd` | | | | | |

## AMMs & DEXs[​](#amms--dexs "Direct link to AMMs & DEXs")

#### Flow EVM Testnet[​](#flow-evm-testnet-2 "Direct link to Flow EVM Testnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract EVM Testnet Address|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [UniswapV2Factory (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x7d726261FB76B264fc20eA1f19D900D760136566) `0x7d726261FB76B264fc20eA1f19D900D760136566`| [UniswapV2Router02 (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x524E1291c109BE27FDE48De97cAf0B3c0F02A68f) `0x524E1291c109BE27FDE48De97cAf0B3c0F02A68f`| [UniswapV2Pair (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x21E3aa01561d7D869785aAedB14130C5807C5A12) `0x21E3aa01561d7D869785aAedB14130C5807C5A12`| [UniswapV3Factory (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x92657b195e22b69E4779BBD09Fa3CD46F0CF8e39) `0x92657b195e22b69E4779BBD09Fa3CD46F0CF8e39`| [NonfungiblePositionManager (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x8b9F96390EC35d5859937c7c5D68Ff6D5CFC312f) `0x8b9F96390EC35d5859937c7c5D68Ff6D5CFC312f`| [SwapRouter02 (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x2Db6468229F6fB1a77d248Dbb1c386760C257804) `0x2Db6468229F6fB1a77d248Dbb1c386760C257804`| [QuoterV2 (FlowSwap)](https://testnet.flowscan.io/evm/contract/0xA1e0E4CCACA34a738f03cFB1EAbAb16331FA3E2c) `0xA1e0E4CCACA34a738f03cFB1EAbAb16331FA3E2c`| [V3Migrator (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x00a101726ff770cd8ed53E8376b9440Bad40CAd9) `0x00a101726ff770cd8ed53E8376b9440Bad40CAd9`| [UniswapV3Staker (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x04400857ad69EaA7dd6fEF1C329E80E50BD30b76) `0x04400857ad69EaA7dd6fEF1C329E80E50BD30b76`| [TickLens (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x36D9bDCbA840F5bcb95EE7bD54a86808aef6581F) `0x36D9bDCbA840F5bcb95EE7bD54a86808aef6581F`| [NFTDescriptor (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x6982D5Cb80Cd7E2cb7C0d0B8452841471Bc84Bc2) `0x6982D5Cb80Cd7E2cb7C0d0B8452841471Bc84Bc2`| [v3\_nft\_position\_descriptor (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x61f4e983A72d9BD8429154982A3d9fCF3A1D98d0) `0x61f4e983A72d9BD8429154982A3d9fCF3A1D98d0`| [TransparentUpgradeableProxy (FlowSwap)](https://testnet.flowscan.io/evm/contract/0xE0895150a7c84e8fB9fecCE72F4C80c130C80fDa) `0xE0895150a7c84e8fB9fecCE72F4C80c130C80fDa`| [UniswapV3Pool (FlowSwap)](https://testnet.flowscan.io/evm/contract/0xa4Db57e3d3c6674FA02a2f3a667d3C22Fe17efF4) `0xa4Db57e3d3c6674FA02a2f3a667d3C22Fe17efF4`| [UniversalRouter (FlowSwap)](https://testnet.flowscan.io/evm/contract/0xB685ab04Dfef74c135A2ed4003441fF124AFF9a0) `0xB685ab04Dfef74c135A2ed4003441fF124AFF9a0`| [Permit2 (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x000000000022D473030F116dDEE9F6B43aC78BA3) `0x000000000022D473030F116dDEE9F6B43aC78BA3`| [FusionXInterfaceMulticall (FlowSwap)](https://testnet.flowscan.io/evm/contract/0x02b9B840CDCEe84510a02cc85f351CAaD41f46CE) `0x02b9B840CDCEe84510a02cc85f351CAaD41f46CE`| [proxy\_admin (FlowSwap)](https://testnet.flowscan.io/evm/contract/0xf4011F45A666dC7eC54445a710c3aae735F7E890) `0xf4011F45A666dC7eC54445a710c3aae735F7E890`| [StableKittyFactoryNG (KittyPunch)](https://evm-testnet.flowscan.io/address/0x0699C35C0104e478f510531F5Dfc3F9313ae49D1) `0x0699C35C0104e478f510531F5Dfc3F9313ae49D1`| [TwoKittyFactory (KittyPunch)](https://evm-testnet.flowscan.io/address/0xeaa5949471C7B31ae97D3a52483028aE595E8e83) `0xeaa5949471C7B31ae97D3a52483028aE595E8e83`| [TriKittyFactory (KittyPunch)](https://evm-testnet.flowscan.io/address/0x62aC6e05Bac04702bF744106499F72f200297121) `0x62aC6e05Bac04702bF744106499F72f200297121`| [KittyRouterNgPoolsOnly (KittyPunch)](https://evm-testnet.flowscan.io/address/0x70e8C797f698De61787A7275628713077723694) `0x70e8C797f698De61787A7275628713077723694`| [PunchSwapV2Router02 (KittyPunch)](https://evm-testnet.flowscan.io/address/0xeD53235cC3E9d2d464E9c408B95948836648870B) `0xeD53235cC3E9d2d464E9c408B95948836648870B`| [PunchSwapV2Factory (KittyPunch)](https://evm-testnet.flowscan.io/address/0x0f6C2EF40FA42B2F0E0a9f5987b2f3F8Af3C173f) `0x0f6C2EF40FA42B2F0E0a9f5987b2f3F8Af3C173f` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

#### Flow Cadence Testnet[​](#flow-cadence-testnet-1 "Direct link to Flow Cadence Testnet")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Cadence Testnet Address [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [StableSwapFactory (IncrementFi)](https://testnet.flowscan.io/contract/A.6ca93d49c45a249f.StableSwapFactory?tab=deployments) `0x6ca93d49c45a249f` | [SwapFactory (IncrementFi)](https://testnet.flowscan.io/contract/A.6ca93d49c45a249f.SwapFactory?tab=deployments) `0x6ca93d49c45a249f` | [SwapPair (IncrementFi)](https://testnet.flowscan.io/contract/A.7afd587a5d5e2efe.SwapPair?tab=deployments) `0x7afd587a5d5e2efe` | [SwapConfig (IncrementFi)](https://testnet.flowscan.io/contract/A.8d5b9dd833e176da.SwapConfig?tab=deployments) `0x8d5b9dd833e176da` | [SwapError (IncrementFi)](https://testnet.flowscan.io/contract/A.8d5b9dd833e176da.SwapError?tab=deployments) `0x8d5b9dd833e176da` | [SwapInterfaces (IncrementFi)](https://testnet.flowscan.io/contract/A.8d5b9dd833e176da.SwapInterfaces?tab=deployments) `0x8d5b9dd833e176da`  | | | | | | | | | | | | | | | | | | | | |

## Bridges & Cross-Chain Messaging[​](#bridges--cross-chain-messaging "Direct link to Bridges & Cross-Chain Messaging")

|  |  |  |  |
| --- | --- | --- | --- |
| Bridge / Protocol Reference Docs|  |  | | --- | --- | | PYUSD -> USDF (LayerZero OFT) [GitHub Repo](https://github.com/onflow/flow-bridge-app?tab=readme-ov-file#evm-testnets) | | | |

## Omni Fungible Tokens (PYUSD → USDF)[​](#omni-fungible-tokens-pyusd--usdf "Direct link to Omni Fungible Tokens (PYUSD → USDF)")

#### Solana Devnet/Testnet[​](#solana-devnettestnet "Direct link to Solana Devnet/Testnet")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Contract Address|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | PYUSD Program ID `D6RHLYN7x69Cb5Y7dFj9T9uJrJCVT9Bt1LT71xHf7QqK`| PYUSD Mint `CXk2AMBfi3TwaEL2468s6zP8xq9NxTXjp9gjMgzeUynM`| PYUSD Mint Authority `A6v157j6XFJXwtT5VWXX7uLYTUrxcYGXB8R6rxrgr9hQ`| PYUSD Escrow `FKt7QuGTkFWHVt7RVgtEsh3rVRZMaeCdQBseyQ9Vf1PN`| PYUSD OFT Store `CFVgSccTEXbs3hN7gnCHx3FAa1L5j5StsKABTPuMaAYo` | | | | | | | | | | | |

#### Sepolia Testnet[​](#sepolia-testnet "Direct link to Sepolia Testnet")

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Contract Address|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | MyOFTAdapter `0x9D6e122780974a917952D70646dD50D2C4f906ae`| PYUSDLocker `0xb077Ef2833Fd7b426146839a86100708c37bfa65`| MyFungi `0x39dBc26413e6eEe40265E4a7ddc5abDC64849781` | | | | | | | |

#### Arbitrum Sepolia Testnet[​](#arbitrum-sepolia-testnet "Direct link to Arbitrum Sepolia Testnet")

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Contract Address|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | MyOFTAdapter `0xDD3BFfb358eF34C2964CB9ce29013D071d59094C`| PYUSDLocker `0x4e2dCCAfe86719B7BFfAc3b1041031dDd07aF5fF`| MyFungi `0x1605B1067Ce0D294786A09368f38063Df50C0e92` | | | | | | | |

## Oracles[​](#oracles "Direct link to Oracles")

#### Flow EVM Testnet[​](#flow-evm-testnet-3 "Direct link to Flow EVM Testnet")

|  |  |  |  |
| --- | --- | --- | --- |
| Contract EVM Testnet Address|  |  | | --- | --- | | [Pyth (ERC1967Proxy)](https://evm-testnet.flowscan.io/address/0x2880aB155794e7179c9eE2e38200202908C17B43) `0x2880aB155794e7179c9eE2e38200202908C17B43` | | | |

#### Flow Cadence Testnet[​](#flow-cadence-testnet-2 "Direct link to Flow Cadence Testnet")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract Name Flow Cadence Testnet Address [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager) Docs|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | [PublicPriceOracle.cdc (IncrementFi)](https://flowscan.io/contract/A.ec67451f8a58216a.PublicPriceOracle) `0x8232ce4a3aff4e94` [Docs](https://docs.increment.fi/)| [BandOracle.cdc (Band)](https://testnet.flowscan.io/contract/A.9fb6606c300b5051.BandOracle) `0x9fb6606c300b5051` [Docs](/defi/band-oracle) | | | | | | | | | | | |

## Ethereum Attestation Service[​](#ethereum-attestation-service "Direct link to Ethereum Attestation Service")

More information can be found on the Credora docs site for [EAS on Flow](https://credora.gitbook.io/eas-for-flow).

Testnet EAS Explorer: <https://flow-testnet.easscan.credora.io>

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Contract Name Flow EVM Testnet Address|  |  |  |  | | --- | --- | --- | --- | | [SchemaRegistry.sol (Ethereum Attestation Service)](https://evm-testnet.flowscan.io/address/0x97900F59828Da4187607Cb8F84f49e3944199d18?tab=contract) `0x97900F59828Da4187607Cb8F84f49e3944199d18`| [EAS.sol (Ethereum Attestation Service)](https://evm-testnet.flowscan.io/address/0xBCF2dA8f82fb032A2474c92Ec5b70C95A83fc0cc?tab=contract) `0xBCF2dA8f82fb032A2474c92Ec5b70C95A83fc0cc` | | | | | |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/defi/defi-contracts-testnet.md)

Last updated on **Jan 28, 2026** by **bz**

[Previous

DeFi Contracts Mainnet](/defi/defi-contracts-mainnet)[Next

Cross-chain swaps on Flow EVM](/defi/cross-chain-swaps)

###### Rate this page

😞😐😊

Copy as Markdown

* [Stablecoins & Wrapped Assets](#stablecoins--wrapped-assets)* [Vaults](#vaults)* [AMMs & DEXs](#amms--dexs)* [Bridges & Cross-Chain Messaging](#bridges--cross-chain-messaging)* [Omni Fungible Tokens (PYUSD → USDF)](#omni-fungible-tokens-pyusd--usdf)* [Oracles](#oracles)* [Ethereum Attestation Service](#ethereum-attestation-service)

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