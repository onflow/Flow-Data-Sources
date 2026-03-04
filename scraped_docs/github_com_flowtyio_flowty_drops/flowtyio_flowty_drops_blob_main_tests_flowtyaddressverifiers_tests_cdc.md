# Source: https://github.com/Flowtyio/flowty-drops/blob/main/tests/FlowtyAddressVerifiers_tests.cdc

```
import Test
import "test_helpers.cdc"
import "FlowtyAddressVerifiers"

access(all) let alice = Test.createAccount()

access(all) fun setup() {
    deployAll()
}

access(all) fun test_FlowtyAddressVerifiers_AllowAll() {
    let v = FlowtyAddressVerifiers.AllowAll(maxPerMint: 10)
    Test.assertEqual(true, v.canMint(addr: alice.address, num: 10, totalMinted: 10, data: {}))
    Test.assertEqual(nil, v.remainingForAddress(addr: alice.address, totalMinted: 10))
}

access(all) fun test_FlowtyAddressVerifiers_AllowList_InAllowList() {
    let mintNum = 5
    let addresses: {Address: Int} = {alice.address: mintNum}
    let v = FlowtyAddressVerifiers.AllowList(allowedAddresses: addresses)

    Test.assertEqual(true, v.canMint(addr: alice.address, num: mintNum, totalMinted: 0, data: {}))
    Test.assertEqual(false, v.canMint(addr: alice.address, num: mintNum+1, totalMinted: 0, data: {}))
    Test.assertEqual(false, v.canMint(addr: alice.address, num: mintNum, totalMinted: 1, data: {}))

    Test.assertEqual(3, v.remainingForAddress(addr: alice.address, totalMinted: 2)!)

    v.removeAddress(addr: alice.address)
    Test.assertEqual(false, v.canMint(addr: alice.address, num: 1, totalMinted: 0, data: {}))

    v.setAddress(addr: alice.address, value: mintNum)
    Test.assertEqual(true, v.canMint(addr: alice.address, num: mintNum, totalMinted: 0, data: {}))
}

access(all) fun test_FlowtyAddressVerifiers_AllowList_NotInAllowList() {
    let mintNum = 5
    let addresses: {Address: Int} = {Test.createAccount().address: mintNum}

    let v = FlowtyAddressVerifiers.AllowList(allowedAddresses: addresses)
    Test.assertEqual(false, v.canMint(addr: alice.address, num: mintNum+1, totalMinted: 0, data: {}))
    Test.assertEqual(nil, v.remainingForAddress(addr: alice.address, totalMinted: 0))
}
```