# Source: https://docs.wallet.flow.com/tutorial/extension-wallet-backup-guide

Extension Wallet Backup Guide | Flow Wallet

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

1. [Tutorial](/tutorial)

# 💻Extension Wallet Backup Guide

[PreviousMobile Wallet Restore Guide](/tutorial/mobile-wallet-restore-guide)[NextExtension Wallet Restore Guide](/tutorial/extension-wallet-restore-guide)

Last updated 10 months ago

`Ctrl``K`

Backing up your Flow Wallet Extension is crucial for ensuring the safety and accessibility of your digital assets. This guide will cover three essential methods for backing up your wallet.Introduction to Account Backup. These methods only used for accounts created in FLOW Wallet Extension.

To ensure the security and accessibility of your account, it’s essential to have a reliable backup plan. We recommend choosing at least two of the following methods to back up your account. This will provide you with multiple layers of protection, giving you peace of mind that your assets are safe and can be easily recovered if needed.

* **Private Key**: Your private key is a unique string of characters that grants access to your wallet. Safeguarding this key is vital, as it allows you to recover your funds in case you lose access to your wallet. Always store your private key in a secure location, and never share it with anyone. You can find your private key under **Settings** → **Account List** → **Main Account** → **Private Key**. Copy your Private key and store it securely.

* **Recovery Phrases**: Also known as seed phrases, recovery phrases consist of a series of words that can be used to restore your wallet. In case of device loss or failure, these phrases are your lifeline to accessing your funds. Make sure to write down your 12 words recovery phrases and keep them in a secure place. You can find your private key under **Settings** → **Account List** → **Main Account** → **Recovery phrases**.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252Fw8LwTi8BuaLJOuWZFOCB%252FScreen%2520Shot%25202024-10-09%2520at%252011.27.48%2520am.png%3Falt%3Dmedia%26token%3Da8857540-1e4c-44bc-b8da-c50f0742bb4b&width=768&dpr=4&quality=100&sign=7b74d0ec&sv=2)

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F8xQPCWMiXU77AQDz02Pz%252FScreen%2520Shot%25202024-10-09%2520at%252011.28.14%2520am.png%3Falt%3Dmedia%26token%3Dd7ff7fae-217e-433f-b3b3-2756e744f4a8&width=768&dpr=4&quality=100&sign=297dbaf4&sv=2)

* **Google Backup**: Utilizing Google Backup can provide an additional layer of security. By linking your wallet to your Google account, you can securely store essential data and recover your wallet more easily if needed.

You can back up in your Google Drive in two ways:

1. When you are registering or importing your account, click on **Connect and Backup** in the step shown in the image to back up your account.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FFn3v639tFiWRmFgBPNYI%252FScreen%2520Shot%25202024-10-09%2520at%252011.19.25%2520am.png%3Falt%3Dmedia%26token%3Da167938a-7510-4d3e-a87e-d64f1b1c4db1&width=768&dpr=4&quality=100&sign=d5c5812d&sv=2)

1. After logging in, go to the **Settings** page → **Backup**, and click the **Sync** button.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252Fusgk1H5j6euW6ZqPy5Oh%252FScreen%2520Shot%25202024-10-09%2520at%252011.21.11%2520am.png%3Falt%3Dmedia%26token%3D2b9902bc-75b9-4f64-b84e-41169397875e&width=768&dpr=4&quality=100&sign=9ed7d9cb&sv=2)

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FYatn1COkDuuncpK9yl0b%252FScreen%2520Shot%25202024-10-09%2520at%252011.21.36%2520am.png%3Falt%3Dmedia%26token%3Dec2ac349-fa25-4b2f-9c1c-bdc803cec922&width=768&dpr=4&quality=100&sign=c526f823&sv=2)

After you’ve completed all the above steps, you’ll find that the backup has been successfully add in your FLOW wallet. This means you’re now ready to restore your account as needed!

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252Fe5gWCJwJcU8diUyqUINY%252FScreen%2520Shot%25202024-10-21%2520at%252011.54.26%2520am.png%3Falt%3Dmedia%26token%3Dc6ebd055-17ac-4a1c-a14c-c866a7b8b0de&width=768&dpr=4&quality=100&sign=8278041b&sv=2)

### Support

If you encounter any issues or have further questions, please reach out to our support team at [[email protected]](/cdn-cgi/l/email-protection)