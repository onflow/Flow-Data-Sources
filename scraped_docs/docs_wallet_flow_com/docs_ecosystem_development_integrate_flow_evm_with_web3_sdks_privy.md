# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy

🔐 Privy

[![Flow Wallet](/assets/logo.png?dpl=dpl_CvQvGN9652mUUTFzXgb4u7nfv4PK)Flow Wallet](/)

[![Flow Wallet](/assets/logo.png?dpl=dpl_CvQvGN9652mUUTFzXgb4u7nfv4PK)Flow Wallet](/)

Search

`⌘``K`

[👋 Welcome to Flow Wallet](/docs)

Ecosystem Primers

[📘 Flow Reference Wallet Primer](/docs/flow-reference-wallet-primer)

FAQ

[❓ FAQ](/docs/faq)

Features

Features

Ecosystem Development

Ecosystem Development

[🛠 Ecosystem Developer Grants](/docs/ecosystem-development/ecosystem-developer-grants)

Integrate Flow EVM with Web3 SDKs

[🔌 Integrate Flow EVM with Web3 SDKs](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks)[🪝 Wagmi](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi)[🌈 Rainbowkit](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit)[⚙️ Ethers.js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/etherjs)[🌐 Web3.js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3js)[⚡ Viem](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem)[🚀 Web3-Onboard](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard)[🔍 MIPD](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd)[🧰 Other SDKs](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/others-sdks)[🔐 Privy](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy)

Download

[📲 Download](/docs/download)

Open Source

[💽 Open Source](/docs/open-source)

Tutorial

Tutorial

AI Integration

[🤖 AI Integration](/docs/ai-integration)

Other

[🔐 Wallet Revoke key guide](/docs/wallet-revoke-key-guide)

🔐 Privy

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🔐 Privy

Guide to Configuring Privy with Flow Wallet (EVM Support)

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy.mdx)

# [Privy](#privy)

---

#### [📌 Prerequisites](#-prerequisites)

* Registered and logged into the [Privy Dashboard](https://www.privy.io/dashboard)
* Your project has Smart Wallet enabled

---

### [1. Enable Smart Wallet](#1-enable-smart-wallet)

1. Log into the [Privy Dashboard](https://www.privy.io/dashboard)
2. Open your project page
3. In the left-hand menu, click on `Smart Wallet`
4. Click the `Enable Smart Wallet` button (if not already enabled)

---

### [2. Add Custom EVM Chains (Flow EVM)](#2-add-custom-evm-chains-flow-evm)

Once Smart Wallet is enabled, you can add the Flow mainnet or testnet EVM chain.

#### [✳️ Add Flow EVM Mainnet](#️-add-flow-evm-mainnet)

1. In the Smart Wallet settings, click `Add New Chain`
2. Fill in the following information:

| Field | Value |
| --- | --- |
| Name | Flow |
| Chain ID | 747 |
| RPC URL | [https://mainnet.evm.nodes.onflow.org](https://mainnet.evm.nodes.onflow.org/) |

![](..//assets/image.png)



---

#### [🧪 Add Flow EVM Testnet](#-add-flow-evm-testnet)

1. Click `Add New Chain` again
2. Enter the following details:

| Field | Value |
| --- | --- |
| Name | Flow Testnet |
| Description | The public RPC URL for Flow Testnet |
| Chain ID | 545 |
| RPC URL | [https://testnet.evm.nodes.onflow.org](https://testnet.evm.nodes.onflow.org/) |

> 💡 The testnet is recommended for development and integration testing.

---

### [✅ Verify the Configuration](#-verify-the-configuration)

After saving, you should see `Flow` and/or `Flow Testnet` listed under your configured chains in Smart Wallet. Privy will automatically assign smart wallet addresses that are compatible with the specified EVM chains.

You can now use Privy’s SDK in your dApp frontend to connect wallets, sign transactions, and interact with contracts on Flow EVM.

---

[🧰 Other SDKs

Previous Page](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/others-sdks)[📲 Download

Next Page](/docs/download)

### On this page

[Privy](#privy)[📌 Prerequisites](#-prerequisites)[1. Enable Smart Wallet](#1-enable-smart-wallet)[2. Add Custom EVM Chains (Flow EVM)](#2-add-custom-evm-chains-flow-evm)[✳️ Add Flow EVM Mainnet](#️-add-flow-evm-mainnet)[🧪 Add Flow EVM Testnet](#-add-flow-evm-testnet)[✅ Verify the Configuration](#-verify-the-configuration)