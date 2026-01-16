# Source: https://docs.wallet.flow.com/docs/features/human-readable-transactions

📖 Human Readable Transactions

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

# 📖 Human Readable Transactions

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/features/human-readable-transactions.mdx)

Flow Reference Wallet supports human-readable transactions during transaction authorization.  
  
**Background**  
  
When users are prompted to authorize a transaction, they are frequently presented with complex and often bewildering information, leading to confusion and increased user friction. This obscurity has unfortunately paved the way for numerous attacks, resulting in significant losses for unsuspecting victims.

On Flow, with [Interaction Templates](https://developers.flow.com/tooling/fcl-js/interaction-templates), Cadence developers have a means to declare static metadata about transactions they ask users to sign. This information is vital to understanding the outcome of the request and often includes data such as an internationalized human-readable title and description of the transaction.

Interaction template auditors play a crucial role in assessing the accuracy and safety of interaction templates. Auditors are entities in the Flow ecosystem that review Interaction Templates for correctness and safety. Flow Reference Wallet harnesses interaction templates and audits to confidently present users with clear, human-readable transaction titles and descriptions during the authorization process.  
  
**Conclusion**  
  
Interaction templates and audits eliminate the need for users to decipher unintelligible authorization prompts, ensuring they confidently sign and approve transactions that they understand.  
  
Flow Foundation believes that increasing the number of human-readable transactions through the usage of interaction templates and audits can further increase the adoption of Web3 and Flow.  
  
For more on how application developers, cadence developers and wallets can use interaction templates, see: <https://developers.flow.com/tooling/fcl-js/interaction-templates>

[🔌 WalletConnect

Previous Page](/docs/features/walletconnect)[💚 Flow Client Library (FCL)

Next Page](/docs/features/flow-client-library-fcl)