# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi

🪝 Wagmi

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

🪝 Wagmi

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🪝 Wagmi

Integrate with Wagmi

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi.mdx)

# [Wagmi](#wagmi)

### [Config wagmi with Chains and providers](#config-wagmi-with-chains-and-providers)

```
// config.ts file
import { http, cookieStorage, createConfig, createStorage } from 'wagmi'
import { flowMainnet, flowTestnet} from 'wagmi/chains'

export function getConfig() {
  return createConfig({
    chains: [flowMainnet, flowTestnet],
    connectors: [
      injected(),
    ],
    storage: createStorage({
      storage: cookieStorage,
    }),
    ssr: true,
    transports: {
      [flowMainnet.id]: http(),
      [flowTestnet.id]: http(),
    },
  })
}
```

### [Connect injected wallet with Flow EVM](#connect-injected-wallet-with-flow-evm-)

```
// page.ts
import { useAccount, useConnect, useDisconnect, useSignMessage, useVerifyMessage } from 'wagmi'
import { signMessage, getAccount, verifyMessage } from '@wagmi/core'
import { getConfig } from '../config'

function App() {
    const config = getConfig()

    const account = useAccount()
    const { connectors, connect, status, error } = useConnect()

    return (
       <div>
          <h2>Connect</h2>
          {connectors.map((connector) => (
            <button
              key={connector.uid}
              onClick={() => connect({ connector })}
              type="button"
            >
              {connector.name}
            </button>
          ))}
        <div/>
    )
}
```

See more detail on <https://github.com/Outblock/wagmi-project>

[🔌 Integrate Flow EVM with Web3 SDKs

Previous Page](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks)[🌈 Rainbowkit

Integrate with Rainbowkit](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit)

### On this page

[Wagmi](#wagmi)[Config wagmi with Chains and providers](#config-wagmi-with-chains-and-providers)[Connect injected wallet with Flow EVM](#connect-injected-wallet-with-flow-evm-)