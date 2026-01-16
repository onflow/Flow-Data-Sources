# Source: https://docs.wallet.flow.com/docs/faq

❓ FAQ

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

❓ FAQ

# ❓ FAQ

Answers to common questions about Flow Wallet

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/faq.mdx)

#### [Is Flow Wallet a Self-Custody or Custodial Wallet?](#is-flow-wallet-a-self-custody-or-custodial-wallet)

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

#### [Where is my Seed Phrase? I can't find it on Flow Wallet iOS or Android.](#where-is-my-seed-phrase-i-cant-find-it-on-flow-wallet-ios-or-android)

Flow Wallet on iOS and Android doesn't use seed phrases. Instead, it leverages your device's Secure Enclave for account security. To ensure account recovery:

1. Create a Multi-Backup
2. Navigate to Settings > Backup > Create Multi-Backup

#### [What is Multi-Backup?](#what-is-multi-backup)

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

[📘 Flow Reference Wallet Primer

Previous Page](/docs/flow-reference-wallet-primer)[🔗 Account Linking

Next Page](/docs/features/account-linking)

### On this page

[Is Flow Wallet a Self-Custody or Custodial Wallet?](#is-flow-wallet-a-self-custody-or-custodial-wallet)[Where is my Seed Phrase? I can't find it on Flow Wallet iOS or Android.](#where-is-my-seed-phrase-i-cant-find-it-on-flow-wallet-ios-or-android)[What is Multi-Backup?](#what-is-multi-backup)