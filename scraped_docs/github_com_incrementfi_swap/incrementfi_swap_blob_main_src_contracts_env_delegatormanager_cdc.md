# Source: https://github.com/IncrementFi/Swap/blob/main/src/contracts/env/DelegatorManager.cdc

```
/**
    A mock DelegatorManager to make SwapPair_Flow_stFlow compilable
*/

access(all) contract DelegatorManager {
    access(self) let epochSnapshotHistory: {UInt64: EpochSnapshot}
    access(all) var quoteEpochCounter: UInt64 

    access(all) struct EpochSnapshot {
        /// Snapshotted protocol epoch                                           
        access(all) let epochCounter: UInt64
        /// Price: stFlow to Flow (>= 1.0)                                      
        access(all) var scaledQuoteStFlowFlow: UInt256                                   
        /// Price: Flow to stFlow (<= 1.0)                                      
        access(all) var scaledQuoteFlowStFlow: UInt256 

        init(epochCounter: UInt64) {
            self.epochCounter = epochCounter
            self.scaledQuoteStFlowFlow = 1
            self.scaledQuoteFlowStFlow = 1
        }
    }

    access(all) view fun borrowEpochSnapshot(at: UInt64): &EpochSnapshot {                   
        return (&self.epochSnapshotHistory[at] as &EpochSnapshot?) ?? panic("EpochSnapshot index out of range")                                                                                           
    }

    access(all) view fun borrowCurrentQuoteEpochSnapshot(): &EpochSnapshot {                                                                                                                                           
        return self.borrowEpochSnapshot(at: self.quoteEpochCounter)                 
    }

    init() {
        self.quoteEpochCounter = 0
        self.epochSnapshotHistory = {}
        self.epochSnapshotHistory[0] = EpochSnapshot(epochCounter: 0)
    }
}
```