# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/README.md

# Flow Scripts for Hot Wheels Garage V2

## This is code that queries the state of the Flow Blockchain

### Script Structure

---

### `get_account_status.cdc`

Summary:

This script returns a boolean. If the collection has been initialized it will return true, if any collection for the project is not initialized, then false.

 | parameter name | parameter type |
 | :------------: | :------------: |
 | address    | Address    |
---

### `get_card_in_account.cdc`

Summary:

This script will return the metadata for the given tokenID in an address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
| tokenID    | UInt64    |
---

### `get_card_totalSupply.cdc`

Summary:

This script will return the total supply of minted HWGarageCardV2 resources
| parameter name | parameter type |
| :------------: | :------------: |
|   N/A  |  N/A   |
---

### `get_cardEditionId_by_packSeriesId.cdc`

Summary:

This script will return a dictionary that maps a series to the current card edition minted for the series key. For example: `{5: 240, 6: 70 }`, means that series 5 has minted card edition 117 and series 6 has minted card edition 66.
| parameter name | parameter type |
| :------------: | :------------: |
|  N/A   |  N/A   |
---

### `get_count_owned_cards.cdc`

Summary:

This script will return the count of cards that are owned for a given address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_count_owned_packs.cdc`

Summary:

This script will return the count of packs that are owned for a given address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_live_series.cdc`

Summary:

This script will return a dictionary for all series that are live. For example, `{5: True}`, means  series 5 is live. If a series is not included then the series is not live and no minting to that series will be successful.
| parameter name | parameter type |
| :------------: | :------------: |
|  N/A   |  N/A   |
---

### `get_owned_cards_by_address.cdc`

Summary:

This script will return the card(s) that are owned for a given address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_owned_packs_by_address.cdc`

Summary:

This script will return the pack(s) that are owned for a given address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_pack_in_account.cdc`

Summary:

This script will return the metadata for a single pack in a given address.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
| tokenID    | UInt64    |
---

### `get_pack_totalSupply.cdc`

Summary:

This script will return the total supply of minted HWGaragePackV2 resources.
| parameter name | parameter type |
| :------------: | :------------: |
|  N/A   |  N/A   |
---

### `get_packEditionId_by_packSeriesId.cdc`

Summary:

This script will return a dictionary that maps a series to the current pack edition minted for the series key. For example: {5: 240, 6: 70 }, means that series 5 has minted pack edition 240 and series 6 has minted pack edition 70.
| parameter name | parameter type |
| :------------: | :------------: |
|  N/A   | N/A    |
---

### `get_redeemable_cards_by_address.cdc`

Summary:

This script will return the metadata for redeemable cards in a given wallet.
| parameter name | parameter type |
| :------------: | :------------: |
| address    | Address    |
---

### `get_token_balance.cdc`

Summary:

This script will return the Flow Token balance for a given wallet address.
| parameter name | parameter type |
| :------------: | :------------: |
| account    | Address    |

---

### `storage_check.cdc`

Summary:

This script will return storage stats for a given Address
| parameter name | parameter type |
| :------------: | :------------: |
| account    | Address    |

---
