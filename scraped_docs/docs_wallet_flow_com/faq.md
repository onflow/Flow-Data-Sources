# Source: https://docs.wallet.flow.com/faq

FAQ | Flow Wallet

[![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)

Flow Wallet](/)

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

Copy

1. [FAQ](/faq)

# ❓FAQ

Answers to common questions about Flow Wallet

[PreviousFlow Reference Wallet Primer](/ecosystem-primers/flow-reference-wallet-primer)[NextAccount Linking](/features/account-linking)

Last updated 11 months ago

`Ctrl``K`

#### Is Flow Wallet a Self-Custody or Custodial Wallet?

Flow Wallet is self-custodial. Users own and control the cryptographic keys securing their Flow accounts and assets.

Chrome extension:

* Secured by a 12-word seed phrase
* Users are responsible for safeguarding their seed phrase
* Loss of seed phrase results in permanent account loss

iOS and Android:

* Utilizes device's Secure Enclave for account security
* No seed phrase required
* Multi-Backup feature available for account recovery
* Create Multi-Backup: Settings > Backup > Create Multi-Backup

#### Where is my Seed Phrase? I can't find it on Flow Wallet iOS or Android.

Flow Wallet on iOS and Android doesn't use seed phrases. Instead, it leverages your device's Secure Enclave for account security. To ensure account recovery:

1. Create a Multi-Backup
2. Navigate to Settings > Backup > Create Multi-Backup

#### What is Multi-Backup?

Multi-Backup is a security feature for Flow Wallet on iOS and Android:

* Creates multiple partial-weight keys (500 weight each)
* Stores keys across selected platforms: iCloud, Google Drive, or Seed Phrase
* Works in conjunction with your device's primary account key
* Enables account recovery if you lose access to your device

This is the multi-backup recovery process:

1. Install Flow Wallet on a new device
2. Initiate account recovery
3. Flow Wallet accesses multi-backup providers
4. Retrieves recovery keys
5. Adds new device's Secure Enclave key
6. Restores access to your account

Create a Multi-Backup on Flow Wallet iOS and Android

* Navigate to Settings > Backup > Create Multi-Backup