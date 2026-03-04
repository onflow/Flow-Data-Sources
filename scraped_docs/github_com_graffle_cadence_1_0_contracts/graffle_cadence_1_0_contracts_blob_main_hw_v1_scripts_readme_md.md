# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/scripts/README.md

scripts README
# Cadence Scripts for Hot Wheels Garage on Flow

## This is code that queries the state of the Flow Blockchain

### Script Structure

---

### `get_account_status.cdc`

This script returns a boolean. If the Pack and Card collections have been initialized it will

return true, if any collection for the project is not initialized, then false.

| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_count_NFT_Packs.cdc`

This script will return the count of packs that are owned for a given address.

| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_count_NFTs.cdc`

This script will return the count of cards that are owned for a given address.

| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_NFT_in_account.cdc`

This script will return the Metadata for the given tokenID at a address

given address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
| tokenID    | UInt64    |
---

### `get_NFT_pack_totalSupply.cdc`

This script will return the total supply of minted HWGaragePack resources

| parameter name | parameter type |
| :------------: | :------------: |
|  N/A   |  N/A   |
---

### `get_NFT_totalSupply.cdc`

This script will return the total supply of minted HWGarageCard resources

| parameter name | parameter type |
| :------------: | :------------: |
|   N/A  |  N/A   |
---

### `get_owned_NFT_packs.cdc`

This script will return the pack(s) that are owned for a given

address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_owned_NFTs.cdc`

This script will return the card(s) that are owned for a given

address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_redeemable_airdrops.cdc`

This script will return the metadata for redeemable cards in a given address.

| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_token_balance.cdc`

This script will return the Flow Token balance for a given wallet address.

| parameter name | parameter type |
| :------------: | :------------: |
| account    | Address    |
---

### `storage_check.cdc`

This script will return storage stats for a given Address
| parameter name | parameter type |
| :------------: | :------------: |
| account    | Address    |
---
