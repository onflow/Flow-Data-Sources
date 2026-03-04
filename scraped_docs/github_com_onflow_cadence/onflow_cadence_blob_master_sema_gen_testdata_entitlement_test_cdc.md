# Source: https://github.com/onflow/cadence/blob/master/sema/gen/testdata/entitlement/test.cdc

```
entitlement Foo

entitlement Bar

entitlement mapping Baz {
    Foo -> Bar
}

entitlement mapping Qux {
    include Identity
    Foo -> Bar
}
```