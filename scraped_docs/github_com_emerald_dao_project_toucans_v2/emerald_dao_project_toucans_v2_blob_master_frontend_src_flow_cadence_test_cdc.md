# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/Test.cdc

```
access(all) contract Test {
  access(all) var gg: String 

  init() {
    self.gg = "gg"
  }
}
```