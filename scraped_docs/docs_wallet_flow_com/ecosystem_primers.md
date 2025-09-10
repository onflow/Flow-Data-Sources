# Source: https://docs.wallet.flow.com/ecosystem-primers

Flow Reference Wallet Primer | Flow Wallet

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

1. [Ecosystem Primers](/ecosystem-primers)

# ⭐Flow Reference Wallet Primer

**Introduction**
Flow is proud to unveil **Flow Reference Wallet**; a new self-custodial wallet designed to serve as a beacon to the Flow ecosystem, guiding wallets with an open-source implementation of the novel and unique product opportunities for wallets on the Flow blockchain. Flow Reference Wallet sets a new standard for wallet development on Flow by promoting a robust and secure, open-source, community-led foundation for wallet developers to build on.
Flow Reference Wallet is available on iOS, and Android. A Chrome Extension can be installed for web support. The release of Flow Reference Wallet marks a significant step towards enhancing user self-custody and ensuring the secure management of assets on the Flow blockchain. It unlocks powerful native features of Flow’s account abstraction model, and transaction model, and provides opportunities for developers to build apps with composable assets and extensible, interoperable mechanics.
This document explains the background behind why Flow built this new wallet and goes into the wallet's key features, including secure key management, account abstraction support, account linking, and the unique possibilities they unlock for user experience and safety, all to advance Web3 adoption and empower users with true ownership of their assets.
**Background**
**‍**
This document explains the background behind why Flow built this new wallet and goes into the wallet's key features, including secure key management, account abstraction support, account linking, and the unique possibilities they unlock for user experience and safety, all to advance Web3 adoption and empower users with true ownership of their assets.
Enabling users to safely self-custody their assets is important as it allows them to enjoy true ownership of their assets on Flow. Flow needs secure wallets that address the current drawbacks of self-custody, and solve the common cases of user error while lowering the technical complexity of maintaining a self-custody account.
Further, Flow’s novel architecture and design enables new features that unlock valuable user experiences and possibilities. Flow's account abstraction, transaction, and key models function differently than those on other networks. Therefore wallets on Flow need to account for these differences and help enable the new user experiences they make possible.
**Key Management**
**‍**
When a user creates a self-custody account, a seed phrase is often created that’s used to derive their private key(s). Users are instructed to save their seed phrase and store it in a secure location. Users often fail to properly secure their seed phrase and can fall victim to social engineering tactics and other schemes that trick them into improperly exposing their seed phrase to a malicious 3rd party. Seed phrases also add significant friction when setting up a wallet due to their confusing nature and the requirement to store them securely. These imperfections make seed phrases cumbersome and error-prone unless used properly by astute or experienced users.
Fortunately, Apple offers secure enclave hardware on its latest iPhone devices. Since secure-enclave supports ECDSA P-256 keys (which are used by Flow’s account abstraction), the iPhone can be utilized as a storage mechanism for a user’s private keys. Securing keys on the iPhone’s secure enclave does not require a seed phrase. It enables users to benefit from the hardware and portability of their mobile device as their self-custody wallet.
Additionally, multi-party computation, Shamir’s secret sharing, and threshold cryptography provide mechanics for distributing a user's secrets across multiple devices and systems, removing the single point of failure that exists when custodying a user's key on a single device. Flow’s account abstraction model also enables multiple keys (of potentially varied weights) to be configured on a single account, enabling wallets to store multiple keys across a set of devices a user controls.
**Transaction Authorization**
**‍**
When prompted to authorize a transaction, wallets often display complex technical information to the user which can be confusing and adds friction to the process. Users often lack the technical understanding to safeguard themselves against authorizing malicious transactions. They risk having their assets stolen and can easily be tricked into signing a transaction that doesn’t do what they expect.
Ideally, users should be presented with messaging that explains what a transaction will do using language they can properly understand and consent to. Transactions should also be audited for safety, and those audits should be presented to a user to help them understand which transactions are safe to authorize. This way, users can have reasonable ways to safeguard themselves from potential attacks and scams.
**Account Abstraction**
**‍**
Flow’s account abstraction provides unique ways for a user to own an account. A user controls keys within their wallet, and those keys can be added to various accounts on Flow. The notion of ownership of an account can be thought of as whether a user can control an account using the keys they maintain. If a key a user controls is added to an account on Flow, and that key has full signing weight on that account, then that account is owned by the user (along with all of its assets). This enables the ability to airdrop assets to a user by adding that user's key to an account containing the assets being airdropped.
Account abstraction on Flow also enables multiple users to hold keys of varied weights on the same account. This means native accounts on Flow function similarly to multi-sig wallets on Ethereum. Users should be able to coordinate with other key holders for an account on transactions to execute, as well as manage the keys held on their accounts. This way users can benefit from the ability to jointly own accounts among groups of other users.
Flow uses a concept known as capabilities to secure and delegate access to functionality on assets held in an account. If a user wants to grant access to some functionality on an asset held in their account with another user or application, they can grant a capability representing that access and give the capability to the other party. While capabilities are groundbreaking in what they make possible for applications on Flow, for users they need to be communicated and expressed to them in understandable ways. A user’s wallet will need to express to the user what assets are impacted by the capabilities that have been granted to their accounts and be able to revoke any capabilities they no longer want.
Account abstraction on Flow also enables accounts to have storage. Account storage is where a user’s assets reside. It uses a mechanic similar to a file system on a computer, where each asset is stored at a unique storage path. It’s difficult for users today to understand what is stored within their accounts storage as Flow lacks tools that express account storage in understandable ways. Flow needs wallets to be able to surface account storage information to users and allow them to manage the assets held within their accounts.
**Account Linking**
**‍**
Account Linking makes frictionless user onboarding possible for applications on Flow. Applications can streamline user onboarding by offering familiar email and social login registration methods, while in the background creating and managing Flow accounts for users dedicated to their application-related activity and assets. As users progress to establishing a self-custody wallet, they can seamlessly connect it with their application accounts through Flow's Account Linking feature.
Given the novelty of this concept, it's crucial to present it intuitively to users. This entails wallet interfaces displaying a clear list of linked accounts, along with the corresponding applications they are associated with. Additionally, Flow wallets should provide the option to unlink accounts, giving users full control over their account management preferences and child account assets.
**Unique Possibilities for Wallets on Flow**
**‍**
In order to highlight the intrinsic value of Flow's design and promote the broader adoption of Web3, we must focus on enhancing the user experience and ensuring users can securely self-custody their assets. To achieve this, it's essential that wallets on Flow address a variety of user stories:
**Multiple Account Ownership Recognition**
- As a **User**, I want to be able to have the accounts on Flow that I control recognized by my wallet, so I can take action upon those accounts and the assets they own
- As a **Developer,** I want to be able to airdrop assets to a user by creating a new account on Flow, depositing the assets to airdrop to the new account, and then adding the recipient's key(s) to the account.
**Shared Account Ownership**
- As a **User**, I want to be able to share ownership of an account with others and to share group custody of those accounts and the assets contained.
**Account Key Management**
- As a **User**, I want to use the specialized secure enclave hardware on my iPhone to securely manage my Flow account keys to achieve self-custody of my accounts and assets.
**Account Storage Management**
- As a **User**, I want to be able to manage my account(s) storage, view the assets that are contained, and perform actions upon those assets such as relocation, transfer, deletion, etc.
**Account Linking Management**
- As a **User**, I want to be able to view which application accounts my account is linked to, including their associated metadata.
- As a **User**, I want to be able to unlink my account from a connected application account to remove the association.
- As a **User**, I want to be shown when a transaction is an account-linking transaction, so I can understand and consent to linking my primary wallet-managed account with an application account.
**Capability Management**
- As a **User**, I want to be able to view all outstanding capabilities I've granted to see what assets and functionality in my account(s) are impacted.
- As a **User**, I want to be able to revoke outstanding capabilities that I’ve granted to remove the possibility of my account(s) and assets being impacted.
**Human Readable Transaction Authorization**
- As a **User**, I want to be shown a human-readable explanation of a transaction I'm requested to sign, so I can understand what it does and how it impacts my account and assets.
**Account Recovery**
- As a **User**, I want to be able to recover my account if I lose access to a set of my account’s keys to recover access to the account and the assets it contains.
**Human Readable Transaction Authorization**
**‍**
When users are prompted for authorization during a transaction, they are frequently presented with complex and bewildering information, leading to confusion and increased user friction. This obscurity has unfortunately paved the way for numerous attacks, resulting in significant losses for unsuspecting victims.
Given the novelty of this concept, it's crucial to present it intuitively to users. This entails wallet interfaces displaying a clear list of linked accounts, along with the corresponding applications they are associated with. Additionally, Flow wallets should provide the option to unlink accounts, giving users full control over their account management preferences and child account assets. On Flow, with interaction templates (<https://developers.flow.com/tooling/fcl-js/interaction-templates>), Cadence developers have a means to declare static metadata about transactions they ask users to sign. This information is vital to understanding the outcome of the request and may include data such as a human-readable title and description.
Interaction template auditors play a crucial role in assessing the accuracy and safety of these templates. Wallets can harness interaction template audits to confidently present users with clear, human-readable transaction titles and descriptions during the authorization process. This approach eliminates the need for users to decipher unintelligible authorization prompts, ensuring they receive and understand important information and can confidently sign and approve.
To leverage the enhanced user experience that this mechanism offers, wallets should embrace best practices in the use of interaction templates for all Flow users.
For more on how application developers and wallets can use Interaction Templates, see: <https://developers.flow.com/tooling/fcl-js/interaction-templates>
**Account Linking**
Accounts on Flow can be linked to create an association between them. This provides many benefits, including improved user onboarding to applications on Flow. Users can sign up for an app via traditional means (email/password, social login, OAuth, etc.), while Flow account creation and key custody are handled by the application. When users become familiar with the concepts of true ownership and asset portability on Flow, they may create their self custody wallet. The application would provide the means to claim the original (“child”) account by linking their new (“parent”) account and delegating access control. In this way, users can claim custody and gain control of assets stored in the application account for use across the Flow ecosystem. Wallets are encouraged to add support for account linking to improve user experience and allow management and visualization of all user-controlled accounts.
For more information on Account Linking, see: <https://developers.flow.com/concepts/hybrid-custody>**Account & Key Ownership**
Account abstraction on Flow enables accounts to have multiple keys that can be added and revoked. When an account on Flow is created, it can be created with any number of keys controlled by any number of entities. An interesting mechanic that is possible on Flow, is the ability to airdrop assets to another user by creating a new account on Flow, depositing assets to the new account, and then finally adding the key of the intended recipient of the assets, all within a single transaction. However, for the user to know that these airdropped assets are owned by them, they need to be displayed to them in their wallet; and to be displayed, the wallet needs to recognize that their user’s key is active on a new account, thereby making the user the owner of its assets.
Wallets need to ensure they are designed with a one-to-many relationship between key and account. When a wallet-controlled key is added to a new account on Flow, the wallet should recognize this and display the newly controlled account to the user. This additionally means that a wallet should enable a user to control multiple Flow accounts, perhaps each controlled by any number or combination of wallet or externally controlled keys.
Since account abstraction on Flow enables accounts to have multiple revocable keys, each of which can have a specific weight, wallets therefore must be able to maintain a set of zero to many keys controlled by a user each with their own specific weight. Wallets should also enable a user to revoke a key they control on an account at any time, as well as create new keys with their preferred weight to add to an account.
For more information on Accounts and Keys on Flow, see: <https://developers.flow.com/concepts/start-here/accounts-and-keys>**Account Key Management & Recovery**
Flow’s account abstraction supports ECDSA P-256 keys which are also supported by the secure-enclave hardware on iPhone. Non-custodial mobile wallets on Flow should therefore use this credible specialized hardware for secure key management, as it enables users to benefit from the credibility, portability, utility, and security of their mobile device as their non-custodial wallet on Flow. Critically, using iPhone’s secure enclave to store keys removes the need for the user to set up a seed phrase, as their keys can be stored directly inside their device. Users should be able to use secondary iPhone devices to store backup keys for their accounts on Flow. A user should be able to store a primary key in their day-to-day device, and backup keys across a set of backup devices in case they lose access to their primary device.
Other mechanics can enable account recovery in the event a user loses access to one or more of their keys. Every user has different preferences, and their preferred mechanic for how account recovery can be performed will vary. Some users may be comfortable with a wallet provider maintaining custody of a key or capability that allows them to set a new key on the user’s account in the event the user loses access to one or more of their keys. Other users may prefer an on-chain account recovery mechanism. For example, if one’s account hasn’t executed a transaction for a defined period, or if the user's defined set of friends vote that the user lost access to their account, then a new user-controlled key might be set on the account. Wallets need to enable users to recover access to their accounts in ways that work best for them.
Technologies such as multi-party computation, Shamir's secret sharing, and threshold cryptography provide mechanics for distributing a user's secrets across multiple devices and systems, further removing the single point of failure that exists when custodying a user's key on a single device. Wallets should engage with systems such as Torus network and lit protocol to provide ways to gate recovery keys behind cloud storage, social login providers, and across recovery devices should a user choose these options.
Promoting a safe user experience; one that empowers users to enjoy true ownership of their assets through self custody, while remaining safe from the possibility of losing access to a set of their account keys will propel Flow and Web3 toward mainstream consumer adoption.
**Account Storage Management**
Flow’s account abstraction enables accounts to have storage. Account storage is where a user’s assets reside, such as their non-fungible tokens, and fungible tokens among others. Similar to storage on a computer, a user may want to manage and view their account storage. This mechanic can take a form similar to that of a file browser on a computer, where a user’s assets are displayed and operations can be performed on them, such as relocation, deletion, viewing their size, provenance, metadata, etc. Since resources on Flow can contain other resources, as is the case for many NFT collections, a user may want to further organize their assets by nesting various resources within each other. For example, a user may organize their NBA Top Shot assets in an NBA Top Shot collection dedicated exclusively to just their favorite moments. A user may further wish to move assets between their Flow accounts, including their linked application accounts.
For more about account storage on Flow, see: <https://developers.flow.com/cadence/language/accounts#account-storage>**Capability Management**
Accounts on Flow can create cadence capabilities that allow the owner of the capability to perform defined mechanics on an account’s assets. For example, a user may grant a capability that allows an external application to modify some component of one of their NFTs. A user could also grant a capability that allows another user to withdraw an amount of FLOW from their account. Capabilities are almost limitless in what they can do and are a critical part of the security and access model for cadence.
Capabilities are managed by an account’s capability controller, which is a system that allows the account to grant, view, and revoke previously granted capabilities. Therefore, wallets need to implement the ability for their users to view, grant, and revoke their previously granted capabilities. What a capability does and represents needs to be expressed to the user in a way that is understandable to them. It should be clear to the user what assets are impacted by which capabilities. This way, a user can safely manage how their assets are impacted by the capabilities they grant.
For more on Flow capability controllers, see: <https://github.com/onflow/flips/blob/main/cadence/20220203-capability-controllers.md>**Ecosystem Lighthouse Wallet**
Flow released a new wallet offering on Flow, **Flow Reference Wallet**. This wallet will act as an ecosystem lighthouse that will progress toward implementing the specified unique product possibilities for Flow. It launched with the majority of its codebase open-source, with the goal of progressing to becoming entirely open-source. The intention for this wallet is to provide an example for other wallet developers on Flow of what is possible, while also providing them with open-source code that can be used by them to replicate and build upon. This wallet will be released on the Apple App Store, Google Play, and Chrome Extension Store for consumer use. Flow intends for this wallet to be an ecosystem project, with community grants available to further its development. Ultimately, this wallet will demonstrate the product possibilities for wallets on Flow, while acting to inspire and promote wallet developers to implement these features in their wallet offerings.
**Development Timeline**
The first version of Flow Reference Wallet was released in Q3 2023.
To follow the development of the new Flow Reference Wallet, the open-source issue/project tracker is available on GitHub, see: <https://github.com/orgs/Outblock/projects/2>**Ecosystem Grants**
To encourage ecosystem participation in the development of Flow Reference Wallet, the following grant projects are available as inspiration for a grant proposal: [https://github.com/onflow/developer-grants/blob/main/projects/flow-core-wallet/README.md](https://github.com/onflow/developer-grants/blob/project-fcw/projects/flow-core-wallet/README.md)**Outcome**
With the release of the Flow Reference Wallet, Flow application developers and users will have a wallet they can use that supports the unique product possibilities for wallets on Flow, and wallet developers will have open-source materials they can use to build upon to improve their product offerings.
**Commitment**
Flow is committed to an open, thriving ecosystem of wallets on Flow. As such, Flow Reference Wallet’s purpose is to promote ecosystem wallet development on Flow by providing open-source examples and materials of Flow’s key product possibilities for wallets. Flow Reference Wallet will not partake in any application or project partnerships, nor will it act as a revenue-generating product. Flow Reference Wallet is intended to be a reference wallet, and is not positioned long term to be the primary wallet for end consumers in Flow’s ecosystem; rather, it’s intended to support ecosystem wallets to build better products to further their and Flow’s adoption.
**Conclusion**
Flow Reference Wallet will increase Flow’s competitiveness in the greater Web3 ecosystem by enabling best-in-class blockchain user experience by highlighting the product possibilities for wallets that Flow's unique design presents while supporting Flow’s ecosystem of wallets by providing open-source examples and materials.
**Contact**
**Hao Fu** - Flow Reference Wallet
telegram: @lmcmz
‍**Jeffrey Doyle** - Flow Wallets
telegram: @jeffjeffjeffjeffjeffjeffjeff
**Working Group**
Flow has an open working group dedicated to furthering the development of wallets on Flow. If you’d like to join this working group please email [[email protected]](/cdn-cgi/l/email-protection) to be added to the recurring meeting.

[PreviousWelcome to Flow Wallet](/)[NextFAQ](/faq/faq)

Last updated 1 year ago