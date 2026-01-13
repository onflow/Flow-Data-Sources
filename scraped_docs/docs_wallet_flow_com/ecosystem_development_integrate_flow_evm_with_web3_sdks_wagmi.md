# Source: https://docs.wallet.flow.com/ecosystem-development/integrate-flow-evm-with-web3-sdks/wagmi

Wagmi | Flow Wallet

bars[![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)![](https://docs.wallet.flow.com/~gitbook/image?url=https%3A%2F%2F2259229985-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCqw72ZIu4wNI7q40hHbt%252Ficon%252FujFWaar3Vnn4QTdMskjH%252Ficon_appstore_1024.png%3Falt%3Dmedia%26token%3D52699cef-93ef-43b6-b628-efba059c75b3&width=32&dpr=4&quality=100&sign=8e5f4036&sv=2)

Flow Wallet](/)

search

circle-xmark

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
  + [🔌Integrate Flow EVM with Web3 SDKschevron-right](/ecosystem-development/integrate-flow-evm-with-web3-sdks)

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

[gitbookPowered by GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=Cqw72ZIu4wNI7q40hHbt)

block-quoteOn this pagechevron-down

copyCopychevron-down

1. [Ecosystem Development](/ecosystem-development)chevron-right
2. [🔌Integrate Flow EVM with Web3 SDKs](/ecosystem-development/integrate-flow-evm-with-web3-sdks)

# Wagmi

Integrate with Wagmi

### [hashtag](#config-wagmi-with-chains-and-providers) Config wagmi with Chains and providers

Copy

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

### [hashtag](#connect-injected-wallet-with-flow-evm) Connect injected wallet with Flow EVM

See more detail on [https://github.com/Outblock/wagmi-projectarrow-up-right](https://github.com/Outblock/wagmi-project)

[PreviousIntegrate Flow EVM with Web3 SDKschevron-left](/ecosystem-development/integrate-flow-evm-with-web3-sdks)[NextRainbowkitchevron-right](/ecosystem-development/integrate-flow-evm-with-web3-sdks/rainbowkit)

Last updated 12 months ago

* [Config wagmi with Chains and providers](#config-wagmi-with-chains-and-providers)
* [Connect injected wallet with Flow EVM](#connect-injected-wallet-with-flow-evm)

Copy

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