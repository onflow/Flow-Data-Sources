# Source: https://docs.wallet.flow.com/docs/features/secure-enclave

🔓 Secure Enclave

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

🔓 Secure Enclave

Features

# 🔓 Secure Enclave

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/features/secure-enclave.mdx)

Flow’s account abstraction deliberately supports ECDSA P-256 keys which are also supported by the Secure Enclave hardware on iPhone.   
  
**What is a Secure Enclave?**

A secure enclave is an environment that provides for the isolation of code and data from an OS using hardware-based CPU-level isolation. It provides a secure, isolated environment for storing and processing sensitive information, such as private keys and biometric data. It's designed to protect sensitive data from unauthorized access, even if the device itself is compromised, and is used by mobile applications to provide enhanced security for their users. This makes it an ideal tool for securing sensitive data on mobile devices.

**Why use Secure Enclave?**

Secure Enclave is a valuable security feature that can help enhance the security of mobile applications and protect users' sensitive data from unauthorized access. By using the Secure Enclave, wallet developers can help to build more secure, reliable, and trustworthy wallets, which can ultimately lead to increased user confidence and adoption.

**Using iPhone's Secure Enclave on Flow Blockchain**

Flow supports multiple curves (such as `secp256k1`) and hash algorithms including `NIST-P256` curve (also called `secp256r1`), which is a widely-used elliptic curve algorithm that provides enhanced security for cryptographic operations. To use iPhone's Secure Enclave on Flow blockchain, wallet developers can use the [CryptoKit](https://developer.apple.com/documentation/cryptokit) framework on iOS and the Android [Keystore](https://developer.android.com/training/articles/keystore) system on Android.  
  
**Pros and Cons of using Secure Enclave**  
  
By understanding the pros and cons of Secure Enclave on iPhone, wallet developers can make informed decisions about how to best secure their wallets and protect their users' data.

#### [Pros](#pros)

1. **Enhanced Security**: The Secure Enclave is a type of Hardware Security Module (HSM) that provides a robust layer of hardware-based security, making it more difficult for attackers to gain unauthorized access to sensitive information.
2. **Ease of Use**: Using the Secure Enclave is generally quite easy and straightforward for developers, as it is integrated into the operating system of the mobile device. This makes it an attractive option for developers who want to add an extra layer of security to their apps without having to invest a lot of time or effort.
3. **Protection Against Physical Attacks**: Secure Enclave on iPhone is designed to be tamper-resistant, which means that it can protect sensitive information even if the mobile device is stolen or lost. This is because the Secure Enclave is tied to a specific device and is not transferable to other devices, making it difficult for attackers to access the information stored in it.
4. **Increased Privacy**: Secure Enclave provides a privacy and security-sensitive option for users who wish to custody their keys using their own hardware instead of relying on cloud backups or custodial service providers.

#### [Cons](#cons)

1. **Hardware Limitations**: The Secure Enclave is only available on certain devices, and requires specific hardware components to function properly. This means that it may not be available or practical to use on all devices.
2. **Risk of Losing Access to Private Keys**: If a user loses their mobile device, the private key stored in the Secure Enclave will also be lost. This is because the Secure Enclave is tied to the specific device and is not transferable to other devices. Therefore, users must take appropriate measures to protect their devices and backup their data, including their private keys, to avoid losing access to their accounts and data.

While the Secure Enclave is a secure and effective way to protect sensitive data on mobile devices, it's important to keep in mind that there is a risk of losing access to the data stored in the enclave if the device is lost or stolen. If a user loses their device, their private key stored in the Secure Enclave will also be lost, which can result in a permanent loss of access to their accounts and data.

**Flow's Advantage in Using iPhone's Secure Enclave**

Flow blockchain has a native solution to the challenge of losing access to private keys. It supports account abstraction natively, which decouples the address and private keys, allowing users and wallets to add multiple keys with varying weights to the same account. This approach provides greater flexibility and security in managing cryptographic operations, while also reducing the risk of losing access to private keys.

For instance, wallets can add backup keys such as social recovery keys, custody account keys, or seed phrase keys to the same accounts, in addition to secure enclave keys. These [account recovery mechanisms](account-recovery.md) provide additional layers of security and accessibility to users, enhancing the overall experience of using Flow.

Moreover, Flow offers another solution for this issue through its [account linking](account-linking.md) feature. By linking existing accounts as child accounts to a user's main account as the parent account, if a user loses access to their child account, they can still withdraw and manage their child account assets through the parent account.

**Conclusion**  
  
Considering the advantages of using Secure Enclave on iPhone, Flow Reference Wallet will therefore move to support this credible specialized hardware for secure key management, as it enables users to benefit from the credibility, portability, utility, and security of their mobile device as their non-custodial wallet on Flow.

[💚 Flow Client Library (FCL)

Previous Page](/docs/features/flow-client-library-fcl)[🦺 Account Recovery

Next Page](/docs/features/account-recovery)

### On this page

[Pros](#pros)[Cons](#cons)