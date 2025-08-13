# Source: https://github.com/IncrementFi/Swap/blob/main/README.md

# 💱 Swap
A *dual-mode* decentralized exchange (DEX) on [](https://cdn.jsdelivr.net/gh/FlowFans/flow-token-list@main/token-registry/A.1654653399040a61.FlowToken/logo.svg) Flow blockchain supporting both **volatile pairs** (adopting Uniswap-V2 curve, suitable for uncorrelated assets like `Flow/USDC`) and **pegged pairs** (adopting Solidly-Stableswap curve, suitable for correlated assets like `USDC/FUSD`, `Flow/stFlow`, et al.).

It allows users to create arbitrary trading pairs between fungible tokens in a permissionless way, including basic functionalities like `CreatePair`, `AddLiquidity`, `RemoveLiquidity`, `Swap`, `TWAP-Oracle`, `Flashloan`, etc.
  
- It adopts the factory pattern that each unique trading pair is deployed using the `SwapPair` template file, with a factory contract storing all deployed pairs.

- On-chain time-weighted average price oracle of each of the trading pair is supported by snapshoting cumulative data on the first call of any block. Developers can choose different window size to support different TWAP data.

- The trading fee is set to `0.3%` for volatile pairs and `0.04%` for pegged pairs by default. All of the trading fees goes to liquidity providers (LP) initially. However, there's a switch that factory admin can opt to turn on to earn `1/6` of the trading fees.

	 
### Documentation
* [CFAMM DEX Docs](https://docs.increment.fi/protocols/decentralized-exchange/cpamm-dex)
* [Stableswap DEX Docs](https://docs.increment.fi/protocols/decentralized-exchange/stableswap-dex)


### Unittest
* `npm run test`

### Security
* Bug bounty: [rules](https://docs.increment.fi/miscs/bug-bounty)
