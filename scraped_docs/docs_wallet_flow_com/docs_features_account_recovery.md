# Source: https://docs.wallet.flow.com/docs/features/account-recovery

🦺 Account Recovery

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

# 🦺 Account Recovery

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/features/account-recovery.mdx)

Flow Reference Wallet enables users to recover their Flow accounts and assets in the event they lose access to their non-custodial wallet.  
  
**Background**  
  
Enabling users on Flow to safely self-custody their assets is important as it allows them to enjoy true ownership of their assets. Wallets need to address the safety drawbacks of self-custody, which include the possibility that a user will lose access to their self-custodial wallet and the keys it maintains. Fortunately, Flow natively supports features such as account abstraction and capability-based access control which open up a variety of options for how wallet providers can enable account recovery should their users lose access to the wallet.  
  
**Account Abstraction & Capability-Based Access Control**  
  
Flow's account abstraction enables accounts on Flow to have any number of keys with any number of weights. A user through their wallet provider can create multiple keys and set them to their account, perhaps storing some keys in a separate secure location or on a backup device. Weighted keys on Flow enable each account to natively act similar to a multi-sig on Ethereum. Users could share a variety of partial-weighted keys with their friends, which could collectively perform multi-sig to recover the assets of the account in the event the user's primary, full-weight keys are lost.  
  
Further, [capability-based access control on Flow](https://developers.flow.com/cadence/language/capabilities) enables even more powerful possibilities for how account recovery can be performed. A user could share a capability with a friend or another backup account, which could include defined logic to only enable account recovery on a specified account if certain conditions are met.  
  
**Usage**  
  
Flow Reference Wallet will use Flow's account abstraction and powerful features such as capability-based access control to demonstrate the variety of possible account recovery mechanics that exist for users on Flow.  
  
**Support**  
  
Today, Flow Reference Wallet supports account recovery by enabling users to store backups of their account credentials / private keys on their desired cloud storage provider (Google Drive, iCloud). This way, if a user loses access to their device they can restore access to their Flow accounts and assets. This mechanic improves the safety and security of Flow Reference Wallet as a non-custodial wallet on Flow, as users have the ability to perform account recovery in the event they lose access to their device.

The following are features not yet available on Flow Reference Wallet. These features are coming soon!

Users will be able to use secondary devices to store backup keys for their accounts on Flow managed by Flow Reference Wallet. A user will be able to store a primary key in their day-to-day device, and backup keys across a set of backup devices in case they lose access to their primary device.  
  
Since every user has different security preferences, their desired mechanic for how to perform account recovery will vary. While Flow Reference Wallet doesn't do this, some users may be comfortable with Flow Reference Wallet maintaining custody of a key or capability that allows a new key to be set on the user’s account in the event the user loses access to one or more of their keys. Other users may prefer a more secure on-chain account recovery mechanism. For example, if a user's account hasn’t executed a transaction for a defined period, or if the user's defined set of friends vote that the user lost access to their account, then a new user-controlled key might be set on the account. Flow Reference Wallet will enable users to recover access to their accounts in ways that work best for them and their security preferences.  
  
Technologies such as multi-party computation, Shamir's secret sharing, and threshold cryptography provide mechanics for distributing a user's secrets across multiple devices and systems, further removing the single point of failure that exists when custodying a user's key on a single device. Flow Reference Wallet will engage with systems such as Torus Network and Lit Protocol to provide ways to gate recovery keys behind cloud storage, social login providers, and across recovery devices should a user choose these options.  
  
**Conclusion**  
  
Flow Foundation believes that a safe user experience; one that empowers users to enjoy true ownership of their assets through self-custody while remaining safe from the possibility of losing access to a set of their account keys will further propel Flow and Web3 toward greater adoption.

[🔓 Secure Enclave

Previous Page](/docs/features/secure-enclave)[🛠 Ecosystem Developer Grants

Next Page](/docs/ecosystem-development/ecosystem-developer-grants)