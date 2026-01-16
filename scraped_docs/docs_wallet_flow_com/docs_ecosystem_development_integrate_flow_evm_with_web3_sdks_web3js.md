# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3js

🌐 Web3.js

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

🌐 Web3.js

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🌐 Web3.js

Integrate with Web3js

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/web3js.mdx)

# [Web3js](#web3js)

### [Connet wallet](#connet-wallet)

```
// Some code
import Web3 from 'web3';

const WalletConnect = () => {

    // connect wallet
    const connectWallet = async () => {
        // init web3 
        const web3 = new Web3(flowWalletProvider);
        // connect wallet
        await flowWalletProvider.request({ method: 'eth_requestAccounts' });
        const accounts = await web3.eth.getAccounts();
  
        const chainId = await web3.eth.getChainId();
        const balance = await web3.eth.getBalance(accounts[0]);
    
      };
  
  return (
     <div>
       <button onClick={connectWallet}>Connect Wallet</button>
     <div/>
  )
}
```

See more detail on <https://github.com/Outblock/web3js-flow-evm-demo>

See more detail on <https://github.com/Outblock/web3js-flow-evm-demo>

[⚙️ Ethers.js

Integrate with Ethers.js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/etherjs)[⚡ Viem

Integrate with Viem](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/viem)

### On this page

[Web3js](#web3js)[Connet wallet](#connet-wallet)