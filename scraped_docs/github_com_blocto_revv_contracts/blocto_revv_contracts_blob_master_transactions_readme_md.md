# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/README.md

# Token
### Setup BloctoToken Minter for Mining
```
flow transactions build ./transactions/setupTeleportAdmin.cdc 1000000.0 --network mainnet --proposer 0x04ee69443dedf0e4 --proposer-key-index 0 --authorizer 0x04ee69443dedf0e4 --authorizer 0x08a13c66a11dea60 --payer 0x08a13c66a11dea60 --gas-limit 1000 -x payload --save ./build/unsigned.rlp

flow transactions sign ./build/unsigned.rlp --signer revv-admin-mainnet --filter payload --save ./build/signed-1.rlp

flow transactions sign ./build/signed-1.rlp --signer revv-teleport-admin-mainnet --filter payload --save ./build/signed-2.rlp

flow transactions send-signed --network mainnet ./build/signed-2.rlp
```
