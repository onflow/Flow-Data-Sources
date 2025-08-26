# Source: https://docs.wallet.flow.com/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit

Rainbowkit | Flow Wallet

[![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)

Flow Wallet](/)

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
    - [Privy](/ecosystem-development/integrate-flow-evm-with-web3-sdks/privy)
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

# Rainbowkit

Integrate with Rainbowkit

[PreviousWagmi](/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi)[NextEtherjs](/ecosystem-development/integrate-flow-evm-with-web3-sdks/etherjs)

Last updated 7 months ago

`Ctrl``K`

### Connect wallet to Flow EVM

Copy

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

Copy

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