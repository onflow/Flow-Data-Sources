# Source: https://developers.flow.com/tutorials/cross-vm-apps/direct-calls

Direct Calls from Cadence to Flow EVM | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Secure Randomness with Commit-Reveal in Cadence](/tutorials/commit-reveal-cadence)
* [Tutorials](/tutorials)
* [Token Launch](/tutorials/token-launch)
* [Deploy a Solidity Contract Using Cadence](/tutorials/deploy-solidity-contract)
* [Cross-VM Apps](/tutorials/cross-vm-apps)

  + [Batched Transactions](/tutorials/cross-vm-apps/introduction)
  + [Interacting with COAs](/tutorials/cross-vm-apps/interacting-with-coa)
  + [Direct Calls to Flow EVM](/tutorials/cross-vm-apps/direct-calls)
  + [Batched EVM Transactions](/tutorials/cross-vm-apps/batched-evm-transactions)
  + [Cross-VM Bridge](/tutorials/cross-vm-apps/vm-bridge)
* [FlowtoBooth Tutorials](/tutorials/flowtobooth)

* [Cross-VM Apps](/tutorials/cross-vm-apps)
* Direct Calls to Flow EVM

On this page

# Direct Calls from Cadence to Flow EVM

Direct calls from Cadence to Flow EVM are essential for enabling Cadence smart contracts to interact seamlessly with the EVM environment hosted on the Flow blockchain. These calls facilitate a range of functionalities including state queries and transaction initiations, allowing Cadence contracts to leverage EVM-based tools and assets.

## Making Direct Calls[​](#making-direct-calls "Direct link to Making Direct Calls")

### Accessing Flow EVM[​](#accessing-flow-evm "Direct link to Accessing Flow EVM")

To interact with Flow EVM, Cadence contracts must first import `EVM` from its service address:

`_10

import EVM from <ServiceAddress>`

Next, create an `EVMAddress` with a sequence of 20 bytes representing the EVM address:

`_10

let addr = EVM.EVMAddress(bytes: bytes)`

Once you have access to an `EVMAddress`, you can query various pieces of state information such as:

* `balance() EVM.Balance` provides the balance of the address. It returns a balance object rather than a basic type to avoid errors when converting from flow to atto-flow.
* `nonce() UInt64` retrieves the nonce associated with the address.
* `code(): [UInt8]` fetches the code at the address; it returns the smart contract code if applicable, and is empty otherwise.

`_10

import EVM from <ServiceAddress>

_10

_10

access(all)

_10

fun main(bytes: [UInt8; 20]): EVM.Balance {

_10

let addr = EVM.EVMAddress(bytes: bytes)

_10

let bal = addr.balance()

_10

return bal

_10

}`

Alternatively, you can use the EVM contract's native deserialization to access the balance provided a hex string representing the address:

`_10

import EVM from <ServiceAddress>

_10

_10

access(all)

_10

fun main(addressHex: String): UFix64 {

_10

let addr = EVM.addressFromString(addressHex)

_10

return addr.balance().inFLOW()

_10

}`

### Sending Transactions to Flow EVM[​](#sending-transactions-to-flow-evm "Direct link to Sending Transactions to Flow EVM")

To send transactions to Flow EVM, use the `run` function which executes RLP-encoded transactions. RLP (Recursive Length Prefix) encoding is used to efficiently encode data into a byte-array format, suitable for Ethereum-based environments. Here's an example of wrapping and sending a transaction:

`_13

import EVM from <ServiceAddress>

_13

_13

transaction(rlpEncodedTransaction: [UInt8], coinbaseBytes: [UInt8; 20]) {

_13

_13

prepare(signer: &Account) {

_13

let coinbase = EVM.EVMAddress(bytes: coinbaseBytes)

_13

let result = EVM.run(tx: rlpEncodedTransaction, coinbase: coinbase)

_13

assert(

_13

runResult.status == EVM.Status.successful,

_13

message: "tx was not executed successfully."

_13

)

_13

}

_13

}`

Using `run` restricts an EVM block to a single EVM transaction, while a future `batchRun` will offer the capability to execute multiple EVM transactions in a batch.

### Handling Transaction Responses[​](#handling-transaction-responses "Direct link to Handling Transaction Responses")

Handling responses correctly is crucial to manage the state changes or errors that occur during `EVM` transactions:

When calling `EVM.run`, it's important to understand that this method does not revert the outer Flow transaction. Developers must therefore carefully handle the response based on the `result.Status` of the EVM transaction execution. There are three main outcomes to consider:

* `Status.invalid`: This status indicates that the transaction or call failed at the validation step, such as due to a nonce mismatch. Transactions with this status are not executed or included in a block, meaning no state change occurs.
* `Status.failed`: This status is assigned when the transaction has technically succeeded in terms of being processable, but the EVM reports an error as the outcome, such as running out of gas. Importantly, a failed transaction or call is still included in a block. Attempting to resubmit a failed transaction will result in an `invalid` status on the second try due to a now incorrect nonce.
* `Status.successful`: This status is given when the transaction or call is successfully executed and no errors are reported by the EVM.

For scenarios where transaction validity is critical, developers may choose to use the `mustRun` variation, which reverts the transaction in the case of a validation failure, providing an added layer of error handling.

### Understanding Gas Usage in EVM Transactions[​](#understanding-gas-usage-in-evm-transactions "Direct link to Understanding Gas Usage in EVM Transactions")

Direct calls to Flow EVM require gas, it's important to understand how gas usage is calculated and billed. During the execution of methods that interact with the EVM:

* **Gas Aggregation**: The gas used by each call is aggregated throughout the transaction.
* **Gas Adjustment**: The total gas used is then adjusted based on a multiplier. This multiplier is determined by the network and can be adjusted by the service account to reflect operational costs and network conditions.
* **Payment of Gas Fees**: The adjusted total gas amount is added to the overall computation fees of the Flow transaction. These fees are paid by the transaction initiator, commonly referred to as the payer.

## Keep Learning[​](#keep-learning "Direct link to Keep Learning")

For more information and a deeper dive into the `EVMAddress`, `Result`, and `Status` objects, see [the contract here](https://github.com/onflow/flow-go/blob/master/fvm/evm/stdlib/contract.cdc).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/cross-vm-apps/direct-calls.md)

Last updated on **Mar 26, 2025** by **Brian Doyle**

[Previous

Interacting with COAs](/tutorials/cross-vm-apps/interacting-with-coa)[Next

Batched EVM Transactions](/tutorials/cross-vm-apps/batched-evm-transactions)

###### Rate this page

😞😐😊

* [Making Direct Calls](#making-direct-calls)
  + [Accessing Flow EVM](#accessing-flow-evm)
  + [Sending Transactions to Flow EVM](#sending-transactions-to-flow-evm)
  + [Handling Transaction Responses](#handling-transaction-responses)
  + [Understanding Gas Usage in EVM Transactions](#understanding-gas-usage-in-evm-transactions)
* [Keep Learning](#keep-learning)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.