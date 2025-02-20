# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/create_participant.cdc

```
import "FlowDKG"

// TODO: only used for testing

transaction(address: Address, nodeID: String) {

    prepare(signer: auth(SaveValue) &Account) {
        let admin = getAccount(address).capabilities.borrow<&FlowDKG.Admin>(/public/dkgAdmin)
             ?? panic("Could not borrow admin reference")

        let dkgParticipant <- admin.createParticipant(nodeID: nodeID)

        signer.storage.save(<-dkgParticipant, to: FlowDKG.ParticipantStoragePath)
    }

}
```