# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks

🔌 Integrate Flow EVM with Web3 SDKs

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

🔌 Integrate Flow EVM with Web3 SDKs

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🔌 Integrate Flow EVM with Web3 SDKs

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks.mdx)

# [🔌 Integrate Flow EVM with Web3 SDKs](#-integrate-flow-evm-with-web3-sdks)

### [Detect Flow wallet provider via EIP-6963](#detect-flow-wallet-provider-via-eip-6963-)

```
// React code
import React, { useState, useEffect } from 'react';

const WalletConnect = () => {
  const [flowWalletProvider, setFlowWalletProvider] = useState(null)


  const setupEventListeners = () => {
    // detect wallet announcement
    window.addEventListener(
      'eip6963:announceProvider',
      ((event: CustomEvent) => {
        const { info, provider } = event.detail;
        console.log('Wallet announced:', info.name);
        // detect flow wallet with rdns
        if (info.rdns == 'com.flowfoundation.wallet') {
          setFlowWalletProvider(provider)
        }

      }) as EventListener
    );
  }


  useEffect(() => {
    setupEventListeners()
  }, [])
  

  // ...//

}
```

[🛠 Ecosystem Developer Grants

Previous Page](/docs/ecosystem-development/ecosystem-developer-grants)[🪝 Wagmi

Integrate with Wagmi](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi)

### On this page

[🔌 Integrate Flow EVM with Web3 SDKs](#-integrate-flow-evm-with-web3-sdks)[Detect Flow wallet provider via EIP-6963](#detect-flow-wallet-provider-via-eip-6963-)