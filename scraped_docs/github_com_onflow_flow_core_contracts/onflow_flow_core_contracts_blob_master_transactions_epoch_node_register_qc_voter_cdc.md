# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/node/register_qc_voter.cdc

```
import "FlowEpoch"
import "FlowIDTableStaking"
import "FlowClusterQC"

transaction() {

    prepare(signer: auth(Storage) &Account) {

        let nodeRef = signer.storage.borrow<&FlowIDTableStaking.NodeStaker>(from: FlowIDTableStaking.NodeStakerStoragePath)
            ?? panic("Could not borrow node reference from storage path")

        let qcVoter <- FlowEpoch.getClusterQCVoter(nodeStaker: nodeRef)

        signer.storage.save(<-qcVoter, to: FlowClusterQC.VoterStoragePath)

    }
}
```