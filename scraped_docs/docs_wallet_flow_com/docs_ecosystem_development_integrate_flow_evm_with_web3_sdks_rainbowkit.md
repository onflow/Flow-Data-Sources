# Source: https://docs.wallet.flow.com/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit

🌈 Rainbowkit

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

🌈 Rainbowkit

Ecosystem DevelopmentIntegrate Flow EVM with Web3 SDKs

# 🌈 Rainbowkit

Integrate with Rainbowkit

[Edit](https://github.com/onflow/FRW-doc/blob/main/content/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit.mdx)

# [Rainbowkit](#rainbowkit)

### [Connect wallet to Flow EVM](#connect-wallet-to-flow-evm)

```
// _app.tsx config provider
import {NextUIProvider} from "@nextui-org/react";
import type { AppProps } from 'next/app';
import {RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';


function MyApp({ Component, pageProps }: AppProps) {

    return (
        <NextUIProvider>
            <OtherProvider>
                <RainbowKitProvider theme={darkTheme()}>
                      <main className="dark text-foreground bg-background">
                        <Component {...pageProps} />
                      </main>
                  </RainbowKitProvider>
             <OtherProvider/>
         <NextUIProvider/>
    )    
}
```



```
// index.ts import connectButton
import { ConnectButton } from '@rainbow-me/rainbowkit'

const Home: NextPage = () => {
    return (
        <main className={styles.main}>
            <h1>Flow EVM Demo</h1>
            <ConnectButton showBalance={true} />
        <main/>
    )
}
```

See more detail on <https://github.com/Outblock/flow-evm-rainbow>

[🪝 Wagmi

Integrate with Wagmi](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi)[⚙️ Ethers.js

Integrate with Ethers.js](/docs/ecosystem-development/integrate-flow-evm-with-web3-sdks/etherjs)

### On this page

[Rainbowkit](#rainbowkit)[Connect wallet to Flow EVM](#connect-wallet-to-flow-evm)