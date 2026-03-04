# Source: https://github.com/austinkline/managed-account/blob/main/contracts/samples/B.cdc

```
access(all) contract B {
    access(all) fun echo(_ s: String): String {
        return s
    }
}
```