# Source: https://developers.flow.com/blockchain-development-tutorials/cross-vm-apps/direct-calls

Direct Calls from Cadence to Flow EVM | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              + [Batched Tx From Scaffold](/blockchain-development-tutorials/cross-vm-apps/introduction)+ [Update Existing wagmi App](/blockchain-development-tutorials/cross-vm-apps/add-to-wagmi)+ [Batched EVM Transactions](/blockchain-development-tutorials/cross-vm-apps/batched-evm-transactions)+ [Direct Calls to Flow EVM](/blockchain-development-tutorials/cross-vm-apps/direct-calls)+ [Interacting with COAs](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa)+ [Cross-VM Bridge](/blockchain-development-tutorials/cross-vm-apps/vm-bridge)* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)* Direct Calls to Flow EVM

On this page

# Direct Calls from Cadence to Flow EVM

Direct calls from Cadence to Flow EVM are essential to allow Cadence smart contracts to interact seamlessly with the EVM environment hosted on the Flow blockchain. These calls facilitate a range of functionalities including state queries and transaction initiations, allowing Cadence contracts to leverage EVM-based tools and assets.

## Make direct calls[​](#make-direct-calls "Direct link to Make direct calls")

### Access Flow EVM[​](#access-flow-evm "Direct link to Access Flow EVM")

To interact with Flow EVM, Cadence contracts must first import `EVM` from its service address:

`_10

import EVM from <ServiceAddress>`

Next, create an `EVMAddress` with a sequence of 20 bytes that represents the EVM address:

`_10

let addr = EVM.EVMAddress(bytes: bytes)`

After you can access an `EVMAddress`, you can query various pieces of state information such as:

* `balance() EVM.Balance` provides the balance of the address. It returns a balance object rather than a basic type to avoid errors when it converts from flow to atto-flow.
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

### Send transactions to Flow EVM[​](#send-transactions-to-flow-evm "Direct link to Send transactions to Flow EVM")

To send transactions to Flow EVM, use the `run` function which executes RLP-encoded transactions. RLP (Recursive Length Prefix) encoding is used to efficiently encode data into a byte-array format, suitable for Ethereum-based environments. Here's an example of how to wrap and send a transaction:

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

When you `run`, it restricts an EVM block to a single EVM transaction, while a future `batchRun` will offer the capability to execute multiple EVM transactions in a batch.

### Handle transaction responses[​](#handle-transaction-responses "Direct link to Handle transaction responses")

It's crucial that your function handles responses correctly to manage the state changes or errors that occur during `EVM` transactions:

When you call `EVM.run`, it's important to understand that this method does not revert the outer Flow transaction. Developers must therefore carefully handle the response based on the `result.Status` of the EVM transaction execution. There are three main outcomes to consider:

* `Status.invalid`: This status indicates that the transaction or call failed at the validation step, such as due to a nonce mismatch. Transactions with this status are not executed or included in a block, which means no state change occurs.
* `Status.failed`: This status is assigned when the transaction has technically succeeded in terms of being processable, but the EVM reports an error as the outcome, such as running out of gas. Importantly, a failed transaction or call is still included in a block. Any attempt to resubmit a failed transaction results in an `invalid` status on the second try due to a now incorrect nonce.
* `Status.successful`: This status appears when the transaction or call is successfully executed and the EVM doesn't report errors.

For scenarios where transaction validity is critical, developers may choose to use the `mustRun` variation, which reverts the transaction in the case of a validation failure. This provides an added layer of error handling.

### Understanding gas usage in EVM transactions[​](#understanding-gas-usage-in-evm-transactions "Direct link to Understanding gas usage in EVM transactions")

Direct calls to Flow EVM require gas. It's important to understand how gas usage is calculated and billed. During the execution of methods that interact with the EVM:

* **Gas Aggregation**: The gas that each call uses is aggregated throughout the transaction.
* **Gas Adjustment**: The total gas used is then adjusted based on a multiplier. This multiplier is determined by the network and the service account can adjust it to reflect operational costs and network conditions.
* **Payment of Gas Fees**: The adjusted total gas amount is added to the overall computation fees of the Flow transaction. The transaction initiator, commonly referred to as the payer, pays these fees.

## Keep learning[​](#keep-learning "Direct link to Keep learning")

For more information and a deeper dive into the `EVMAddress`, `Result`, and `Status` objects, see [the contract here](https://github.com/onflow/flow-go/blob/master/fvm/evm/stdlib/contract.cdc).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cross-vm-apps/direct-calls.md)

Last updated on **Nov 5, 2025** by **cshannon1218**

[Previous

Batched EVM Transactions](/blockchain-development-tutorials/cross-vm-apps/batched-evm-transactions)[Next

Interacting with COAs](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa)

###### Rate this page

😞😐😊

Copy as Markdown

* [Make direct calls](#make-direct-calls)
  + [Access Flow EVM](#access-flow-evm)+ [Send transactions to Flow EVM](#send-transactions-to-flow-evm)+ [Handle transaction responses](#handle-transaction-responses)+ [Understanding gas usage in EVM transactions](#understanding-gas-usage-in-evm-transactions)* [Keep learning](#keep-learning)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.