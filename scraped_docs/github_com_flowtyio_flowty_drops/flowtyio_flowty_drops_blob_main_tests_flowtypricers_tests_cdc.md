# Source: https://github.com/Flowtyio/flowty-drops/blob/main/tests/FlowtyPricers_tests.cdc

```
import Test
import "test_helpers.cdc"
import "FlowtyPricers"

import "FlowToken"

access(all) let placeholder = Test.createAccount()

access(all) fun setup() {
    deployAll()
}

access(all) fun test_importAll() {
    scriptExecutor("import_all.cdc", [])
}

access(all) fun test_FlowtyPricers_FlatPrice() {
    let price = 1.1
    let pricer = FlowtyPricers.FlatPrice(price: price, paymentTokenType: Type<@FlowToken.Vault>())

    Test.assertEqual(pricer.getPaymentTypes()[0], Type<@FlowToken.Vault>())

    let num = 2
    let cost = pricer.getPrice(num: num, paymentTokenType: Type<@FlowToken.Vault>(), minter: placeholder.address)
    Test.assertEqual(cost, price * UFix64(num))
}

access(all) fun test_FlowtyPricers_Free() {
    let pricer = FlowtyPricers.Free()
    Test.assertEqual(0.0, pricer.getPrice(num: 5, paymentTokenType: Type<@FlowToken.Vault>(), minter: placeholder.address))
}
```