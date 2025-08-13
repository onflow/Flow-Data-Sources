# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/CLI_SCRIPTS.md

Flow CLI ready to paste scripts for Flowty Wrapped transactions and scripts

1 - Create new emulator account
(if you already made this step before but restarted emulator, remove emulator-1 object from flow.json)
`flow accounts create`

On account name you can add: `emulator-1`

2 - Setup FlowtyWrapped Collection
`flow transactions send --signer=emulator-1 transactions/setup_flowty_wrapped.cdc`

3 - Register Edition

`flow transactions send --signer=emulator-account transactions/register_edition.cdc 'true' '0' '100' '""' '""'`

4 - Mint FlowtyWrapped

`flow transactions send --signer=emulator-account transactions/mint_flowty_wrapped.cdc '0x01cf0e2f2f715450' 'testSingleMint' '1' '1' '1' '[""]' '[""]'`

4 - Check NFT Edition

`flow scripts execute scripts/get_editions_flowty_wrapped.cdc '0x01cf0e2f2f715450' '1'`

Optional

Borrow NFT

`flow scripts execute scripts/borrow_nft.cdc '0x01cf0e2f2f715450' '1'`

Get nftIDs

`flow scripts execute scripts/get_nft_ids.cdc '0x01cf0e2f2f715450'`
