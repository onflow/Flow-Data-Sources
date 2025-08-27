# Source: https://docs.wallet.flow.com/tutorial/mobile-wallet-backup-guide

Mobile Wallet Backup Guide | Flow Wallet

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

Copy

1. [Tutorial](/tutorial)

# 🔐Mobile Wallet Backup Guide

Welcome to the Flow Mobile Wallet! Our wallet is designed to provide a secure and user-friendly experience for managing your digital assets. One of the standout features of the Flow Mobile Wallet is its robust backup options, ensuring that your funds remain safe and accessible.

#### Device Backup

Designed with your security in mind, our mobile wallet utilizes secure enclave technology to ensure that your account is created and managed safely. With this cutting-edge approach, no private keys are accessible by the wallet team, giving you complete control over your digital assets.

With the Flow Mobile Wallet, you can easily back up your entire wallet on your device. When you register or log into your profile on your device, your profile will be automatically backed up on your device. And you can scan the QR code shown by the Flow Wallet to sync your wallet between your device. [Restore guideline link]

And you can view your device backup details in Backup section in Profile page.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F5esT2O1478c5P2H6eZVq%252FIMG_7129.jpg%3Falt%3Dmedia%26token%3D80e50f78-9678-4cb8-a8a8-bbc8dcac45f1&width=768&dpr=4&quality=100&sign=1ab40502&sv=2)

#### Multi-Backup

For added flexibility, the Flow Mobile Wallet supports multi-backup options. Users can create multiple backups across different devices or cloud services, ensuring that you always have access to your wallet.

A multi-backup stores multiple partial-weight keys across your accounts on trusted providers like Google Drive and iCloud(only in IOS), or a Recovery Phrase.

Two partial-weight keys must be used together to recover access to your account. Each key individually cannot be used. This means, that to recover access to your account, Flow Wallet requires access to two of your backups.

Your backups are encrypted using your wallet PIN code. You must remember or write down your PIN code and store it in a safe place.

**Step 1:** Navigate to the **Profile** page and select the **Backup** section.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FziahUrIfI1c7cJbZCtlK%252FIMG_7114.PNG%3Falt%3Dmedia%26token%3D851bcad1-508c-4333-a791-7012ac187de3&width=768&dpr=4&quality=100&sign=9e649d9f&sv=2)

**Step 2:** Choose 'Create Multi-Backup'.

**Step 3:** Select at least two types of backup options to ensure your assets are protected.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252Fj4Jwk8BWXScYthdxwTBJ%252FIMG_7134.jpg%3Falt%3Dmedia%26token%3D09fca22d-404a-4389-877e-c816712382f9&width=768&dpr=4&quality=100&sign=9bd1e9d4&sv=2)

**Step 4:** If prompted, create a new PIN or verify your existing PIN to proceed with the backup process.

**Step 5:** Follow the prompts to initiate the backup process in Google Drive.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FiYxpdqPtrc7O2yEOaq2U%252FRPReplay_Final1727930714%2520%255BMConverter.eu%255D.webp%3Falt%3Dmedia%26token%3Db7489970-bff0-4674-8a11-38b162d99118&width=768&dpr=4&quality=100&sign=ac7edf17&sv=2)

**Step 6:** Create a backup in iCloud by following the on-screen instructions.

**Step 7:** Carefully read all information regarding the recovery phrase backup. Once you understand the instructions, tick the checkbox to acknowledge.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F6vidVJBEK05H3xTBv2pE%252FIMG_7126.PNG%3Falt%3Dmedia%26token%3Dfecc31f6-c6fd-451f-9d97-3b0e72079660&width=768&dpr=4&quality=100&sign=3b18d129&sv=2)

**Step 8:** Copy your seed phrase and store it securely.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FVZqJWfKwNlI68Nw10CNv%252FIMG_7127.PNG%3Falt%3Dmedia%26token%3D88f6bdbc-4068-4ef4-84c5-2604c0c78ede&width=768&dpr=4&quality=100&sign=27e82e63&sv=2)

**Step 9:** Click the **Next** button. On the confirmation page, review your backups and ensure everything is in order.

#### Seed Phrase Backup

Creating a seed phrase is a traditional method for securing your digital assets. Unlike secure enclave methods, which rely on hardware-level security, a seed phrase provides a straightforward way to restore and access your wallet across devices. This guide will walk you through the process of creating a full access seed phrase in the Flow Wallet.

**Step 1:** Navigate to the **Profile** page and select the **Backup** section.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FziahUrIfI1c7cJbZCtlK%252FIMG_7114.PNG%3Falt%3Dmedia%26token%3D851bcad1-508c-4333-a791-7012ac187de3&width=768&dpr=4&quality=100&sign=9e649d9f&sv=2)

**Step 2:** Choose 'Create Recovery Phrase Backup'.

**Step 3:** Carefully read all information regarding the recovery phrase backup. Once you understand the instructions, tick the checkbox to acknowledge.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F7mHoAtpbr9Ndvz4Pz7V6%252FIMG_7131.PNG%3Falt%3Dmedia%26token%3Dfdd74af0-79e3-4995-b946-545d0350a00d&width=768&dpr=4&quality=100&sign=5c817262&sv=2)

**Step 4:** Copy your seed phrase and store it securely.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FhdDWZQPjpCb3uKrDsM2I%252FIMG_7132.PNG%3Falt%3Dmedia%26token%3Df8a82fd4-84c7-4c3e-bb3a-67956a3938ee&width=768&dpr=4&quality=100&sign=b2bfcd2e&sv=2)

**Step 5:** Click the **Next** button. On the confirmation page, review your seed phrase backup and ensure everything is in order.

### Support

If you encounter any issues or have further questions, please reach out to our support team at [[email protected]](/cdn-cgi/l/email-protection).

[PreviousOpen Source](/open-source/open-source)[NextMove Assets between Flow and EVM](/tutorial/move-assets-between-flow-and-evm)

Last updated 10 months ago