# Source: https://github.com/blocto/flow-transactions/blob/main/build/MikoSea/Mikosea/user/batchDeleteComment.mainnet.cdc

```
import MIKOSEANFT from 0x0b80e42aaab305f0

transaction(commentIds:[UInt64]){
  execute{
    for commentId in commentIds {
      MIKOSEANFT.deleteComment(commentId: commentId)
    }
  }
}
```