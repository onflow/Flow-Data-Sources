# Source: https://docs.wallet.flow.com/tutorial/move-assets-between-flow-and-evm

Move Assets between Flow and EVM | Flow Wallet

[![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)

Flow Wallet](/)

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
  + [🔌Integrate Flow EVM with Web3 SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks)
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

1. [Tutorial](/tutorial)

# 💸Move Assets between Flow and EVM

### Indroduction

Welcome to our tutorial on transferring FT and NFT between Flow Wallet, COA (Flow EVM), and EOA (Externally Owned Accounts ). As the blockchain ecosystem continues to expand, understanding how to navigate different wallets and protocols is essential for maximizing your digital asset management. This guide will provide step-by-step instructions on how to seamlessly transfer tokens between Flow Wallet and EVM environments, ensuring you can effectively manage both your fungible and non-fungible assets.

There are three types of accounts used for EVM on Flow.

1. **Externally Owned Accounts (EOA)**: EOAs are controlled by private individuals using cryptographic keys and can initiate transactions directly. They are the primary account type for users to interact with the blockchain, holding and sending cryptocurrency or calling smart contract functions.
2. **Contract Accounts**: These accounts hold smart contract code and are governed by this code's logic. Unlike EOAs, Contract Accounts do not initiate transactions on their own but can execute transactions in response to calls they receive from EOAs or other contracts.
3. **Cadence Owned Accounts (COA)**: This is an account type unique to Flow EVM. These accounts are managed by [Cadence resources](https://cadence-lang.org/docs/1.0/language/resources) and can be used to interact with the Flow EVM from within the Cadence environment.

### Fungible asset transaction

#### Transfer FT between FLOW wallet and COA

Fungible Tokens (FT) can be easily transferred between your Flow wallet and COA, as well as to other users. This guide will provide step-by-step instructions to ensure a smooth transfer process.

**1.Transferring FT Between Your Flow Account and COA**

**Step 1:** Select 'Move' button on the top-right corner of homepage.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FLwvnjkcooQqygOqV9roQ%252FScreenshot_20241001-153222.png%3Falt%3Dmedia%26token%3D86e5a2ed-86b5-4d12-9225-f98717787521&width=768&dpr=4&quality=100&sign=4f5dc10&sv=2)

**Step 2:** Select the option to Move Tokens .

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FxyuWtXEsWt97PPxK1NjO%252FScreen%2520Shot%25202024-10-01%2520at%25203.37.40%2520pm.png%3Falt%3Dmedia%26token%3Dba37d704-4243-4303-92db-ddbd7edd4dcf&width=768&dpr=4&quality=100&sign=b15552b3&sv=2)

**Step 3:** Select token from token list

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FDncusN9HnrCgTaMNATCZ%252FScreen%2520Shot%25202024-10-01%2520at%25203.36.45%2520pm.png%3Falt%3Dmedia%26token%3D5ca28241-7e5c-4544-909a-4929288b4ce3&width=768&dpr=4&quality=100&sign=5acd0da4&sv=2)

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FMijrn8maIFuEVQovt7QP%252FScreen%2520Shot%25202024-10-01%2520at%25203.37.19%2520pm.png%3Falt%3Dmedia%26token%3D9f4c59e9-5973-4f5b-ac38-fcdc242d8d6d&width=768&dpr=4&quality=100&sign=b9a13f2a&sv=2)

**Step 4:** Enter the amount you wish to transfer.

**Step 5:** Confirm the transaction details and submit the transfer.

**2.Sending FT to Other Flow Accounts/COA**

**Step 1:** Select 'Send' button in homepage.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FaShhQKpLUy0V5ZE5Kbjy%252FScreenshot_20241002-133910.png%3Falt%3Dmedia%26token%3D5bd39249-c6a8-43b4-bd5f-cb8d74be1a54&width=768&dpr=4&quality=100&sign=fb5aa4b4&sv=2)

**Step 2:** Enter the recipient's COA/other Flow account address, otherwise you can choose recipient's address you already save in address book .

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FAPy1KpUIuBQwUAwny1V4%252FScreenshot_20241002-133926.png%3Falt%3Dmedia%26token%3D964bc7c4-699f-4cfb-883e-fb43b1cc130a&width=768&dpr=4&quality=100&sign=de67f80&sv=2)

**Step 3:** Indicate the type of FT you wish to send.

**Step 4:** Indicate the amount of FT you wish to send.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F32BeEvhbJmRShIAuPXJQ%252FScreenshot_20241002-133941.png%3Falt%3Dmedia%26token%3Dd68640af-ad5e-4e02-a8b7-44aad24efac8&width=768&dpr=4&quality=100&sign=aeb043b2&sv=2)

**Step 5:** Confirm all details and click “Send” to finalize the transaction.

#### **Transfer FT to EOA**

Transferring FT to an EOA is a straightforward process. The steps to send FT from your Flow accounts anaqwd COA to EOA are the same as when sending to other Flow or COA wallets.

### Non-fungible assets transaction

#### Transfer NFT between FLOW wallet and COA

**1.Transferring NFT Between Your Flow Account and COA**

**Step 1:** Select 'Move' button on the top-right corner of homepage.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FLwvnjkcooQqygOqV9roQ%252FScreenshot_20241001-153222.png%3Falt%3Dmedia%26token%3D86e5a2ed-86b5-4d12-9225-f98717787521&width=768&dpr=4&quality=100&sign=4f5dc10&sv=2)

**Step 2:** Select the option to Move NFT.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F4dvtFl4fRL6sTQ4ZaDDp%252FScreenshot_20241002-133711.png%3Falt%3Dmedia%26token%3D6b2c0e4c-8ffe-4796-9dbd-4604fdc7eaad&width=768&dpr=4&quality=100&sign=25accba1&sv=2)

**Step 3:** Select NFT collection from nft list.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FpFdrM2YLMTx1Rd4Di2wn%252FScreen%2520Shot%25202024-10-02%2520at%25202.51.06%2520pm.png%3Falt%3Dmedia%26token%3D9e80507a-aaa0-4999-8f57-a8a273a7845e&width=768&dpr=4&quality=100&sign=3d5974f0&sv=2)

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F5xQ3UEtGMElWCROcMnVP%252FScreenshot_20241002-133731.png%3Falt%3Dmedia%26token%3Dffe0b06a-7a42-44dd-81b1-33810ca313ad&width=768&dpr=4&quality=100&sign=835bf6fa&sv=2)

**Step 4:** Select NFTs from grid view.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FEscVQ4ePvzr52yI9kqRp%252FScreen%2520Shot%25202024-10-02%2520at%25202.53.09%2520pm.png%3Falt%3Dmedia%26token%3D4c2cc195-5c42-46ca-87b6-d77e3a53d797&width=768&dpr=4&quality=100&sign=69277266&sv=2)

**Step 5:** Confirm the transaction details and click 'Move NFT' button.

**2.Sending NFT to Other Flow Accounts/COA**

**Step 1:** Select second button on the bottom of homepage

**Step 2:** Select NFT collection,then select NFT.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FFZwU953bfJxqELq5xokY%252FScreenshot_20241002-133801.png%3Falt%3Dmedia%26token%3Dbea9d4a3-eee7-4aaa-a5d0-7c4da0c7bc7b&width=768&dpr=4&quality=100&sign=9ba9ea77&sv=2)

**Step 3:** Click 'Send' button on the bottom of the page.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FvSlSoWc8pVufqZ1qgzt0%252FScreenshot_20241002-133822.png%3Falt%3Dmedia%26token%3D0385a2e0-cada-43f0-a93e-682e159bec78&width=768&dpr=4&quality=100&sign=2f7eba5a&sv=2)

**Step 4:** Enter the recipient's COA/other Flow account address.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252FOP5k0V7jRFhHIhVgn95y%252FScreenshot_20241002-133842.png%3Falt%3Dmedia%26token%3Dcb18f204-2e9d-4902-b78e-bf0a6c00252d&width=768&dpr=4&quality=100&sign=bcef6c8&sv=2)

**Step 5:** Confirm all details and click “Send” to finalize the transaction.

![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Fuploads%252F90eQ2Fvra9rXqTQo4ugq%252FScreenshot_20241002-133856.png%3Falt%3Dmedia%26token%3D9a8c2660-a737-4220-aaac-49fdadc5ecf5&width=768&dpr=4&quality=100&sign=a5ae18b9&sv=2)

### Support

If you encounter any issues or have further questions, please reach out to our support team at [[email protected]](/cdn-cgi/l/email-protection).

[PreviousMobile Wallet Backup Guide](/tutorial/mobile-wallet-backup-guide)[NextMobile Wallet Restore Guide](/tutorial/mobile-wallet-restore-guide)

Last updated 1 year ago

* [Indroduction](#indroduction)
* [Fungible asset transaction](#fungible-asset-transaction)
* [Non-fungible assets transaction](#non-fungible-assets-transaction)
* [Support](#support)