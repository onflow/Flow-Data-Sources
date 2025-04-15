# Source: https://github.com/Outblock/FRW-scripts/blob/main/scriptTest/src/index.js

```
import * as fcl from '@onflow/fcl'
import * as t from '@onflow/types'
import { send as httpSend } from '@onflow/transport-http'

import {
  queryScripts,
  exportScripts,
  exportScript,
} from '@outblock/frw-scripts'

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
  const scriptMap = await exportScripts()
  const script = await exportScript('bridges/calculateBridgeFee', {
    '0xFlowEVMBridge': '0x1e4aa0b87d10b141',
  })
  console.log(script)

  fclInit()
  let res = await queryScripts('staking/getApr', [], {})
  console.log(res)
  res = await queryScripts(
    'basic/getAccountInfo',
    [fcl.arg('0x1d7e57aa55817448', t.Address)],
    {},
  )
  console.log(res)
}

main()

```