# Source: https://docs.wallet.flow.com/docs/features/account-linking

🔗 Account Linking

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

[🔗 Account Linking](/docs/features/account-linking)[🔌 WalletConnect](/docs/features/walletconnect)[📖 Human Readable Transactions](/docs/features/human-readable-transactions)[💚 Flow Client Library (FCL)](/docs/features/flow-client-library-fcl)[🔓 Secure Enclave](/docs/features/secure-enclave)[🦺 Account Recovery](/docs/features/account-recovery)

Ecosystem Development

Ecosystem Development

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

Features

# 🔗 Account Linking

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/features/account-linking.mdx)

Flow Reference Wallet supports Account Linking, which is uniquely supported by Flow's account abstraction, which enables accounts to be linked together to create an association between them.   
  
**Background**  
  
One of the major hindrances to Web3 adoption is often the requirement for users to sign up for a wallet provider. This step during user onboarding to an application often causes excessive user friction and can deter users from participating. Flow solves this issue with account linking, which removes the requirement for users to sign up for a wallet prior to experiencing apps on Flow, while also enabling users to graduate to self-custody and true ownership of their assets.

**Purpose**

Account Linking enables users to sign up for an application using familiar means (email/password, social login, OAuth, etc.), while Flow account creation and key custody are handled by the app behind the scenes. Users can then use the application without needing their own wallet. When users inevitably become familiar with the concepts of true ownership and asset portability on Flow, they can then create their self-custody Flow account using their desired wallet provider.  
  
The application would provide the means for the user to claim the original (“child”) account by linking their new (“parent”) account managed by their wallet provider and delegating access control. In this way, users can claim custody and gain control of assets stored in the application account.  
  
**Usage**

Flow Reference Wallet supports and demonstrates account linking by automatically detecting when a transaction is attempting to perform account linking, and displaying it to the user using custom UI. Users can then view their assets across their variety of linked accounts, and manage their linked accounts directly within Flow Reference Wallet.  
  
**Conclusion**  
  
Flow Foundation believes that account linking eliminates the barriers to Web3 adoption by enabling familiar user onboarding mechanics to bring users to applications on Flow. Flow Reference Wallet provides support for account linking so users can seamlessly graduate to self-custody of their assets, and benefit from the portability of those assets across the ecosystem of apps on Flow.   
  
For more information on account linking, see: <https://flow.com/account-linking>  
  
For detailed technical documentation on account linking, see: <https://developers.flow.com/build/advanced-concepts/account-linking>

[❓ FAQ

Answers to common questions about Flow Wallet](/docs/faq)[🔌 WalletConnect

Next Page](/docs/features/walletconnect)