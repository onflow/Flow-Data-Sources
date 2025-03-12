# Source: https://developers.flow.com/build/app-architecture

App Architecture | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* App Architecture

On this page

# App Architecture on Flow Blockchain

The Flow blockchain, with its focus on scalability and user-centric design, offers a unique environment for app development. Designed from the ground up, Flow prioritizes user experience, aiming to bridge the gap to mainstream adoption without compromising on decentralization or security.

While the Flow blockchain offers various architectural patterns, the recommended approaches for developers are **Self-Custody** and **App Custody**. These choices align with Flow's ethos of user-centric design and flexibility.

### Self-Custody Architecture[​](#self-custody-architecture "Direct link to Self-Custody Architecture")

In a self-custody architecture, users retain direct control over their private keys and assets. This model emphasizes user sovereignty and decentralization, placing the responsibility of asset management squarely on the user's shoulders. While it offers the highest degree of control, it also demands a certain level of technical knowledge and awareness from the user, which can sometimes lead to a more complex user experience.

![self-custody.png](/assets/images/self-custody-30dadf36915ad9d32c951cec2bfc2a61.png)

**Architectural Elements**:

* **Wallet**: A wallet where users store their private keys and sign transactions.
* **Frontend**: Interfaces directly with the user and their wallet for signing transactions.
* **Method of Talking to Chain**: Through FCL directly.

**Benefits**:

* **Control**: Users maintain full ownership of their assets and transactions.
* **Security**: Direct management of private keys reduces potential points of failure.

**Considerations**:

* **User Experience**: The direct control model can lead to a more complex user experience, especially for those unfamiliar with blockchain. Typically, all transactions must be approved by the user, which can be cumbersome.
* **Key Management**: Users are solely responsible for managing, backing up, and ensuring the safe generation and storage of their keys.

**Ideal Use Cases**:

* **Decentralized Finance (DeFi)**: Users interacting with financial protocols while maintaining full control.
* **Web3 Native Users**: Those familiar with blockchain technology and key management.

### App Custody Architecture[​](#app-custody-architecture "Direct link to App Custody Architecture")

App custody on Flow offers a unique approach to key management and user experience. Unlike traditional app custody solutions on other blockchains, Flow's App Custody architecture introduces features like **[account linking](/build/guides/account-linking)** and **[walletless onboarding](/build/guides/account-linking/child-accounts)**. These features ensure that while users enjoy a seamless experience, they still have the option to link their accounts and move their assets freely around the Flow ecosystem, providing a balanced approach to key management.

![app-custody.png](/assets/images/app-custody-f91cb2f87bdaf50b9c8c9081f1c9e01e.png)

**Architectural Elements**:

* **Wallet**: Both user custody and app custody wallets coexist.
* **Frontend**: Interfaces for both wallet types and features for account linking and walletless onboarding.
* **Backend**: Manages app-custody user keys and assets. Also supports direct blockchain interactions.
* **Method of Interacting with the Chain**: Both direct FCL calls and backend-managed interactions.
* **Payment Rails**: Flexible methods, accommodating both direct and managed transactions.

**Benefits**:

* **Walletless Onboarding**: Users can start interacting with the app using traditional, familiar web2 mechanics without the initial need for a blockchain wallet.
* **Streamlined Experience**: Transactions can be processed without constant user approval, offering a smoother user journey.
* **Open Ecosystem with Account Linking**: Users can link their accounts, ensuring they can move their assets freely around the Flow ecosystem without being locked into a single application.
* **Flexibility**: Cater to both tech-savvy users and newcomers without compromising on security.
* **Platform Versatility**: The abstraction of the user wallet allows for integration with various platforms, including Unity games, consoles, and mobile applications.

**Considerations**:

* **Complexity**: Implementing app custody can be more intricate.
* **Trust**: Users need to trust the dApp with certain aspects of their data and assets.
* **Legal Implications**: Operating with app custody may come with legal considerations, depending on jurisdiction and the nature of the dApp. It's essential to consult with legal professionals to ensure compliance.

**Ideal Use Cases**:

* **Gaming**: Seamless gaming without constant transaction approvals.
* **Social Media Platforms**: Earning tokens for content without initial blockchain familiarity.
* **Loyalty Programs**: Earning rewards without deep blockchain setup.

## Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up")

Selecting the right architecture is crucial when developing an app on the Flow blockchain. Your choice will influence not only the technical aspects but also the user experience and overall trust in your application. While Flow offers the tools and flexibility to cater to various needs, it's up to developers to harness these capabilities effectively. Whether you opt for a self-custody or app custody approach, ensure that your decision aligns with the core objectives of your app and the expectations of your users. Making informed architectural decisions will lay a strong foundation for your app's success.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/app-architecture/index.md)

Last updated on **Feb 27, 2025** by **Chase Fleming**

[Previous

Smart Contracts ↙](/build/basics/smart-contracts)[Next

Learn Cadence ↗️](/build/learn-cadence)

###### Rate this page

😞😐😊

* [Self-Custody Architecture](#self-custody-architecture)
* [App Custody Architecture](#app-custody-architecture)
* [Wrapping Up](#wrapping-up)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.