# Source: https://github.com/onflow/bridged-usdc/blob/main/README.md

# Flow Bridged USDC

This repo holds the `USDCFlow` smart contract, the Cadence 
Fungible Token contract that acts as the Cadence bridged version of
Flow EVM USDC.

# What is Flow?

Flow is the blockchain for open worlds. Read more about it [here](https://www.flow.com/).

# What is Cadence?

Cadence is a Resource-oriented programming language 
for developing smart contracts for the Flow Blockchain.
Read more about it [here](https://www.cadence-lang.org)

We recommend that anyone who is reading this should have already
completed the [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps) 
so they can build a basic understanding of the programming language.

# USDCFlow

`contracts/USDCFlow.cdc`

| Network       | Contract Address     |
| ------------- | -------------------- |
| Previewnet    | Coming Soon |
| Testnet       | [`0x64adf39cbc354fcb`](https://contractbrowser.com/A.64adf39cbc354fcb.USDCFlow) |
| Mainnet       | [`0xf1ab99c82dee3526`](https://contractbrowser.com/A.f1ab99c82dee3526.USDCFlow) |

This is the contract that defines the Cadence version of Flow USDC. 
Before the Sept 4th Crescendo migration, sent
old `FiatToken` vaults to the `USDCFlow.wrapFiatToken()` function
and received `USDCFlow` vaults back with the exact same balance.

Now, the `USDCFlow` smart contract integrates directly with
the [Flow VM bridge](https://github.com/onflow/flow-evm-bridge) to become
the bridged version of Flow EVM USDC. These tokens are be backed
by real USDC via Ethereum mainnet and Flow EVM, so they retain their value.

This contract is deployed to a different address
and has a different name than the original `FiatToken`,
so contracts that want to support USDC on Flow
will need to use this `USDCFlow` smart contract instead of `FiatToken`.

You can find transactions and scripts for interacting with the `USDCFlow` contract in the `transactions/` directory.

# Testnet Versions

On Flow **Testnet**, the original `USDCFlow` smart contract did not migrate properly,
so a new one had to be deployed in order to function properly. If you are using
`USDCFlow` on testnet, make sure to use the contract deployed at `0x64adf39cbc354fcb`.
This is not an issue on mainnet and the contract at `0xf1ab99c82dee3526` is safe to use.

# Local Development

The contract in this repo is not yet included in the Flow emulator.
If you want to use this contract with the emulator,
you must add it to your `flow.json` and deploy it yourself.

### Prerequisites

- Install Flow CLI on your machine. For instructions, see the [Flow CLI documentation](https://developers.flow.com/tools/flow-cli/install).

Ensure it is installed with:

```sh
flow version
```

### Run the Tests

To run the tests in this repo, simply navigate
to the root directory and run `make test`.
That will run all the tests in the `tests/` directory.

### Additional Resources

- [Old `FiatToken` code](https://github.com/flow-usdc/flow-usdc)
- [Blog Post Announcing Migration from old USDC to new USDC](https://www.flow.com/post/stablecoins-on-flow-evolving-for-interoperability)
- [Flow VM Bridge Github Repo](https://github.com/onflow/flow-evm-bridge/tree/main)