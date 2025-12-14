# Source: https://docs.wallet.flow.com/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard

Web3-Onboard | Flow Wallet

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

1. [Ecosystem Development](/ecosystem-development)
2. [🔌Integrate Flow EVM with Web3 SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks)

# Web3-Onboard

Integrate with Web3-Onboard

### Connect wallet to Flow EVM

Copy

```
// page.tsx
import Onboard from '@web3-onboard/core'
import injectedModule from '@web3-onboard/injected-wallets'
import { ethers } from 'ethers'

const WalletConnect = () => {
    
    // config flow network
    const onboard = Onboard({
    wallets: [injected],
    chains: [
      {
        id: '747',
        token: 'FLOW',
        label: 'Flow EVM Mainnet',
        rpcUrl: 'https://mainnet.evm.nodes.onflow.org'
      },
      {
        id: '545',
        token: 'FLOW',
        label: 'Flow EVM Testnet',
        rpcUrl: 'https://testnet.evm.nodes.onflow.org'
      }
    ]
  })
  
   // connect wallet
  const connectWallet = async () => {

      // request wallet connect
      const wallets = await onboard.connectWallet()

      if (wallets[0]) {
        setAccount(wallets[0].address)
        // create an ethers provider with the last connected wallet provider
        const ethersProvider = new ethers.BrowserProvider(flowWalletProvider, 'any')

        const { address } = wallets[0].accounts[0]

        const chainId = wallets[0].chains[0].id
        const balance = await ethersProvider.getBalance(address)

      }
  };
  
  return (
    <div>
       <button onClick={connectWallet}>Connect Wallet</button>
    <div/>
  )
}
```

See more detail on <https://github.com/Outblock/web3-onboard-flow-evm-demo>

[PreviousViem](/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem)[NextMIPD](/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd)

Last updated 11 months ago