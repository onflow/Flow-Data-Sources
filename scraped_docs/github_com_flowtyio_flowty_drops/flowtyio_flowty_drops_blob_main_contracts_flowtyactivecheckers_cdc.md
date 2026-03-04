# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/FlowtyActiveCheckers.cdc

```
import "FlowtyDrops"

/*
This contract contains implementations for the FlowtyDrops.ActiveChecker struct interface.
You can use these implementations, or your own, to configure when a phase in a drop is active
*/
access(all) contract FlowtyActiveCheckers {
    /*
    The AlwaysOn ActiveChecker is always on and never ends.
    */
    access(all) struct AlwaysOn: FlowtyDrops.ActiveChecker {
        access(all) view fun hasStarted(): Bool {
            return true
        }

        access(all) view fun hasEnded(): Bool {
            return false
        }

        access(all) view fun getStart(): UInt64? {
            return nil
        }

        access(all) view fun getEnd(): UInt64? {
            return nil
        }
    }

    /*
    The manual checker is used to explicitly toggle a drop.
    This version of checker allows a creator to turn on or off a drop at will
    */
    access(all) struct ManualChecker: FlowtyDrops.ActiveChecker {
        access(self) var started: Bool
        access(self) var ended: Bool

        access(all) view fun hasStarted(): Bool {
            return self.started
        }

        access(all) view fun hasEnded(): Bool {
            return self.ended
        }

        access(all) view fun getStart(): UInt64? {
            return nil
        }

        access(all) view fun getEnd(): UInt64? {
            return nil
        }

        access(Mutate) fun setStarted(_ b: Bool) {
            self.started = b
        }

        access(Mutate) fun setEnded(_ b: Bool) {
            self.ended = b
        }

        init() {
            self.started = false
            self.ended = false
        }
    }

    /*
    TimestampChecker uses block timestamps to determine if a phase or drop is live or not.
    A timestamp checker has a start and an end time.
    */
    access(all) struct TimestampChecker: FlowtyDrops.ActiveChecker {
        access(all) var start: UInt64?
        access(all) var end: UInt64?


        access(all) view fun hasStarted(): Bool {
            return self.start == nil || UInt64(getCurrentBlock().timestamp) >= self.start!
        }

        access(all) view fun hasEnded(): Bool {
            if self.end == nil {
                return false
            }

            return UInt64(getCurrentBlock().timestamp) > self.end!
        }

        access(all) view fun getStart(): UInt64? {
            return self.start
        }

        access(all) view fun getEnd(): UInt64? {
            return self.end
        }

        access(Mutate) fun setStart(start: UInt64?) {
            self.start = start
        }

        access(Mutate) fun setEnd(end: UInt64?) {
            self.end = end
        }

        init(start: UInt64?, end: UInt64?) {
            pre {
                start == nil || end == nil || start! < end!: "start must be less than end"
            }

            self.start = start
            self.end = end
        }
    }
}
```