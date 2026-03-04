# Source: https://github.com/Flowtyio/flow-raffle/blob/main/contracts/FLOATRaffleSource.cdc

```
import "FlowtyRaffles"
import "FLOAT"

/*
FLOATRaffleSource - A Raffle source implementation which uses the claims on a FLOAT as the source of a drawing.
*/
access(all) contract FLOATRaffleSource {
    access(all) resource RaffleSource {
        access(all) let eventCap: Capability<&FLOAT.FLOATEvents>
        access(all) let eventId: UInt64

        access(all) fun getEntries(): [AnyStruct] {
            return self.borrowEvent().getClaims().values
        }

        access(all) fun getEntryCount(): Int {
            return self.borrowEvent().getClaims().length
        }

        access(all) fun getEntryAt(index: Int): AnyStruct {
            return self.borrowEvent().getClaims()[UInt64(index)]
        }

        access(FlowtyRaffles.Reveal) fun revealCallback(drawingResult: FlowtyRaffles.DrawingResult) {
            return
        }

        access(FlowtyRaffles.Add) fun addEntry(_ v: AnyStruct) {
            panic("addEntry is not supported on FLOATRaffleSource")
        }

        access(FlowtyRaffles.Add) fun addEntries(_ v: [AnyStruct]) {
            panic("addEntries is not supported on FLOATRaffleSource")
        }

        access(all) fun borrowEvent(): &FLOAT.FLOATEvent {
            let cap = self.eventCap.borrow() ?? panic("eventCap is not valid")
            return cap.borrowPublicEventRef(eventId: self.eventId) ?? panic("invalid event id")
        }
        
        init(eventCap: Capability<&FLOAT.FLOATEvents>, eventId: UInt64) {
            self.eventCap = eventCap
            self.eventId = eventId

            // ensure we can borrow the event. This will panic if the we aren't able to
            self.borrowEvent()
        }
    }

    access(all) fun createRaffleSource(eventCap: Capability<&FLOAT.FLOATEvents>, eventId: UInt64): @RaffleSource {
        return <- create RaffleSource(eventCap: eventCap, eventId: eventId)
    }
}
```