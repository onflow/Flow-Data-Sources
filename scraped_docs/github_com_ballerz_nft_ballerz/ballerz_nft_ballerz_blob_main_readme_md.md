# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/README.md

# Ballerz

## Contract staging instructions

1. run `npm i`
1. make a file called `mainnet-account.pkey`
1. paste your account private key into the file (NOTE: This file is listed in this repo's .gitignore, so it will not be committed)
1. Run the command `flow-c1 migrate stage --network mainnet`

## Testnet staging instructions

You can follow the below steps to stage your contract in testnet for practice. This has absolutely **NO** impact on mainnet,
and can be done as many times as you would like.

1. generate a new key using `flow keys generate`
1. make a file called `testnet-account.pkey`
1. copy the public key, and go to https://testnet-faucet.onflow.org/ to give it some flow tokens
1. copy the generated address from the faucet and paste it into the `testnet-account` section in your `flow.json`:
    ```
    "testnet-account": {
      "address": "0x1", <-- Update to your new address
      "key": {
        "type": "file",
        "location": "testnet-account.pkey"
      }
    },
    ```
1. check out the branch `pre-crescendo`, which has the Ballerz current contract code
    ```
    git pull
    git checkout pre-crescendo
    ```
1. install all contract dependencies
    ```
    npm i
    ```
1. deploy to testnet
    ```
    flow project deploy -n testnet --update
    ```
1. check out your main branch with crescendo code in it
    ```
    git checkout main
    ```
1. Install all contract dependencies (NOTE: we are reinstalling to pull in crescendo code)
1. Run the staging command
    ```
    flow-c1 migrate stage --network testnet
    ```