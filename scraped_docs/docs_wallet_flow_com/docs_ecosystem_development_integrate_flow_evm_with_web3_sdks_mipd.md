# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd

🔍 MIPD

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

🔍 MIPD

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🔍 MIPD

Integrate with MIPD

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/mipd.mdx)

# [MIPD](#mipd)

### [Connect wallet](#connect-wallet-)

```
// page.tsx

import { ethers, formatEther } from 'ethers'
import { createStore } from 'mipd'

const store = createStore()

const WalletConnect = () => {
    
    // get providers
    const providers = useSyncExternalStore(store.subscribe, store.getProviders, () => null) // return null of getSnapshot
    
    // find flow wallet provider or you can replace with others
    const getFlowWalletProvider = () => {
      return providers!.find(
        (provider: any) => provider.info.rdns === 'com.flowfoundation.wallet',
      );
    }
    
     // connect wallet func
    const connectWallet = async () => {
        const flowWalletProvider = getFlowWalletProvider()
        const accounts = await flowWalletProvider?.provider.request({
          method: 'eth_requestAccounts'
        });
        
        // wrap provider with etherjs
        let etherProvider = new ethers.BrowserProvider(flowWalletProvider?.provider)

        const network = await etherProvider.getNetwork();
        const chainId = network.chainId.toString()
        const balance = await etherProvider.getBalance(accounts[0])
    };
    
    
    return (
        <div>
            <button onClick={connectWallet}>Connect Wallet</button>
        <div/>
    )

}
```

See more detail on <https://github.com/Outblock/mipd-flow-evm-demo>

[🚀 Web3-Onboard

Integrate with Web3-Onboard](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3-onboard)[🧰 Other SDKs

Next Page](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/others-sdks)

### On this page

[MIPD](#mipd)[Connect wallet](#connect-wallet-)