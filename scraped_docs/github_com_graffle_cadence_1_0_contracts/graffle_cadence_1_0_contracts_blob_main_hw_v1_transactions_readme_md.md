# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/README.md

transaction README
# Cadence Transactions for Hot Wheels Garage on Flow

This is code that modifies the state of the Flow Blockchain (this is where you pay for things)

## Transaction Structure

### `add_proposal_keys.cdc`

Summary: This transactions will add new proposal keys to a wallet

| parameter name | parameter type |
| :------------: | :------------: |
| numProposers | UInt16 |
---

### `admin_airdrop.cdc`

Summary: This transactions requires that an admin sign it to airdrop a redeemable to an address
| parameter name | parameter type | notes |
| :--------------: | :--------------: | :--: |
packID| UInt64 | redeemable items for series 4 will be ==2
address| Address | where the airdrop is going
token_serial| String | salesforce Serial identifier
original_card_serial| String | card serial that triggered airdrop
original_series_name| String | will be `Series_4`
original_car_name| String | name of the car that triggered airdrop
token_image_URL| String | the IPFS URL of the token that is airdropped
token_release_date| String |
token_expire_date| String
template_ID| String
token_thumbnail_CID| String
---

### `admin_mint_pack.cdc`

Summary: An admin signed transaction that will mint a pack to an address
| parameter name | parameter type | Notes |
| :--------------: | :--------------: |:--:|
| address | Address | Where the pack will be deposited
| packSeriesID | UInt64 | the pack series identifier pack series 4 == 1
| packHash | String | received from the front end
---

### `admin_mint_token.cdc`

Summary: An admin signed transaction that will mint a card to an address
| parameter name | parameter type |
| :--------------: | :--------------: |
| address | Address |
| packID | UInt64 |
| metadatas | [{String: String}] |
| packHash | String |
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

Summary: A user signed transaction that will redeem a pack with a valid packHash
| parameter name | parameter type |
| :--------------: | :--------------: |
| packID | UInt64 |
| packHash | String |
---

### `setup_project_collections.cdc`

Summary: The account that signs the transaction will initialize the project collections

---

### `userBurnAirdrop.cdc`

Summary: This is a user signed transaction to burn an airdrop card they own. To be called when the token is redeemed.
| parameter name | parameter type |
| :--------------: | :--------------: |
| airdropEditionID | UInt64 |
| owner | Address |
