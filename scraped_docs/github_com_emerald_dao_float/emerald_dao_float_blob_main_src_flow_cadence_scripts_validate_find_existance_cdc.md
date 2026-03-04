# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/validate_find_existance.cdc

```
import "FIND"

access(all) fun main(name: String): Bool {
  return FIND.lookup(name) != nil
}
```