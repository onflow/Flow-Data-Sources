# Source: https://github.com/Flowtyio/lost-and-found/blob/main/scripts/lost-and-found/get_address.cdc

```
import "LostAndFound"

access(all) fun main(): Address {
    return LostAndFound.getAddress()
}
```