# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/README.md

# Flow Transactions for Hot Wheels Garage V2

This is code that modifies the state of the Flow Blockchain (this is where you pay for things)

## Transaction Structure

### `admin_add_series.cdc`

Summary: This transactions will add a new series drop

| parameter name | parameter type |
| :------------: | :------------: |
| seriesID | UInt64 |
---

### `admin_airdrop_redeemable_card.cdc`

Summary: This transactions reqires that an admin sign it to airdrop a redeemable to an address
| parameter name | parameter type |
| :--------------: | :--------------: |
| address | Address |
| airdropSeriesID | UInt64 |
| metadatas | [{String: String}] |
---

### `admin_mint_card.cdc`

Summary: An admin signed transaction that will mint a card to an address
| parameter name | parameter type |
| :--------------: | :--------------: |
| address | Address |
| packHash | String |
| packSeriesID | UInt64 |
| packID | UInt64 |
| metadatas | [{String: String}] |
---

### `admin_mint_pack.cdc`

Summary: An admin signed transaction that will mint a pack to an address
| parameter name | parameter type |
| :--------------: | :--------------: |
| address | Address |
| packHash | String |
| packSeriesID | UInt64 |
| metadatas | [{String: String}] |
---

### `claim_pack.cdc`

Summary: A user signed transaction that will claim a pack with a valid packHash
| parameter name | parameter type |
| :--------------: | :--------------: |
| address | Address |
| packHash | String |
---

### `flow_transfer.cdc`

Summary: This transactions will send flow to a wallet from the user that signs this transaction
| parameter name | parameter type |
| :--------------: | :--------------: |
| amount | UFix64 |
| to | Address |
---

### `redeem_pack.cdc`

Summary: This is a user initiated transaction, it starts the redemption process for a pack
| parameter name | parameter type |
| :--------------: | :--------------: |
| packID | UInt64 |
| packHash | String |
---

### `setup_project_collections.cdc`

Summary: The account that signs it will initialize the project collections

---

### `userBurnAirdrop.cdc`

Summary: This is a user signed transaction to burn an airdrop card they own.
| parameter name | parameter type |
| :--------------: | :--------------: |
| airdropEditionID | UInt64 |
| owner | Address |
 