# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/send_whiteboard_message.cdc

```
import FlowDKG from "FlowDKG"

transaction(content: String) {

    let dkgParticipant: &FlowDKG.Participant

    prepare(signer: auth(BorrowValue) &Account) {
        self.dkgParticipant = signer.storage.borrow<&FlowDKG.Participant>(from: FlowDKG.ParticipantStoragePath)
            ?? panic("Cannot borrow dkg participant reference")
    }

    execute {
        self.dkgParticipant.postMessage(content)
    }
}
```