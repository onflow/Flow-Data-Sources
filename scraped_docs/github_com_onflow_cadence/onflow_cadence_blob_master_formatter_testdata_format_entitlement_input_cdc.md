# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/entitlement/input.cdc

```
access(all) contract Foo {

    access(all)
    entitlement NodeOperator

    access(all)
    entitlement mapping AccountMapping {
        include Identity
    }
}

```