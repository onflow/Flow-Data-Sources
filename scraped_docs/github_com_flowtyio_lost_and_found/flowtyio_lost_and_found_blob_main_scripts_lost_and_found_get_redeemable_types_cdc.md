# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/lost-and-found/get_redeemable_types.cdc

```
import "LostAndFound"

access(all) fun main(addr: Address): [Type] {
    return LostAndFound.getRedeemableTypes(addr)
}
```