# Source: https://github.com/blocto/flow-transactions/blob/main/transactions/MikoSea/Mikosea/user/batchDeleteComment.cdc

```
import MIKOSEANFT from 0xMIKOSEA_MIKOSEANFT_ADDRESS

transaction(commentIds:[UInt64]){
  execute{
    for commentId in commentIds {
      MIKOSEANFT.deleteComment(commentId: commentId)
    }
  }
}

```