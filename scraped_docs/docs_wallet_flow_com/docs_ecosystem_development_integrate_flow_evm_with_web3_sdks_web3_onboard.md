# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard

🚀 Web3-Onboard

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

[🛠 Ecosystem Developer Grants](/docs/ecosystem-development/ecosystem-developer-grants)

Integrate Flow EVM with Web3 SDKs

[🔌 Integrate Flow EVM with Web3 SDKs](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks)[🪝 Wagmi](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi)[🌈 Rainbowkit](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit)[⚙️ Ethers.js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/etherjs)[🌐 Web3.js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3js)[⚡ Viem](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem)[🚀 Web3-Onboard](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard)[🔍 MIPD](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd)[🧰 Other SDKs](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/others-sdks)[🔐 Privy](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy)

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

🚀 Web3-Onboard

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🚀 Web3-Onboard

Integrate with Web3-Onboard

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard.mdx)

# [Web3-Onboard](#web3-onboard)

### [Connect wallet to Flow EVM](#connect-wallet-to-flow-evm)

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

[⚡ Viem

Integrate with Viem](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem)[🔍 MIPD

Integrate with MIPD](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd)

### On this page

[Web3-Onboard](#web3-onboard)[Connect wallet to Flow EVM](#connect-wallet-to-flow-evm)