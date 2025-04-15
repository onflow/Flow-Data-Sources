# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactionTest/src/index.js

```
import * as fcl from '@onflow/fcl'
import * as t from '@onflow/types'
import { send as httpSend } from '@onflow/transport-http'
import { getAuthz } from './utils/authz.js'

import {
  executeTransaction,
  exportScripts,
  exportScript,
} from '@outblock/frw-transactions'

import { address } from './config/constants.js'

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

const main = async () => {
  fclInit()

  let authz = getAuthz(address, exportScripts)

  let res = await exportScripts()
  console.log(res)

  // res = await executeTransaction('basic/temp', [], { authz })
  // console.log(res)

  res = await exportScript('bridges/onboardByTypeIdentifier', {
    '0xFlowEVMBridge': '0x1e4aa0b87d10b141',
  })
  console.log(res)
}

main()

```