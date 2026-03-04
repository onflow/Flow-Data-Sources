# Source: https://github.com/Flowtyio/flowty-drops/blob/main/tests/FlowtyActiveCheckers_tests.cdc

```
import Test
import "test_helpers.cdc"
import "FlowtyActiveCheckers"

access(all) fun setup() {
    deployAll()
}

access(all) fun test_FlowtyActiveCheckers_AlwaysOn() {
    let s = FlowtyActiveCheckers.AlwaysOn()
    Test.assert(s.hasStarted(), message: "AlwaysOn checker should always be started")
    Test.assert(!s.hasEnded(), message: "AlwaysOn checker never ends")

    Test.assertEqual(nil, s.getStart())
    Test.assertEqual(nil, s.getEnd())
}

access(all) fun test_FlowtyActiveCheckers_ManualChecker() {
    let s = FlowtyActiveCheckers.ManualChecker()

    Test.assertEqual(false, s.hasStarted())
    Test.assertEqual(false, s.hasEnded())
    Test.assertEqual(nil, s.getStart())
    Test.assertEqual(nil, s.getEnd())

    // now turn the checker on
    s.setStarted(true)
    Test.assertEqual(true, s.hasStarted())
    Test.assertEqual(false, s.hasEnded())

    s.setEnded(true)
    Test.assertEqual(true, s.hasStarted())
    Test.assertEqual(true, s.hasEnded())
}

access(all) fun test_FlowtyActiveCheckers_TimestampChecker_StartIsNil() {
    let end = UInt64(getCurrentBlock().timestamp) + 10
    let s = FlowtyActiveCheckers.TimestampChecker(start: nil, end: end)

    Test.assertEqual(true, s.hasStarted())
    Test.assertEqual(nil, s.getStart())

    Test.assertEqual(false, s.hasEnded())
    Test.assertEqual(end, s.getEnd()!)
}

access(all) fun test_FlowtyActiveCheckers_TimestampChecker_StartAfterNow() {
    let start = UInt64(getCurrentBlock().timestamp) + 1
    let end = UInt64(getCurrentBlock().timestamp) + 10
    let s = FlowtyActiveCheckers.TimestampChecker(start: start, end: end)

    Test.assertEqual(false, s.hasStarted())
    Test.assertEqual(start, s.getStart()!)

    Test.assertEqual(false, s.hasEnded())
    Test.assertEqual(end, s.getEnd()!)
}

access(all) fun test_FlowtyActiveCheckers_TimestampChecker_StartBeforeNow() {
    let start = UInt64(getCurrentBlock().timestamp) - 1
    let end = UInt64(getCurrentBlock().timestamp) + 10
    let s = FlowtyActiveCheckers.TimestampChecker(start: start, end: end)

    Test.assertEqual(true, s.hasStarted())
    Test.assertEqual(start, s.getStart()!)

    Test.assertEqual(false, s.hasEnded())
    Test.assertEqual(end, s.getEnd()!)
}

access(all) fun test_FlowtyActiveCheckers_TimestampChecker_Ended() {
    let start = UInt64(getCurrentBlock().timestamp) - 10
    let end = UInt64(getCurrentBlock().timestamp) - 1
    let s = FlowtyActiveCheckers.TimestampChecker(start: start, end: end)

    Test.assertEqual(true, s.hasStarted())
    Test.assertEqual(true, s.hasEnded())
}

access(all) fun test_FlowtyActiveCheckers_TimestampChecker_InvalidStartEnd() {
    let start: UInt64 = 10
    let end: UInt64 = 9

    Test.expectFailure(fun() {
        FlowtyActiveCheckers.TimestampChecker(start: start, end: end)
    }, errorMessageSubstring: "start must be less than end")
}
```