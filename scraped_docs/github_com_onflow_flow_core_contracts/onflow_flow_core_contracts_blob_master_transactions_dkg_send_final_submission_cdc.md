# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/send_final_submission.cdc

```
import FlowDKG from "FlowDKG"

transaction(submission: [String?]) {

    let dkgParticipant: &FlowDKG.Participant

    prepare(signer: auth(BorrowValue) &Account) {
        self.dkgParticipant = signer.storage.borrow<&FlowDKG.Participant>(from: FlowDKG.ParticipantStoragePath)
            ?? panic("Cannot borrow dkg participant reference")
    }

    execute {
        self.dkgParticipant.sendFinalSubmission(submission)
    }
}
```