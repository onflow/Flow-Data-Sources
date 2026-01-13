# Source: https://docs.wallet.flow.com/features

Account Linking | Flow Wallet

bars[![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)

Flow Wallet](/)

search

circle-xmark

`Ctrl``k`

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
  + [🔌Integrate Flow EVM with Web3 SDKschevron-right](/ecosystem-development/integrate-flow-evm-with-web3-sdks)
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

[gitbookPowered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=Cqw72ZIu4wNI7q40hHbt)

block-quoteOn this pagechevron-down

copyCopychevron-down

1. [Features](/features)

# ⛓️Account Linking

Flow Reference Wallet supports Account Linking, which is uniquely supported by Flow's account abstraction, which enables accounts to be linked together to create an association between them.
**Background**One of the major hindrances to Web3 adoption is often the requirement for users to sign up for a wallet provider. This step during user onboarding to an application often causes excessive user friction and can deter users from participating. Flow solves this issue with account linking, which removes the requirement for users to sign up for a wallet prior to experiencing apps on Flow, while also enabling users to graduate to self-custody and true ownership of their assets.

**Purpose**

Account Linking enables users to sign up for an application using familiar means (email/password, social login, OAuth, etc.), while Flow account creation and key custody are handled by the app behind the scenes. Users can then use the application without needing their own wallet. When users inevitably become familiar with the concepts of true ownership and asset portability on Flow, they can then create their self-custody Flow account using their desired wallet provider.
The application would provide the means for the user to claim the original (“child”) account by linking their new (“parent”) account managed by their wallet provider and delegating access control. In this way, users can claim custody and gain control of assets stored in the application account.
**Usage**

Flow Reference Wallet supports and demonstrates account linking by automatically detecting when a transaction is attempting to perform account linking, and displaying it to the user using custom UI. Users can then view their assets across their variety of linked accounts, and manage their linked accounts directly within Flow Reference Wallet.
**Conclusion**
Flow Foundation believes that account linking eliminates the barriers to Web3 adoption by enabling familiar user onboarding mechanics to bring users to applications on Flow. Flow Reference Wallet provides support for account linking so users can seamlessly graduate to self-custody of their assets, and benefit from the portability of those assets across the ecosystem of apps on Flow.
For more information on account linking, see: [https://flow.com/account-linkingarrow-up-right](https://flow.com/account-linking)
For detailed technical documentation on account linking, see: [https://developers.flow.com/build/advanced-concepts/account-linkingarrow-up-right](https://developers.flow.com/build/advanced-concepts/account-linking)

[PreviousFAQchevron-left](/faq/faq)[NextWalletConnectchevron-right](/features/walletconnect)

Last updated 1 year ago