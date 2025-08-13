# Source: https://github.com/austinkline/jimbo/blob/main/README.md

# PuffPalz

## Prerequisites

1. [Install NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
2. Install the latest version of the flow cli
    ```
    sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
    ```

## Crescendo migration steps

1. Create a file named `mainnet-key.pkey`
2. Paste the private key for your account into the file
   1. NOTE: DO NOT CHECK THIS FILE IN. All `.pkey` files are added to .gitignore, never change this rule
3. Stage your contract:
    ```
    flow-c1 migrate stage --network mainnet
    ```