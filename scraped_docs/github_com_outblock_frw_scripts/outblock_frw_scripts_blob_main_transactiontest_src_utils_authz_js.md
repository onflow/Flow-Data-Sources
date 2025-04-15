# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactionTest/src/utils/authz.js

```
import { sign } from './crypto.js'
import fcl from '@onflow/fcl'

export async function authz(account) {
  return {
    // there is stuff in the account that is passed in
    // you need to make sure its part of what is returned
    ...account,
    // the tempId here is a very special and specific case.
    // what you are usually looking for in a tempId value is a unique string for the address and keyId as a pair
    // if you have no idea what this is doing, or what it does, or are getting an error in your own
    // implementation of an authorization function it is recommended that you use a string with the address and keyId in it.
    // something like... tempId: `${address}-${keyId}`
    tempId: 'SERVICE_ACCOUNT',
    addr: fcl.sansPrefix(process.env.FLOW_ACCOUNT_ADDRESS), // eventually it wont matter if this address has a prefix or not, sadly :'( currently it does matter.
    keyId: Number(process.env.FLOW_ACCOUNT_KEY_ID), // must be a number
    signingFunction: (signable) => ({
      addr: fcl.withPrefix(process.env.FLOW_ACCOUNT_ADDRESS), // must match the address that requested the signature, but with a prefix
      keyId: Number(process.env.FLOW_ACCOUNT_KEY_ID), // must match the keyId in the account that requested the signature
      signature: sign(process.env.FLOW_ACCOUNT_PRIVATE_KEY, signable.message), // signable.message |> hexToBinArray |> hash |> sign |> binArrayToHex
      // if you arent in control of the transaction that is being signed we recommend constructing the
      // message from signable.voucher using the @onflow/encode module
    }),
  }
}

export function authFunc(opt = {}) {
  const { addr, keyId = 0, tempId = 'SERVICE_ACCOUNT', key } = opt

  return (account) => {
    return {
      ...account,
      tempId,
      addr: fcl.sansPrefix(addr),
      keyId: Number(keyId),
      signingFunction: (signable) => ({
        addr: fcl.withPrefix(addr), // must match the address that requested the signature, but with a prefix
        keyId: Number(keyId), // must match the keyId in the account that requested the signature
        signature: sign(key, signable.message), // signable.message |> hexToBinArray |> hash |> sign |> binArrayToHex
        // if you arent in control of the transaction that is being signed we recommend constructing the
        // message from signable.voucher using the @onflow/encode module
      }),
    }
  }
}

export function getAuthz(addr, key, keyId = 0) {
  const authz = authFunc({
    addr,
    key,
    keyId,
  })
  return authz
}

```