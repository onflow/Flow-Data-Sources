# Source: https://docs.wallet.flow.com/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy

Privy | Flow Wallet

[![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)

Flow Wallet](/)

`Ctrl``K`

* [👋Welcome to Flow Wallet](/)
* Ecosystem Primers

  + [⭐Flow Reference Wallet Primer](/ecosystem-primers/flow-reference-wallet-primer)
* FAQ

  + [❓FAQ](/faq/faq)
* Features

  + [⛓️Account Linking](/features/account-linking)
  + [🔌WalletConnect](/features/walletconnect)
  + [📖Human Readable Transactions](/features/human-readable-transactions)
  + [💚Flow Client Library (FCL)](/features/flow-client-library-fcl)
  + [🔓Secure Enclave](/features/secure-enclave)
  + [🦺Account Recovery](/features/account-recovery)
* Ecosystem Development

  + [🛠️Ecosystem Developer Grants](/ecosystem-development/ecosystem-developer-grants)
  + [🔌Integrate Flow EVM with Web3 SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks)

    - [Wagmi](/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi)
    - [Rainbowkit](/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit)
    - [Etherjs](/ecosystem-development/integrate-flow-evm-with-web3-sdks/etherjs)
    - [Web3js](/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3js)
    - [Viem](/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem)
    - [Web3-Onboard](/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard)
    - [MIPD](/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd)
    - [Others SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks/others-sdks)
    - [Privy](/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy)
* Download

  + [📲Download](/download/download)
* Open Source

  + [💽Open Source](/open-source/open-source)
* Tutorial

  + [🔐Mobile Wallet Backup Guide](/tutorial/mobile-wallet-backup-guide)
  + [💸Move Assets between Flow and EVM](/tutorial/move-assets-between-flow-and-evm)
  + [📱Mobile Wallet Restore Guide](/tutorial/mobile-wallet-restore-guide)
  + [💻Extension Wallet Backup Guide](/tutorial/extension-wallet-backup-guide)
  + [🖥️Extension Wallet Restore Guide](/tutorial/extension-wallet-restore-guide)
  + [🔁Extension Update Guide](/tutorial/extension-update-guide)
  + [🪙FLOW wallet init token guide](/tutorial/flow-wallet-init-token-guide)
  + [💾Extension Private Key and Seed Phrase Guide](/tutorial/extension-private-key-and-seed-phrase-guide)
  + [⛵Mobile Wallet Export Log Guide](/tutorial/mobile-wallet-export-log-guide)
* [🔐Wallet Revoke key guide](/wallet-revoke-key-guide)

[Powered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=Cqw72ZIu4wNI7q40hHbt)

On this page

* [1. Enable Smart Wallet](#id-1.-enable-smart-wallet)
* [2. Add Custom EVM Chains (Flow EVM)](#id-2.-add-custom-evm-chains-flow-evm)
* [✅ Verify the Configuration](#verify-the-configuration)

Copy

1. [Ecosystem Development](/ecosystem-development)
2. [🔌Integrate Flow EVM with Web3 SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks)

# Privy

🛠️ Guide to Configuring Privy with Flow Wallet (EVM Support)

---

#### 📌 Prerequisites

* Registered and logged into the [Privy Dashboard](https://www.privy.io/dashboard)
* Your project has Smart Wallet enabled

---

### 1. Enable Smart Wallet

1. Log into the [Privy Dashboard](https://www.privy.io/dashboard)
2. Open your project page
3. In the left-hand menu, click on `Smart Wallet`
4. Click the `Enable Smart Wallet` button (if not already enabled)

---

### 2. Add Custom EVM Chains (Flow EVM)

Once Smart Wallet is enabled, you can add the Flow mainnet or testnet EVM chain.

#### ✳️ Add Flow EVM Mainnet

1. In the Smart Wallet settings, click `Add New Chain`
2. Fill in the following information:

Field

Value

Name

Flow

Chain ID

747

RPC URL

[https://mainnet.evm.nodes.onflow.org](https://mainnet.evm.nodes.onflow.org/)

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FVClVdzznxpio2udliqBp%252Fimage.png%3Falt%3Dmedia%26token%3D81dfdc0d-f6dd-4dc2-9646-b548c999df71&width=768&dpr=4&quality=100&sign=2e5a1921&sv=2)

---

#### 🧪 Add Flow EVM Testnet

1. Click `Add New Chain` again
2. Enter the following details:

Field

Value

Name

Flow Testnet

Description

The public RPC URL for Flow Testnet

Chain ID

545

RPC URL

[https://testnet.evm.nodes.onflow.org](https://testnet.evm.nodes.onflow.org/)

> 💡 The testnet is recommended for development and integration testing.

---

### ✅ Verify the Configuration

After saving, you should see `Flow` and/or `Flow Testnet` listed under your configured chains in Smart Wallet. Privy will automatically assign smart wallet addresses that are compatible with the specified EVM chains.

You can now use Privy’s SDK in your dApp frontend to connect wallets, sign transactions, and interact with contracts on Flow EVM.

---

[PreviousOthers SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks/others-sdks)[NextDownload](/download/download)

Last updated 24 days ago