# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/rarible/README.md

# Rarible Folder

This folder contains several scripts for interacting with the mattel nft collections

# Setup
- Make sure you have the most up to date version of the flow crescendo cli: `sudo sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`
- Check the version with `flow-c1 version`

- Generate an emulator private key with: `flow-c1 keys generate`
- Then take the `Private Key` and in `rarible/emulator-acount.pkey` replace `REPLACE_WITH_PRIVATE_KEY` leaving the `0x`
Note: If you mess up this step you will see `Only hexadecimal keys can be used as the emulator service account key.` when trying to start the `emulator`

# Testing

In one terminal open an emulator with `flow-c1 emulator`
NOTE: If you messed up the private key step you will see 

In another terminal Run: `./run_transactions.sh`

This script will:
1. deploy all the necessary smart contracts
2. tests `balance-script.cdc`
3. tests `setup-account-mattel.cdc` to initialize the emulator account for receiving nfts
4. tests `transfer-check.cdc` which makes sure the capability has been created
5. mints several nfts
6. tests `transfer-tx.cdc` which transfers an nft
7. tests `burn-tx.cdc` which burns one of the minted nfts
8. tests `sell-garage.cdc` which tests the sell method on an nft

To test `cancel-order.cdc`
take the `listingResourceID` from the event emited by `sell-garage.cdc` and you it in the following command:
`flow-c1 transactions send ./cancel-order.cdc LISTING_RESOURCE_ID`