# Source: https://developers.flow.com/ecosystem/defi-liquidity/faq




Stablecoins & Bridges on Flow FAQ | Flow Developer Portal





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
* Stablecoins & Bridges FAQ
On this page
# DeFi & Liquidity FAQ

Below are common questions regarding stablecoins, liquidity, and bridging on Flow. Click on each question to expand and view the answer.

## Stablecoins on Flow[​](#stablecoins-on-flow "Direct link to Stablecoins on Flow")

What stablecoins are available on Flow?

USDC (USD Coin) - Issued by Circle

USDT (Tether USD) - Issued by Tether

USDF (USD Flow) - Backed by PYUSD (PayPal USD) issued by PayPal


What are the smart contract addresses for the stablecoins and bridges on Flow?

You can find all the contract addresses for the stablecoins and bridges on Flow here:  

[DeFi Contracts on Flow](/ecosystem/defi-liquidity/defi-contracts)


Where can I trade stablecoins on Flow?

Stablecoins can be traded on major Flow-based decentralized exchanges (DEXs) like:

* KittyPunch, PunchSwap - <https://swap.kittypunch.xyz/>
* IncrementFi, IncrementSwap - [https://app.increment.fi/swap](https://app.increment.fi/swap?in=A.1654653399040a61.FlowToken&out=)

How can I earn yield on stablecoins on Flow?

You can earn yield through:

* Lending Platforms - Supply stablecoins on [IncrementFi](https://app.increment.fi/dashboard) & [MoreMarkets](https://app.more.markets/) to earn interest.
* Liquidity Pools - Provide liquidity on [IncrementFi](https://app.increment.fi/liquidity) or [KittyPunch](https://www.kittypunch.xyz/) to earn trading fees and farm LP tokens.
* Yield Aggregators (Coming soon) - Use [KittyPunch](https://app.kittypunch.xyz/) to automate stablecoin yield strategies.

Is it safe to use stablecoins on Flow?

Stablecoins on Flow are designed to be secure and efficient but as with any blockchain asset, there are risks to be aware of:

* Depegging - While rare, some stablecoins have lost their peg in the past due to liquidity issues or market crashes. Flow stablecoins like USDC and USDF are backed by trusted issuers to maintain stability.
* Smart Contract Risks - Bugs or exploits in DeFi platforms can lead to losses.
* Centralization Risks - USDC and USDT are controlled by centralized issuers who can freeze assets.
* Bridging Risks - Flow stablecoins (USDC, USDT, USDF) use LayerZero for bridging, a secure and widely adopted cross-chain solution. While all bridges carry some risk, LayerZero is built with advanced security measures to reduce vulnerabilities.

How can I bridge stablecoins to and from Flow?

You can bridge USDC, USDT, and USDF via <https://bridge.flow.com/> or <https://stargate.finance/bridge>

### Step-by-step example USDC to Flow[​](#step-by-step-example-usdc-to-flow "Direct link to Step-by-step example USDC to Flow")

1. Go to any of the bridges (e.g. <https://stargate.finance/bridge>)
2. Connect your wallet that holds USDC
3. Select the source chain (e.g. Ethereum, BNB Chain, Base)
4. Choose Flow as the destination chain
5. Enter the amount of USDC you want to bridge
6. Approve and confirm the transaction
7. Wait for the transfer to complete - It usually takes a few minutes

What are the fees for using stablecoins on Flow?

Flow’s transaction fees are extremely low (typically less than $0.000179 per transaction), making stablecoin transfers and trading much cheaper than on any other chain.

In many cases, Flow Wallet or Flow-based apps sponsor the gas fees, meaning users can transact stablecoins without paying any gas. This makes Flow an ideal chain for cost-efficient DeFi transactions.


Can I use stablecoins for payments on Flow?

Stablecoins can be used for payments on Flow with services like:

[Beezie](https://beezie.io/), [Flowty](https://www.flowty.io/), [Flowverse](https://nft.flowverse.co/) and many other platforms.


What are some upcoming innovations in stablecoins on Flow?

* DeFi integrations with RWAs (Real World Assets).
* Stay tuned on [Flow X account](https://x.com/flow_blockchain) or via the community [Flowverse](https://x.com/flowverse_)
## Stargate and LayerZero on Flow[​](#stargate-and-layerzero-on-flow "Direct link to Stargate and LayerZero on Flow")

What is LayerZero?

LayerZero is an omnichain interoperability protocol that enables seamless cross-chain communication between different blockchains. It allows assets, messages, and data to move securely between chains without relying on traditional bridges.


What is Stargate?

Stargate is a liquidity transfer protocol built on LayerZero that allows users to bridge assets across multiple blockchains with minimal slippage and deep liquidity.


How does Stargate support Flow?

With Stargate now supporting Flow, users can bridge assets to and from Flow blockchain via [Stargate Finance](https://stargate.finance/bridge). This enables Flow to interact with other major chains like Ethereum, Base, Arbitrum One, and BNB Chain, unlocking global onchain liquidity for Flow-based apps and DeFi protocols.


What assets can be bridged to Flow via Stargate?

Currently, Stargate supports bridging USDC, USDT, and ETH between Flow and other chains. Additional assets may be added in the future.


What are the fees for bridging USDC/USDT/ETH with Stargate?

* Total fees: You pay gas fees + relayer fees, typically less than $1.5 per bridge transaction.
* Gas fees vary depending on network congestion and gas prices.
* Bridging from Ethereum costs around 0.0003868 ETH (~$1.04) in gas fees, plus LayerZero relayer fees of 0.00003536 ETH ($0.095).
* Flow’s transaction fees are extremely low (typically less than $0.000179 per transaction), making stablecoin transfers and trading significantly cheaper than other chains.
* In many cases, Flow Wallet or Flow-based apps sponsor gas fees, allowing users to bridge and transact stablecoins with zero cost on Flow.

How fast is bridging between Flow and other chains?

* Most transactions settle within a few minutes (~3 mins).
* Congestion on the source chain can cause delays.

Is bridging via Stargate safe?

Stargate is built on LayerZero, a well-audited and widely used interoperability protocol.

* Secure & Trusted – Used by top DeFi ecosystems with rigorous security audits.
* Efficient & Cost-Effective – Fast transactions with low fees, especially on Flow.
* Reliable Bridged Assets – USDC, USDT, and ETH bridged via Stargate are fully supported in Flow’s DeFi ecosystem.

Tip: Always verify official links to ensure a safe bridging experience.


What are the benefits of LayerZero on Flow?

* Direct USDC transfers between Flow and other blockchains.
* Unlocks cross-chain DeFi use cases (e.g., lending, trading, staking).
* Low fees and high-speed transactions on Flow.

Can I use Stargate to bridge NFTs or other tokens to Flow?

Currently, Stargate only supports stablecoins like USDC and USDT, but NFT and asset bridging may be possible in the future via LayerZero-based messaging.


What are some use cases for LayerZero on Flow?

* **DeFi**: Seamless liquidity transfer between Flow and other ecosystems.
* **Gaming**: Cross-chain in-game assets & currency settlements.
* **Payments**: Fast and low-cost USDC/USDT/USDF transactions.
* **NFTs**: Future potential for cross-chain NFT bridging.

What wallets support LayerZero bridging on Flow?

You can use any EVM wallet such as Metamask, Coinbase Wallet, and Flow Wallet.


What stablecoins are currently live on Flow EVM?

You can see a full list of stablecoins here:  

[DeFi Contracts on Flow](/ecosystem/defi-liquidity/defi-contracts)

Trading pools for USDF and stgUSDC (USDC via Stargate) are already live and available for immediate use on Flow EVM and can be seamlessly transferred to any Flow Cadence address.


Should Cadence applications switch to USDF or stgUSDC?

Cadence applications can use USDC.e as the default, but they now also have the option to support USDF or stgUSDC based on their needs.

If you have questions you can join [Flow Discord](https://discord.gg/flow) to get free technical support.

## Support and Additional Resources[​](#support-and-additional-resources "Direct link to Support and Additional Resources")

Where can I check the status of my bridge transaction?

* Use [Stargate’s Explorer](https://stargate.finance/bridge) to track your transfer.
* You can also check Flow transactions on [evm.flowscan.io](https://evm.flowscan.io)
* You can also visit <https://bridge.flow.com/> and connect your wallet to view activity.

Where can I get support if I have issues with the bridge?

* **Stargate Discord**: <https://discord.com/invite/9sFqx9U>
* **Flow Discord**: <https://discord.gg/flow>

Where can I get updates or ask questions?

* **Flow Twitter/X:** <https://x.com/flow_blockchain>
* **Flow Discord**: <https://discord.gg/flow>
[Edit this page](https://github.com/onflow/docs/tree/main/docs/ecosystem/defi-liquidity/faq.md)Last updated on **Feb 14, 2025** by **bz**[PreviousDeFi Contracts](/ecosystem/defi-liquidity/defi-contracts)[NextBridges](/ecosystem/bridges)
###### Rate this page

😞😐😊

* [Stablecoins on Flow](#stablecoins-on-flow)
  + [Step-by-step example USDC to Flow](#step-by-step-example-usdc-to-flow)
* [Stargate and LayerZero on Flow](#stargate-and-layerzero-on-flow)
* [Support and Additional Resources](#support-and-additional-resources)
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

