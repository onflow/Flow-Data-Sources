# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/casting-continuation/golden.cdc

```
access(all) fun test() {
    self.vault <- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>())
        as! @FlowToken.Vault
    let x = something as? @SomeType
}

```