# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactionTest/src/utils/crypto.js

```
import elliptic from 'elliptic'
import sha3 from 'sha3'
const e = new elliptic.ec('p256')


export const hashMsgHex = (msgHex) => {
  const sha = new sha3.SHA3(256)
  sha.update(Buffer.from(msgHex, 'hex'))
  return sha.digest()
}

export function sign(privateKey, msgHex) {
  const key = e.keyFromPrivate(Buffer.from(privateKey, 'hex'))
  const sig = key.sign(hashMsgHex(msgHex))
  const n = 32 // half of signature length?
  const r = sig.r.toArrayLike(Buffer, 'be', n)
  const s = sig.s.toArrayLike(Buffer, 'be', n)
  return Buffer.concat([r, s]).toString('hex')
}

```