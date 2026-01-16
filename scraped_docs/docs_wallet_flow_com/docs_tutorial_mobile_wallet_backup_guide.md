# Source: https://docs.wallet.flow.com/docs/tutorial/mobile-wallet-backup-guide

🔐 Mobile Wallet Backup Guide

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

[🔐 Mobile Wallet Backup Guide](/docs/tutorial/mobile-wallet-backup-guide)[💸 Move Assets between Flow and EVM](/docs/tutorial/move-assets-between-flow-and-evm)[📱 Mobile Wallet Restore Guide](/docs/tutorial/mobile-wallet-restore-guide)[💻 Extension Wallet Backup Guide](/docs/tutorial/extension-wallet-backup-guide)[🖥️ Extension Wallet Restore Guide](/docs/tutorial/extension-wallet-restore-guide)[🔁 Extension Update Guide](/docs/tutorial/extension-update-guide)[🪙 FLOW wallet init token guide](/docs/tutorial/flow-wallet-init-token-guide)[💾 Extension Private Key and Seed Phrase Guide](/docs/tutorial/extension-private-key-and-seed-phrase-guide)[📤 Mobile Wallet Export Log Guide](/docs/tutorial/mobile-wallet-export-log-guide)

AI Integration

[🤖 AI Integration](/docs/ai-integration)

Other

[🔐 Wallet Revoke key guide](/docs/wallet-revoke-key-guide)

🔐 Mobile Wallet Backup Guide

Tutorial

# 🔐 Mobile Wallet Backup Guide

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/tutorial/mobile-wallet-backup-guide.mdx)

Welcome to the Flow Mobile Wallet! Our wallet is designed to provide a secure and user-friendly experience for managing your digital assets. One of the standout features of the Flow Mobile Wallet is its robust backup options, ensuring that your funds remain safe and accessible.

#### [Device Backup](#device-backup)

Designed with your security in mind, our mobile wallet utilizes secure enclave technology to ensure that your account is created and managed safely. With this cutting-edge approach, no private keys are accessible by the wallet team, giving you complete control over your digital assets.

With the Flow Mobile Wallet, you can easily back up your entire wallet on your device. When you register or log into your profile on your device, your profile will be automatically backed up on your device. And you can scan the QR code shown by the Flow Wallet to sync your wallet between your device. [Restore guideline link]

And you can view your device backup details in Backup section in Profile page.

![](/assets/IMG_7129.jpg)

#### [Multi-Backup](#multi-backup)

For added flexibility, the Flow Mobile Wallet supports multi-backup options. Users can create multiple backups across different devices or cloud services, ensuring that you always have access to your wallet.

A multi-backup stores multiple partial-weight keys across your accounts on trusted providers like Google Drive and iCloud(only in IOS), or a Recovery Phrase.

Two partial-weight keys must be used together to recover access to your account. Each key individually cannot be used. This means, that to recover access to your account, Flow Wallet requires access to two of your backups.

Your backups are encrypted using your wallet PIN code. You must remember or write down your PIN code and store it in a safe place.

**Step 1:** Navigate to the **Profile** page and select the **Backup** section.

![](/assets/IMG_7114.PNG)

**Step 2:** Choose 'Create Multi-Backup'.

**Step 3:** Select at least two types of backup options to ensure your assets are protected.

![](/assets/IMG_7134.jpg)

**Step 4:** If prompted, create a new PIN or verify your existing PIN to proceed with the backup process.

**Step 5:** Follow the prompts to initiate the backup process in Google Drive.

![](/assets/RPReplay_Final1727930714 [MConverter.eu].webp)

**Step 6:** Create a backup in iCloud by following the on-screen instructions.

**Step 7:** Carefully read all information regarding the recovery phrase backup. Once you understand the instructions, tick the checkbox to acknowledge.

![](/assets/IMG_7126.PNG)

**Step 8:** Copy your seed phrase and store it securely.

![](/assets/IMG_7127.PNG)

**Step 9:** Click the **Next** button. On the confirmation page, review your backups and ensure everything is in order.

#### [Seed Phrase Backup](#seed-phrase-backup)

Creating a seed phrase is a traditional method for securing your digital assets. Unlike secure enclave methods, which rely on hardware-level security, a seed phrase provides a straightforward way to restore and access your wallet across devices. This guide will walk you through the process of creating a full access seed phrase in the Flow Wallet.

**Step 1:** Navigate to the **Profile** page and select the **Backup** section.

![](/assets/IMG_7114.PNG)

**Step 2:** Choose 'Create Recovery Phrase Backup'.

**Step 3:** Carefully read all information regarding the recovery phrase backup. Once you understand the instructions, tick the checkbox to acknowledge.

![](/assets/IMG_7131.PNG)

**Step 4:** Copy your seed phrase and store it securely.

![](/assets/IMG_7132.PNG)

**Step 5:** Click the **Next** button. On the confirmation page, review your seed phrase backup and ensure everything is in order.

### [Support](#support)

If you encounter any issues or have further questions, please reach out to our support team at [support@flow.com](mailto:support@flow.com).

[💽 Open Source

Previous Page](/docs/open-source)[💸 Move Assets between Flow and EVM

Next Page](/docs/tutorial/move-assets-between-flow-and-evm)

### On this page

[Device Backup](#device-backup)[Multi-Backup](#multi-backup)[Seed Phrase Backup](#seed-phrase-backup)[Support](#support)