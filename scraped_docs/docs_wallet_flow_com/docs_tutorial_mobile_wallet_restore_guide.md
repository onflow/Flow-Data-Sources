# Source: https://docs.wallet.flow.com/docs/tutorial/mobile-wallet-restore-guide

📱 Mobile Wallet Restore Guide

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

📱 Mobile Wallet Restore Guide

Tutorial

# 📱 Mobile Wallet Restore Guide

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/tutorial/mobile-wallet-restore-guide.mdx)

Welcome to the Flow mobile Wallet Account Restoration Guide! This resource will help you seamlessly restore your account using various backup methods. Whether you need to recover your wallet from a device backup, utilize a multi-backup, or access your account using raw keys, we've got you covered.

![](/assets/Screenshot_20241004-123407.png)

### [From Device Backup](#from-device-backup)

When you have already logged into an account on another mobile device and want to import the same account on your current device, you can use the device backup feature. Here’s how:

**Step 1:** On your current device, select **‘From Device Backup’**.

![](/assets/Screenshot_20241004-124810.png)

**Step 2:** On the other phone, open the Flow Wallet app and use the scan feature located in the top right corner to scan the QR code.

![](/assets/Screenshot_20241004-130025.png)

**Step 3:** On the other phone, click' **Approve**' in **Connect for Flow Core**.

![](/assets/Screenshot_20241004-1254502.png)

**Step 4:** Click **‘Next’** on your current device.

**Step 5:** Finally, on the other phone, click '**Hold to Sync'.**

![](/assets/Screenshot_20241004-1255202.png)

This will complete the device backup process, allowing you to access your account on your current device.

### [From Multi Backup](#from-multi-backup)

A multi-backup stores multiple partial-weight keys across your accounts on trusted providers like Google Drive and iCloud(only in IOS), or a Recovery Phrase.

Two partial-weight keys must be used together to recover access to your account. Each key individually cannot be used. This means, that to recover access to your account, Flow Wallet requires access to two of your backups.

If you previously backed up your account using the multi-backup method [[multi-backup link](broken-reference)], you can restore your account using the following steps:

**Step 1:** On your current device, select **‘From Multi- Backup’**.

**Step 2:** Select at least two types of backup options to restore your wallet.

![](/assets/IMG_7134 (1).jpg)

**Step 3:** If you choose google drive backup, follow the prompts to restore wallet in Google Drive.

![](/assets/IMG_7142.png)

**Step 4:** Verify your existing PIN to proceed with the Google drive restore process.

![](/assets/IMG_7143.png)

**Step 5:** Restore a backup in iCloud by following the on-screen instructions.

![](/assets/IMG_7144.png)

**Step 6:** Verify your existing PIN to proceed with the iCloud restore process.

**Step 7:** Input your 15 words seed phrase.

![](/assets/IMG_7145.png)

**Step 8:** Choose the profile match with above recovery phrase.

![](/assets/IMG_7147.png)

This will complete the multi-backup process, allowing you to access your account on your current device.

### [From Raw Key](#from-raw-key)

The Flow Wallet Mobile version allows users to import profile from the Flow Wallet extension as well as various external accounts. In the section below, we will explain how to use Google Drive, full access mnemonic phrases, keystore files, and private keys to import your profiles seamlessly.

![](/assets/Screenshot_20241004-152652.png)

#### [Google Drive(if create Backup in web extension)](#google-driveif-create-backup-in-web-extension)

Restore a backup in Google drive by following the on-screen instructions.

![](/assets/screen-20241004-152739 [MConverter.eu].webp)

#### [12 word Seed Phrase](#12-word-seed-phrase)

Enter your 12-word seed phrase in the correct order.

If you have a specific derivation path or passphrase, make sure to enter it as needed.

Once you’ve entered your seed phrase (and passphrase if applicable), you should have access to your wallet and funds.

![](/assets/Screenshot_20241004-152832.png)

#### [Keystore (for Blocto users)](#keystore-for-blocto-users)

Copy and past your Blocto keystore json data in the correct order.

Enter your password and ensure that the password is entered correctly (it is case-sensitive).

![](/assets/Screenshot_20241004-152845.png)

#### [Private key](#private-key)

Copy and past your private key in the correct order.

![](/assets/Screenshot_20241004-152855.png)

### [Support](#support)

If you encounter any issues or have further questions, please reach out to our support team at [support@flow.com](mailto:support@flow.com).

[💸 Move Assets between Flow and EVM

Previous Page](/docs/tutorial/move-assets-between-flow-and-evm)[💻 Extension Wallet Backup Guide

Next Page](/docs/tutorial/extension-wallet-backup-guide)

### On this page

[From Device Backup](#from-device-backup)[From Multi Backup](#from-multi-backup)[From Raw Key](#from-raw-key)[Google Drive(if create Backup in web extension)](#google-driveif-create-backup-in-web-extension)[12 word Seed Phrase](#12-word-seed-phrase)[Keystore (for Blocto users)](#keystore-for-blocto-users)[Private key](#private-key)[Support](#support)