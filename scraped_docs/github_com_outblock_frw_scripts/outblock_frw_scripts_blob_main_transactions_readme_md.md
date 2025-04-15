# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/README.md

# outblock/frw-transactions

## Execute transction with script path

```javascript
// with fcl config

import * as fcl from '@onflow/fcl'
import * as t from '@onflow/types'
import { send as httpSend } from '@onflow/transport-http'

import { executeTransaction } from '@outblock/frw-transactions'

const fclInit = () => {
  return fcl
    .config()
    .put('sdk.transport', httpSend)
    .put('accessNode.api', 'https://rest-mainnet.onflow.org')
    .put('0xNonFungibleToken', '0x1d7e57aa55817448')
    .put('0xMetadataViews', '0x1d7e57aa55817448')
    .put('0xFungibleToken', '0xf233dcee88fe0abe')
    .put('0xFlowToken', '0x1654653399040a61')
}

// ....

// script path is folder/scriptName.cdc with CamelCase
const res = await executeTransaction(
  'basic/temp',
  [], // args
  { authz: fcl.authz }, // authz
  {
    // address mapping
    '0xFlowIDTableStaking': '0x8624b52f9ddcd04a',
  },
)
console.log(res) // txId

```

## Export scripts

```javascript
import { exportScripts } from '@outblock/frw-transactions'

// export all transactions mapping
const scripts = await exportScripts()
// or with address mapping
const scripts = await exportScripts({
  '0xFlowIDTableStaking': '0x8624b52f9ddcd04a', // FlowIDTableStaking address replace
  // ....
})

// return {folder: {scriptName: scriptContent}}

// export single script
const script = await exportScript('bridges/onboardByTypeIdentifier', {
  '0xFlowEVMBridge': '0x1e4aa0b87d10b141', // FlowIDTableStaking address replace
})

// return scriptContent
```
