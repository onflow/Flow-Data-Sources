# Source: https://developers.flow.com/evm/quickstart

EVM Quickstart | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Network Information](/evm/networks)
* [EVM Quickstart](/evm/quickstart)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)

* EVM Quickstart

On this page

# EVM Quickstart

Flow EVM is an EVM-equivalent blockchain that combines the advantages of Flow, including security, low-cost gas, and native VRF with compatibility with exiting blockchain applications tools, and contracts. If it works on another EVM-equivalent blockchain, it should work on Flow EVM!

This guide is a self-contained quickstart that will walk you through deploying a contract on Flow EVM testnet with [Hardhat](https://hardhat.org/) and testing it with [testnet Flowscan](https://evm-testnet.flowscan.io/).

If you prefer, check out our tutorials for [Remix](/evm/guides/remix) and [Foundry](/evm/guides/foundry) for information on how to deploy a contract with those platforms.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Fund a wallet with testnet tokens from the [Flow Faucet](https://faucet.flow.com/fund-account)
* Deploy a contract on Flow EVM Testnet
* Interact with a contract using [Flowscan](https://evm-testnet.flowscan.io/)
* Utilize automatically sponsored gas with the [Flow Wallet](https://wallet.flow.com/) on testnet **and mainnet**

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Traditional Cryptocurrency Wallet[​](#traditional-cryptocurrency-wallet "Direct link to Traditional Cryptocurrency Wallet")

EVM [Accounts](/evm/accounts) created by the Flow wallet have unique properties that allow for powerful features, but they do **not** have recovery phrases or private keys that can be exported in a way that's compatible with [Hardhat](https://hardhat.org/). As a result, you'll need to use a traditional EOA and [MetaMask](https://metamask.io), or the wallet of your choice, to deploy your contracts.

## Deploy Your Contract[​](#deploy-your-contract "Direct link to Deploy Your Contract")

For this exercise, we'll use a [Button Clicker Contract](https://github.com/briandoyle81/button-clicker-contract/blob/main/contracts/ClickToken.sol) that's relatively simple, but includes several [OpenZeppelin](https://www.openzeppelin.com/) contracts. This way, we can walk through the process to configure your project to use these common imports.

info

If you **really** want to speedrun this tutorial, fork the [Button Clicker Contract](https://github.com/briandoyle81/button-clicker-contract/blob/main/contracts/ClickToken.sol) repo, run `npm install`, add a `.env` with your deploy wallet key as `DEPLOY_WALLET_1`, and deploy with `npx hardhat ignition deploy ./ignition/modules/ClickToken.ts --network flowTestnet`.

Then skip to the frontend section.

### Hardhat Setup[​](#hardhat-setup "Direct link to Hardhat Setup")

Open a terminal window and navigate either to the folder where you wish to create your project folder, or an empty project folder. Run:

`_10

npx hardhat init`

![Hardhat Init](/assets/images/hardhat-init-4b18bd4d51ccfaa9c1758dca1b640ee9.png)

Select `Create a TypeScript project (with Viem)`

Enter `.` if you ran the command from an empty folder, or enter a path.

Choose the defaults for the remaining options, then open the project in your editor.

### Environment Setup[​](#environment-setup "Direct link to Environment Setup")

Add a `.env` and in it, add an environment variable called `DEPLOY_WALLET_1` with your deployment wallet's [private key](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/).

`_10

DEPLOY_WALLET_1=<YOUR_PRIVATE_KEY>`

danger

The [private key](https://support.metamask.io/configure/accounts/how-to-export-an-accounts-private-key/) functions the same as the recovery phrase for a wallet. Anyone with the key can drain the wallet at any time! Use separate wallets for development and never commit a key to a repo.

### Hardhat Config[​](#hardhat-config "Direct link to Hardhat Config")

We'll be using [OpenZeppelin Contracts](https://www.openzeppelin.com/contracts), so install them, then open the project in your editor:

`_10

npm install --save-dev @openzeppelin/hardhat-upgrades

_10

npm install --save-dev @nomicfoundation/hardhat-ethers ethers # peer dependencies`

Then install the contracts themselves:

`_10

npm install --save-dev @openzeppelin/contracts`

You'll also need `dotenv` to better protect your wallet key, so go ahead and add that too:

`_10

npm install dotenv`

Open `hardhat.config`. Below the imports, add the `require` statements for the contracts and `dotenv`:

`_10

require('@openzeppelin/hardhat-upgrades');

_10

require('dotenv').config();`

The default config is pretty bare. We'll need to add quite a few items. We'll do these one at a time, then provide a complete copy at the end.

First, add a `networks` property containing the network information for Flow Testnet and Mainnet:

`_10

networks: {

_10

flow: {

_10

url: 'https://mainnet.evm.nodes.onflow.org',

_10

accounts: [process.env.DEPLOY_WALLET_1 as string],

_10

},

_10

flowTestnet: {

_10

url: 'https://testnet.evm.nodes.onflow.org',

_10

accounts: [process.env.DEPLOY_WALLET_1 as string],

_10

},

_10

},`

Then, add an entry for `etherscan`:

`_10

etherscan: {

_10

}`

In it, add a property for `apiKey` and add keys for Flow Mainnet and Testnet. Note that the Etherscan API requires this to be here, but at the time of writing, API keys aren't actually needed. Any text can be used:

`_10

apiKey: {

_10

// Is not required by blockscout. Can be any non-empty string

_10

'flow': "abc",

_10

'flowTestnet': "abc"

_10

},`

Next, add `customChains` and the network information for Flow:

`_18

customChains: [

_18

{

_18

network: 'flow',

_18

chainId: 747,

_18

urls: {

_18

apiURL: 'https://evm.flowscan.io/api',

_18

browserURL: 'https://evm.flowscan.io/',

_18

},

_18

},

_18

{

_18

network: 'flowTestnet',

_18

chainId: 545,

_18

urls: {

_18

apiURL: 'https://evm-testnet.flowscan.io/api',

_18

browserURL: 'https://evm-testnet.flowscan.io/',

_18

},

_18

},

_18

];`

You should end up with:

`_46

import type { HardhatUserConfig } from 'hardhat/config';

_46

import '@nomicfoundation/hardhat-toolbox-viem';

_46

_46

require('@openzeppelin/hardhat-upgrades');

_46

require('dotenv').config();

_46

_46

const config: HardhatUserConfig = {

_46

solidity: '0.8.28',

_46

networks: {

_46

flow: {

_46

url: 'https://mainnet.evm.nodes.onflow.org',

_46

accounts: [process.env.DEPLOY_WALLET_1 as string],

_46

},

_46

flowTestnet: {

_46

url: 'https://testnet.evm.nodes.onflow.org',

_46

accounts: [process.env.DEPLOY_WALLET_1 as string],

_46

},

_46

},

_46

etherscan: {

_46

apiKey: {

_46

// Is not required by blockscout. Can be any non-empty string

_46

flow: 'abc',

_46

flowTestnet: 'abc',

_46

},

_46

customChains: [

_46

{

_46

network: 'flow',

_46

chainId: 747,

_46

urls: {

_46

apiURL: 'https://evm.flowscan.io/api',

_46

browserURL: 'https://evm.flowscan.io/',

_46

},

_46

},

_46

{

_46

network: 'flowTestnet',

_46

chainId: 545,

_46

urls: {

_46

apiURL: 'https://evm-testnet.flowscan.io/api',

_46

browserURL: 'https://evm-testnet.flowscan.io/',

_46

},

_46

},

_46

],

_46

},

_46

};

_46

_46

export default config;`

### Contract Setup[​](#contract-setup "Direct link to Contract Setup")

Delete `Lock.sol` and add `ClickToken.sol`. In it add, the [Button Clicker Contract](https://github.com/briandoyle81/button-clicker-contract/blob/main/contracts/ClickToken.sol).

warning

Hardhat only installs the most current version of Solidity. `^0.8.27` means that this contract requires 0.8.27 or **higher**. You generally **don't** want to include the `^` in your contracts unless you have a specific reason for doing so.

We won't go into the details of the contract for this tutorial. It's a relatively simple [ERC-20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) implementation that mints one token any time the `mintTo` function is called. Perfect for a Button Clicker game!

### Deployment Setup[​](#deployment-setup "Direct link to Deployment Setup")

Delete `Lock.ts` from the `ignition/modules` folder, and add `ClickToken.ts`. In it, add:

`_12

// This setup uses Hardhat Ignition to manage smart contract deployments.

_12

// Learn more about it at https://hardhat.org/ignition

_12

_12

import { buildModule } from '@nomicfoundation/hardhat-ignition/modules';

_12

_12

const ClickerModule = buildModule('ClickTokenModule', (m) => {

_12

const clickToken = m.contract('ClickToken');

_12

_12

return { clickToken };

_12

});

_12

_12

export default ClickerModule;`

### Obtain Testnet Funds[​](#obtain-testnet-funds "Direct link to Obtain Testnet Funds")

Visit the [Flow Faucet](https://faucet.flow.com/fund-account) and follow the instructions to add testnet funds. Compared to other networks, the [Flow Faucet](https://faucet.flow.com/fund-account) grants a vast amount of tokens - enough gas for millions of transactions.

### Deploy the Contract[​](#deploy-the-contract "Direct link to Deploy the Contract")

Deploy the contract with:

`_10

npx hardhat ignition deploy ./ignition/modules/ClickToken.ts --network flowTestnet`

You should see something similar to:

`_13

✔ Confirm deploy to network flowTestnet (545)? … yes

_13

Hardhat Ignition 🚀

_13

_13

Deploying [ ClickTokenModule ]

_13

_13

Batch #1

_13

Executed ClickTokenModule#ClickToken

_13

_13

[ ClickTokenModule ] successfully deployed 🚀

_13

_13

Deployed Addresses

_13

_13

ClickTokenModule#ClickToken - 0x5Ff8221DfDD1F82fd538391D231502B4b927fbD7`

### Verify the Contract[​](#verify-the-contract "Direct link to Verify the Contract")

Next, verify the contract with:

`_10

hardhat ignition verify chain-545 --include-unrelated-contracts`

You'll see something similar to:

`_10

briandoyle@Mac button-clicker-contract % npx hardhat ignition verify chain-545 --include-unrelated-contracts

_10

Verifying contract "contracts/ClickToken.sol:ClickToken" for network flowTestnet...

_10

Successfully verified contract "contracts/ClickToken.sol:ClickToken" for network flowTestnet:

_10

- https://evm-testnet.flowscan.io//address/0x64366c923d5046F8417Dcd8a0Cb4a789F8722387#code`

## Testing the Contract[​](#testing-the-contract "Direct link to Testing the Contract")

Click the link to open the contract in [testnet Flowscan](https://evm-testnet.flowscan.io/). Click the `Connect` button and connect your wallet, then navigate to the `Contract` tab and `Read/Write contract`.

![read write contract](/assets/images/read-write-dd09b9394736ff453da4292fc6e9b5fd.png)

Find the `mintTo` function and expand the UI to mint yourself a few tokens. You can click the `self` button to automatically add your address without needing to copy/paste.

Once you've "earned" a few tokens, use `balanceOf` to see how many tokens you have. You can also use `getAllScores` to get a list of everyone with the tokens, and how many they have.

### Testing with Free Gas[​](#testing-with-free-gas "Direct link to Testing with Free Gas")

If you don't have it yet, set up the [Flow Wallet](https://wallet.flow.com/), connect, and try minting some more tokens. You'll see that the wallet automatically sponsors your gas:

![flow-wallet](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAVUAAAAzCAYAAAAn1pvdAAABWWlDQ1BJQ0MgUHJvZmlsZQAAKJF1kM1LAlEUxc+Ug1BSLaJNLWbTorCQKXXtB5ggMU2F6e45mgZ+PMaJaNcfEf0J0b6FBAbSukUgVLQKWrWOhCh53ZmpRosuXO6Pw7mP8y4wEmCcV30AanXL1FNxZSeXV/zP8EFCAFHMMqPJY5qWIQu+53D1bslL1V2y31pPqvm0LHLn953LiTf56a9/qMaKpaZB84NaNbhpAVKIWDuwuM1HxNMmhSI+trns8pnNBZfbjmdLTxDfEE8ZFVYkfiQOFgb08gDXqvvGVwY7faBU396kOUM9hwxSULCGJHSaWWw4jH92Vp2dBBrgOISJPZRRgUWbMVI4qigRp1GHgWUEiVWEqMP2rX/f0NMai0DkleDK0xj96SJKMSOeNn8NTHaBdpgzk/1cVur5mrsrqsvjLUA+EeIlC/gXgP6dEO8tIfqnwOgD0Ol9Av7gZDqIM1gUAAAAVmVYSWZNTQAqAAAACAABh2kABAAAAAEAAAAaAAAAAAADkoYABwAAABIAAABEoAIABAAAAAEAAAFVoAMABAAAAAEAAAAzAAAAAEFTQ0lJAAAAU2NyZWVuc2hvdHXl4tYAAAHVaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA2LjAuMCI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjUxPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjM0MTwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlVzZXJDb21tZW50PlNjcmVlbnNob3Q8L2V4aWY6VXNlckNvbW1lbnQ+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgol240pAAAWGUlEQVR4Ae2dd5AUxRfH3+0dgqhgACPoIWBWMAuSzYjZMgFqqX9YJoxlKhT1p5jAiDmCmMAyYg6gBLNgzoKYxawIHnf85tOzb7Z3bnZ39u5AKN+r2p3p6deve74z8+3XYXoqOnbsuLCiokIWLlwoKhY2POx+sOfB+CBEoGw+7NSpU+7uURRtawgYAoaAIdAgBKrwSMpmYvNszbO3lk30wNnzYy27vJYdzf/o7rAdQ8AQMAQMgUYhkGlUaktsCBgChoAhkIeAkWoeHBYwBAwBQ6BxCBipNg4/S20IGAKGQB4CVXmhWCCTycj6668vlZWVsZgwuPLKK8vrr78uc+fOTYy3g4aAIWAI/NcQKEiqwVQrOe+886RFixaywgorJOLy888/C8Q7fvx4uf/++xN17KAhYAgYAv8lBBJJddVVV5Vhw4bJxIkT5bPPPiuKRzB7QPbcc095//335d133y2qa5GGgCFgCCwRCDTLyIL+HaWuR3up69LWFSkz40fJTJktVRM+F6mpbXAxE0l1n332kd9//90R6g477CBrrrmmLLfccnmZ/PXXX/LNN9/Ic889J127dpXu3bsvVaS6/PLLC+fgzy/LO8ESATz42tpaqampKaGZLnrZZZeVv//+O52yaRkChkCDEVgwcGOpOX7Leulre7YTfjVndJNm17whVWPfq6eT5kDiQNUyyywj//zzj2yxxRbSt29f12f6448/iv+jH5U4dCCW5s2bF83v4IMPlrffftv98GjfeeedKExXw4YbbijvvfeezJgxw/0ef/xxOeWUU1z3gm944403dnqHHnqofzhKP3DgwLzje++9t9x6663RsT59+sjTTz8tTz31lEybNk1OP/10qarKr1sK5YGRrbbaSu644w558cUX5bXXXpNRo0bJ6quv7uynOcfJkydHZWHngAMOkAceeECmTJniynTiiSfmnfO1114rL7zwgkC6vjzzzDMOe/8Y+4qjYq3blVZaqWAclSbyyiuvRNdE09EKMVlyEOA+YCwjraTRL6WDA7LiiiumzTLSYyxm8803T502jX4anagACTv/XLljIqHGVSHd+SN3iB9OFa4Spv5XiPPYeDPE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)

Even better, the [Flow Wallet](https://wallet.flow.com/) is currently **sponsoring transactions on mainnet** too!

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to:

* Fund a wallet with testnet tokens from the [Flow Faucet](https://faucet.flow.com/fund-account)
* Deploy a contract on Flow EVM Testnet using Hardhat
* Interact with a contract using [Flowscan](https://evm-testnet.flowscan.io/)
* Utilize automatically sponsored gas with the [Flow Wallet](https://wallet.flow.com/) on testnet and mainnet

You've now mastered the basics of deploying and interacting with EVM contracts on Flow. But this is just the beginning! Flow EVM's true power lies in its ability to combine the best of both worlds: EVM compatibility with Flow's native features.

In our [Cross-VM Apps](/tutorials/cross-vm-apps/introduction) tutorial series, you'll learn how to supercharge your EVM applications by integrating them with Flow Cadence. You'll discover how to:

* Build hybrid applications that seamlessly connect to both Flow EVM and Flow Cadence
* Use Cadence's powerful features to enhance your EVM contracts
* Enable multi-call contract writes with a single signature
* Take advantage of Flow's native features like VRF and sponsored transactions

Ready to unlock the full potential of Flow EVM? Start with our [Batched Transactions](/tutorials/cross-vm-apps/introduction) tutorial to learn how to build your first cross-VM application.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/quickstart.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

Network Information](/evm/networks)[Next

Fees](/evm/fees)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
  + [Traditional Cryptocurrency Wallet](#traditional-cryptocurrency-wallet)
* [Deploy Your Contract](#deploy-your-contract)
  + [Hardhat Setup](#hardhat-setup)
  + [Environment Setup](#environment-setup)
  + [Hardhat Config](#hardhat-config)
  + [Contract Setup](#contract-setup)
  + [Deployment Setup](#deployment-setup)
  + [Obtain Testnet Funds](#obtain-testnet-funds)
  + [Deploy the Contract](#deploy-the-contract)
  + [Verify the Contract](#verify-the-contract)
* [Testing the Contract](#testing-the-contract)
  + [Testing with Free Gas](#testing-with-free-gas)
* [Conclusion](#conclusion)

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
* [Flowscan Mainnet](https://flowscan.io/)
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