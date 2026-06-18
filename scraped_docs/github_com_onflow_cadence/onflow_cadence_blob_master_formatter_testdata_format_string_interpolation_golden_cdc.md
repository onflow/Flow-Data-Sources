# Source: https://github.com/onflow/cadence/blob/master/formatter/testdata/format/string-interpolation/golden.cdc

```
access(all) fun test() {
    panic(
        "Cannot borrow DKG Participant reference from path \(FlowDKG.ParticipantStoragePath). The signer needs to ensure their account is initialized with the DKG Participant resource."
    )
    let short = "Hello \(name)!"
}

```