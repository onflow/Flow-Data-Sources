# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem

⚡ Viem

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

⚡ Viem

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# ⚡ Viem

Integrate with Viem

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem.mdx)

# [Viem](#viem)

### [Connect wallet to Flow EVM](#connect-wallet-to-flow-evm)

```
// page.tsx

import { createWalletClient, custom, http } from 'viem'
import { flowMainnet, flowTestnet } from 'viem/chains'

const WalletConnect = () => {
    
  // connect wallet function
  const connectWallet = async () => {
    try {
      const client = createWalletClient({
        chain: flowMainnet,
        transport: custom(flowWalletProvider!)
      })

      // request user to connect wallet
      const [address] = await client.getAddresses()
      const chainId = await client.getChainId(); // get chain id

    } catch (err: any) {
      console.log('Connect wallet failed:' + err.message);
    }
  };
  
  return (
      <div>
         <button onClick={connectWallet}>Connect Wallet</button>
      <div/>
  )
}
```

See more detail on <https://github.com/Outblock/viem-flow-evm-demo>

[🌐 Web3.js

Integrate with Web3js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3js)[🚀 Web3-Onboard

Integrate with Web3-Onboard](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard)

### On this page

[Viem](#viem)[Connect wallet to Flow EVM](#connect-wallet-to-flow-evm)