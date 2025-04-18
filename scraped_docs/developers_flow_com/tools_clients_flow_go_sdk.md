# Source: https://developers.flow.com/tools/clients/flow-go-sdk

Flow Go SDK | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)

    - [Migration Guide v0.25.0](/tools/clients/flow-go-sdk/migration-v0.25.0)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Client Tools](/tools/clients)
* Flow Go SDK

On this page

# Flow Go SDK

[![Logo](/images/tools/sdk-banner.svg)](/tooling/intro)

[**View on GitHub**](https://github.com/onflow/flow-go-sdk)  
  
[SDK Specifications](../fcl-js/sdk-guidelines/)[Contribute](https://github.com/onflow/flow-go-sdk/blob/master/CONTRIBUTING.md)[Report a Bug](https://github.com/onflow/flow-go-sdk/issues)

  

## Overview[​](#overview "Direct link to Overview")

This reference documents all the methods available in the SDK, and explains in detail how these methods work.
SDKs are open source, and you can use them according to the licence.

The library client specifications can be found here:

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client)

## Getting Started[​](#getting-started "Direct link to Getting Started")

### Installing[​](#installing "Direct link to Installing")

The recommended way to install Go Flow SDK is by using Go modules.

If you already initialized your Go project, you can run the following command in your terminal:

`_10

go get github.com/onflow/flow-go-sdk`

It's usually good practice to pin your dependencies to a specific version.
Refer to the [SDK releases](https://github.com/onflow/flow-go-sdk/tags) page to identify the latest version.

### Importing the Library[​](#importing-the-library "Direct link to Importing the Library")

After the library has been installed you can import it.

`_10

import "github.com/onflow/flow-go-sdk"`

## Connect[​](#connect "Direct link to Connect")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#New)

The Go SDK library uses HTTP or gRPC APIs to communicate with the access nodes and it must be configured with correct access node API URL.
The library provides default factories for connecting to Flow AN APIs and you can easily switch between HTTP or gRPC if you use the provided client interface.

You can check more examples for creating clients in the examples:
**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/http_grpc_clients/main.go)**

Basic Example:

`_10

// common client interface

_10

var flowClient client.Client

_10

_10

// initialize an http emulator client

_10

flowClient, err := http.NewClient(http.EmulatorHost)

_10

_10

// initialize a gPRC emulator client

_10

flowClient, err = grpc.NewClient(grpc.EmulatorHost)`

You can also initialize an HTTP client or gRPC client directly which will offer you access to network specific options,
but be aware you won't be able to easily switch between those since they don't implement a common interface. This is only
advisable if the implementation needs the access to those advanced options.
Advanced Example:

`_10

// initialize http specific client

_10

httpClient, err := http.NewHTTPClient(http.EMULATOR_URL)

_10

_10

// initialize grpc specific client

_10

grpcClient, err := grpc.NewGRPCClient(

_10

grpc.EMULATOR_URL,

_10

grpcOpts.WithTransportCredentials(insecure.NewCredentials()),

_10

)`

## Querying the Flow Network[​](#querying-the-flow-network "Direct link to Querying the Flow Network")

After you have established a connection with an access node, you can query the
Flow network to retrieve data about blocks, accounts, events and transactions. We will explore
how to retrieve each of these entities in the sections below.

### Get Blocks[​](#get-blocks "Direct link to Get Blocks")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetBlockByHeight)

Query the network for block by id, height or get the latest block.

📖 **Block ID** is SHA3-256 hash of the entire block payload. This hash is stored as an ID field on any block response object (ie. response from `GetLatestBlock`).

📖 **Block height** expresses the height of the block on the chain. The latest block height increases by one for every valid block produced.

#### Examples[​](#examples "Direct link to Examples")

This example depicts ways to get the latest block as well as any other block by height or ID:

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/get_blocks/main.go)**

`_26

func demo() {

_26

ctx := context.Background()

_26

flowClient := examples.NewFlowClient()

_26

_26

// get the latest sealed block

_26

isSealed := true

_26

latestBlock, err := flowClient.GetLatestBlock(ctx, isSealed)

_26

printBlock(latestBlock, err)

_26

_26

// get the block by ID

_26

blockID := latestBlock.ID.String()

_26

blockByID, err := flowClient.GetBlockByID(ctx, flow.HexToID(blockID))

_26

printBlock(blockByID, err)

_26

_26

// get block by height

_26

blockByHeight, err := flowClient.GetBlockByHeight(ctx, 0)

_26

printBlock(blockByHeight, err)

_26

}

_26

_26

func printBlock(block *flow.Block, err error) {

_26

examples.Handle(err)

_26

_26

fmt.Printf("\nID: %s\n", block.ID)

_26

fmt.Printf("height: %d\n", block.Height)

_26

fmt.Printf("timestamp: %s\n\n", block.Timestamp)

_26

}`

Result output:

`_13

ID: 835dc83939141097aa4297aa6cf69fc600863e3b5f9241a0d7feac1868adfa4f

_13

height: 10

_13

timestamp: 2021-10-06 15:06:07.105382 +0000 UTC

_13

_13

_13

ID: 835dc83939141097aa4297aa6cf69fc600863e3b5f9241a0d7feac1868adfa4f

_13

height: 10

_13

timestamp: 2021-10-06 15:06:07.105382 +0000 UTC

_13

_13

_13

ID: 7bc42fe85d32ca513769a74f97f7e1a7bad6c9407f0d934c2aa645ef9cf613c7

_13

height: 0

_13

timestamp: 2018-12-19 22:32:30.000000042 +0000 UTC`

### Get Account[​](#get-account "Direct link to Get Account")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetAccount)

Retrieve any account from Flow network's latest block or from a specified block height.
The `GetAccount` method is actually an alias for the get account at latest block method.

📖 **Account address** is a unique account identifier. Be mindful about the `0x` prefix, you should use the prefix as a default representation but be careful and safely handle user inputs without the prefix.

An account includes the following data:

* Address: the account address.
* Balance: balance of the account.
* Contracts: list of contracts deployed to the account.
* Keys: list of keys associated with the account.

#### Examples[​](#examples-1 "Direct link to Examples")

Example depicts ways to get an account at the latest block and at a specific block height:

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/get_accounts/main.go)**

`_22

func demo() {

_22

ctx := context.Background()

_22

flowClient := examples.NewFlowClient()

_22

_22

// get account from the latest block

_22

address := flow.HexToAddress("f8d6e0586b0a20c7")

_22

account, err := flowClient.GetAccount(ctx, address)

_22

printAccount(account, err)

_22

_22

// get account from the block by height 0

_22

account, err = flowClient.GetAccountAtBlockHeight(ctx, address, 0)

_22

printAccount(account, err)

_22

}

_22

_22

func printAccount(account *flow.Account, err error) {

_22

examples.Handle(err)

_22

_22

fmt.Printf("\nAddress: %s", account.Address.String())

_22

fmt.Printf("\nBalance: %d", account.Balance)

_22

fmt.Printf("\nContracts: %d", len(account.Contracts))

_22

fmt.Printf("\nKeys: %d\n", len(account.Keys))

_22

}`

Result output:

`_10

Address: f8d6e0586b0a20c7

_10

Balance: 999999999999600000

_10

Contracts: 2

_10

Keys: 1

_10

_10

Address: f8d6e0586b0a20c7

_10

Balance: 999999999999600000

_10

Contracts: 2

_10

Keys: 1`

### Get Transactions[​](#get-transactions "Direct link to Get Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetTransaction)

Retrieve transactions from the network by providing a transaction ID. After a transaction has been submitted, you can also get the transaction result to check the status.

📖 **Transaction ID** is a hash of the encoded transaction payload and can be calculated before submitting the transaction to the network.

⚠️ The transaction ID provided must be from the current spork.

📖 **Transaction status** represents the state of transaction in the blockchain. Status can change until it is sealed.

| Status | Final | Description |
| --- | --- | --- |
| UNKNOWN | ❌ | The transaction has not yet been seen by the network |
| PENDING | ❌ | The transaction has not yet been included in a block |
| FINALIZED | ❌ | The transaction has been included in a block |
| EXECUTED | ❌ | The transaction has been executed but the result has not yet been sealed |
| SEALED | ✅ | The transaction has been executed and the result is sealed in a block |
| EXPIRED | ✅ | The transaction reference block is outdated before being executed |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/get_transactions/main.go)**

`_26

func demo(txID flow.Identifier) {

_26

ctx := context.Background()

_26

flowClient := examples.NewFlowClient()

_26

_26

tx, err := flowClient.GetTransaction(ctx, txID)

_26

printTransaction(tx, err)

_26

_26

txr, err := flowClient.GetTransactionResult(ctx, txID)

_26

printTransactionResult(txr, err)

_26

}

_26

_26

func printTransaction(tx *flow.Transaction, err error) {

_26

examples.Handle(err)

_26

_26

fmt.Printf("\nID: %s", tx.ID().String())

_26

fmt.Printf("\nPayer: %s", tx.Payer.String())

_26

fmt.Printf("\nProposer: %s", tx.ProposalKey.Address.String())

_26

fmt.Printf("\nAuthorizers: %s", tx.Authorizers)

_26

}

_26

_26

func printTransactionResult(txr *flow.TransactionResult, err error) {

_26

examples.Handle(err)

_26

_26

fmt.Printf("\nStatus: %s", txr.Status.String())

_26

fmt.Printf("\nError: %v", txr.Error)

_26

}`

Example output:

`_10

ID: fb1272c57cdad79acf2fcf37576d82bf760e3008de66aa32a900c8cd16174e1c

_10

Payer: f8d6e0586b0a20c7

_10

Proposer: f8d6e0586b0a20c7

_10

Authorizers: []

_10

Status: SEALED

_10

Error: <nil>`

### Get Events[​](#get-events "Direct link to Get Events")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetEventsForBlockIDs)

Retrieve events by a given type in a specified block height range or through a list of block IDs.

📖 **Event type** is a string that follow a standard format:

`_10

A.{contract address}.{contract name}.{event name}`

Please read more about [events in the documentation](/build/core-contracts/flow-token). The exception to this standard are
core events, and you should read more about them in [this document](https://cadence-lang.org/docs/language/core-events).

📖 **Block height range** expresses the height of the start and end block in the chain.

#### Examples[​](#examples-2 "Direct link to Examples")

Example depicts ways to get events within block range or by block IDs:

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/get_events/main.go)**

`_34

func demo(deployedContract *flow.Account, runScriptTx *flow.Transaction) {

_34

ctx := context.Background()

_34

flowClient := examples.NewFlowClient()

_34

_34

// Query for account creation events by type

_34

result, err := flowClient.GetEventsForHeightRange(ctx, "flow.AccountCreated", 0, 30)

_34

printEvents(result, err)

_34

_34

// Query for our custom event by type

_34

customType := fmt.Sprintf("AC.%s.EventDemo.EventDemo.Add", deployedContract.Address.Hex())

_34

result, err = flowClient.GetEventsForHeightRange(ctx, customType, 0, 10)

_34

printEvents(result, err)

_34

_34

// Get events directly from transaction result

_34

txResult, err := flowClient.GetTransactionResult(ctx, runScriptTx.ID())

_34

examples.Handle(err)

_34

printEvent(txResult.Events)

_34

}

_34

_34

func printEvents(result []client.BlockEvents, err error) {

_34

examples.Handle(err)

_34

_34

for _, block := range result {

_34

printEvent(block.Events)

_34

}

_34

}

_34

_34

func printEvent(events []flow.Event) {

_34

for _, event := range events {

_34

fmt.Printf("\n\nType: %s", event.Type)

_34

fmt.Printf("\nValues: %v", event.Value)

_34

fmt.Printf("\nTransaction ID: %s", event.TransactionID)

_34

}

_34

}`

Example output:

`_13

Type: flow.AccountCreated

_13

Values: flow.AccountCreated(address: 0xfd43f9148d4b725d)

_13

Transaction ID: ba9d53c8dcb0f9c2f854f93da8467a22d053eab0c540bde0b9ca2f7ad95eb78e

_13

_13

Type: flow.AccountCreated

_13

Values: flow.AccountCreated(address: 0xeb179c27144f783c)

_13

Transaction ID: 8ab7bfef3de1cf8b2ffb36559446100bf4129a9aa88d6bc59f72a467acf0c801

_13

_13

...

_13

_13

Type: A.eb179c27144f783c.EventDemo.Add

_13

Values: A.eb179c27144f783c.EventDemo.Add(x: 2, y: 3, sum: 5)

_13

Transaction ID: f3a2e33687ad23b0e02644ebbdcd74a7cd8ea7214065410a8007811d0bcbd353`

### Get Collections[​](#get-collections "Direct link to Get Collections")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetCollection)

Retrieve a batch of transactions that have been included in the same block, known as ***collections***.
Collections are used to improve consensus throughput by increasing the number of transactions per block and they act as a link between a block and a transaction.

📖 **Collection ID** is SHA3-256 hash of the collection payload.

Example retrieving a collection:

`_15

func demo(exampleCollectionID flow.Identifier) {

_15

ctx := context.Background()

_15

flowClient := examples.NewFlowClient()

_15

_15

// get collection by ID

_15

collection, err := flowClient.GetCollection(ctx, exampleCollectionID)

_15

printCollection(collection, err)

_15

}

_15

_15

func printCollection(collection *flow.Collection, err error) {

_15

examples.Handle(err)

_15

_15

fmt.Printf("\nID: %s", collection.ID().String())

_15

fmt.Printf("\nTransactions: %s", collection.TransactionIDs)

_15

}`

Example output:

`_10

ID: 3d7b8037381f2497d83f2f9e09422c036aae2a59d01a7693fb6003b4d0bc3595

_10

Transactions: [cf1184e3de4bd9a7232ca3d0b9dd2cfbf96c97888298b81a05c086451fa52ec1]`

### Execute Scripts[​](#execute-scripts "Direct link to Execute Scripts")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.ExecuteScriptAtLatestBlock)

Scripts allow you to write arbitrary non-mutating Cadence code on the Flow blockchain and return data. You can learn more about [Cadence and scripts here](https://cadence-lang.org/docs/language), but we are now only interested in executing the script code and getting back the data.

We can execute a script using the latest state of the Flow blockchain or we can choose to execute the script at a specific time in history defined by a block height or block ID.

📖 **Block ID** is SHA3-256 hash of the entire block payload, but you can get that value from the block response properties.

📖 **Block height** expresses the height of the block in the chain.

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/execute_script/main.go)**

`_62

func demo() {

_62

ctx := context.Background()

_62

flowClient := examples.NewFlowClient()

_62

_62

script := []byte(`

_62

access(all) fun main(a: Int): Int {

_62

return a + 10

_62

}

_62

`)

_62

args := []cadence.Value{ cadence.NewInt(5) }

_62

value, err := flowClient.ExecuteScriptAtLatestBlock(ctx, script, args)

_62

_62

examples.Handle(err)

_62

fmt.Printf("\nValue: %s", value.String())

_62

_62

complexScript := []byte(`

_62

access(all) struct User {

_62

access(all) var balance: UFix64

_62

access(all) var address: Address

_62

access(all) var name: String

_62

_62

init(name: String, address: Address, balance: UFix64) {

_62

self.name = name

_62

self.address = address

_62

self.balance = balance

_62

}

_62

}

_62

_62

access(all) fun main(name: String): User {

_62

return User(

_62

name: name,

_62

address: 0x1,

_62

balance: 10.0

_62

)

_62

}

_62

`)

_62

args = []cadence.Value{ cadence.NewString("Dete") }

_62

value, err = flowClient.ExecuteScriptAtLatestBlock(ctx, complexScript, args)

_62

printComplexScript(value, err)

_62

}

_62

_62

type User struct {

_62

balance uint64

_62

address flow.Address

_62

name string

_62

}

_62

_62

func printComplexScript(value cadence.Value, err error) {

_62

examples.Handle(err)

_62

fmt.Printf("\nString value: %s", value.String())

_62

_62

s := value.(cadence.Struct)

_62

u := User{

_62

balance: s.Fields[0].ToGoValue().(uint64),

_62

address: s.Fields[1].ToGoValue().([flow.AddressLength]byte),

_62

name: s.Fields[2].ToGoValue().(string),

_62

}

_62

_62

fmt.Printf("\nName: %s", u.name)

_62

fmt.Printf("\nAddress: %s", u.address.String())

_62

fmt.Printf("\nBalance: %d", u.balance)

_62

}`

Example output:

`_10

Value: 15

_10

String value: s.34a17571e1505cf6770e6ef16ca387e345e9d54d71909f23a7ec0d671cd2faf5.User(balance: 10.00000000, address: 0x1, name: "Dete")

_10

Name: Dete

_10

Address: 0000000000000001

_10

Balance: 1000000000`

## Mutate Flow Network[​](#mutate-flow-network "Direct link to Mutate Flow Network")

Flow, like most blockchains, allows anybody to submit a transaction that mutates the shared global chain state. A transaction is an object that holds a payload, which describes the state mutation, and one or more authorizations that permit the transaction to mutate the state owned by specific accounts.

Transaction data is composed and signed with help of the SDK. The signed payload of transaction then gets submitted to the access node API. If a transaction is invalid or the correct number of authorizing signatures are not provided, it gets rejected.

Executing a transaction requires couple of steps:

* [Building transaction](#build-the-transaction).
* [Signing transaction](#sign-transactions).
* [Sending transaction](#send-transactions).

## Transactions[​](#transactions "Direct link to Transactions")

A transaction is nothing more than a signed set of data that includes script code which are instructions on how to mutate the network state and properties that define and limit it's execution. All these properties are explained bellow.

📖 **Script** field is the portion of the transaction that describes the state mutation logic. On Flow, transaction logic is written in [Cadence](https://cadence-lang.org/docs). Here is an example transaction script:

`_10

transaction(greeting: String) {

_10

execute {

_10

log(greeting.concat(", World!"))

_10

}

_10

}`

📖 **Arguments**. A transaction can accept zero or more arguments that are passed into the Cadence script. The arguments on the transaction must match the number and order declared in the Cadence script. Sample script from above accepts a single `String` argument.

📖 **[Proposal key](/build/basics/transactions#proposal-key)** must be provided to act as a sequence number and prevent reply and other potential attacks.

Each account key maintains a separate transaction sequence counter; the key that lends its sequence number to a transaction is called the proposal key.

A proposal key contains three fields:

* Account address
* Key index
* Sequence number

A transaction is only valid if its declared sequence number matches the current on-chain sequence number for that key. The sequence number increments by one after the transaction is executed.

📖 **[Payer](/build/basics/transactions#signer-roles)** is the account that pays the fees for the transaction. A transaction must specify exactly one payer. The payer is only responsible for paying the network and gas fees; the transaction is not authorized to access resources or code stored in the payer account.

📖 **[Authorizers](/build/basics/transactions#signer-roles)** are accounts that authorize a transaction to read and mutate their resources. A transaction can specify zero or more authorizers, depending on how many accounts the transaction needs to access.

The number of authorizers on the transaction must match the number of &Account parameters declared in the prepare statement of the Cadence script.

Example transaction with multiple authorizers:

`_10

transaction {

_10

prepare(authorizer1: &Account, authorizer2: &Account) { }

_10

}`

#### Gas Limit[​](#gas-limit "Direct link to Gas Limit")

📖 **Gas limit** is the limit on the amount of computation a transaction requires, and it will abort if it exceeds its gas limit.
Cadence uses metering to measure the number of operations per transaction. You can read more about it in the [Cadence documentation](https://cadence-lang.org/docs).

The gas limit depends on the complexity of the transaction script. Until dedicated gas estimation tooling exists, it's best to use the emulator to test complex transactions and determine a safe limit.

#### Reference Block[​](#reference-block "Direct link to Reference Block")

📖 **Reference block** specifies an expiration window (measured in blocks) during which a transaction is considered valid by the network.
A transaction will be rejected if it is submitted past its expiry block. Flow calculates transaction expiry using the *reference block* field on a transaction.
A transaction expires after `600` blocks are committed on top of the reference block, which takes about 10 minutes at average Mainnet block rates.

### Build Transactions[​](#build-transactions "Direct link to Build Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk#Transaction)

Building a transaction involves setting the required properties explained above and producing a transaction object.

Here we define a simple transaction script that will be used to execute on the network and serve as a good learning example.

`_12

transaction(greeting: String) {

_12

_12

let guest: Address

_12

_12

prepare(authorizer: &Account) {

_12

self.guest = authorizer.address

_12

}

_12

_12

execute {

_12

log(greeting.concat(",").concat(self.guest.toString()))

_12

}

_12

}`

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/transaction_signing/single_party/main.go)**

`_57

import (

_57

"context"

_57

"os"

_57

"github.com/onflow/flow-go-sdk"

_57

"github.com/onflow/flow-go-sdk/client"

_57

)

_57

_57

func main() {

_57

_57

greeting, err := os.ReadFile("Greeting2.cdc")

_57

if err != nil {

_57

panic("failed to load Cadence script")

_57

}

_57

_57

proposerAddress := flow.HexToAddress("9a0766d93b6608b7")

_57

proposerKeyIndex := 3

_57

_57

payerAddress := flow.HexToAddress("631e88ae7f1d7c20")

_57

authorizerAddress := flow.HexToAddress("7aad92e5a0715d21")

_57

_57

var accessAPIHost string

_57

_57

// Establish a connection with an access node

_57

flowClient := examples.NewFlowClient()

_57

_57

// Get the latest sealed block to use as a reference block

_57

latestBlock, err := flowClient.GetLatestBlockHeader(context.Background(), true)

_57

if err != nil {

_57

panic("failed to fetch latest block")

_57

}

_57

_57

// Get the latest account info for this address

_57

proposerAccount, err := flowClient.GetAccountAtLatestBlock(context.Background(), proposerAddress)

_57

if err != nil {

_57

panic("failed to fetch proposer account")

_57

}

_57

_57

// Get the latest sequence number for this key

_57

sequenceNumber := proposerAccount.Keys[proposerKeyIndex].SequenceNumber

_57

_57

tx := flow.NewTransaction().

_57

SetScript(greeting).

_57

SetComputeLimit(100).

_57

SetReferenceBlockID(latestBlock.ID).

_57

SetProposalKey(proposerAddress, proposerKeyIndex, sequenceNumber).

_57

SetPayer(payerAddress).

_57

AddAuthorizer(authorizerAddress)

_57

_57

// Add arguments last

_57

_57

hello := cadence.NewString("Hello")

_57

_57

err = tx.AddArgument(hello)

_57

if err != nil {

_57

panic("invalid argument")

_57

}

_57

}`

After you have successfully [built a transaction](#build-the-transaction) the next step in the process is to sign it.

### Sign Transactions[​](#sign-transactions "Direct link to Sign Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk#Transaction.SignEnvelope)

Flow introduces new concepts that allow for more flexibility when creating and signing transactions.
Before trying the examples below, we recommend that you read through the [transaction signature documentation](../../../build/basics/transactions.md.

After you have successfully [built a transaction](#build-the-transaction) the next step in the process is to sign it. Flow transactions have envelope and payload signatures, and you should learn about each in the [signature documentation](/build/basics/transactions).

Quick example of building a transaction:

`_16

import (

_16

"github.com/onflow/flow-go-sdk"

_16

"github.com/onflow/flow-go-sdk/crypto"

_16

)

_16

_16

var (

_16

myAddress flow.Address

_16

myAccountKey flow.AccountKey

_16

myPrivateKey crypto.PrivateKey

_16

)

_16

_16

tx := flow.NewTransaction().

_16

SetScript([]byte("transaction { execute { log(\"Hello, World!\") } }")).

_16

SetComputeLimit(100).

_16

SetProposalKey(myAddress, myAccountKey.Index, myAccountKey.SequenceNumber).

_16

SetPayer(myAddress)`

Transaction signing is done through the `crypto.Signer` interface. The simplest (and least secure) implementation of `crypto.Signer` is `crypto.InMemorySigner`.

Signatures can be generated more securely using keys stored in a hardware device such as an [HSM](https://en.wikipedia.org/wiki/Hardware_security_module). The `crypto.Signer` interface is intended to be flexible enough to support a variety of signer implementations and is not limited to in-memory implementations.

Simple signature example:

`_10

// construct a signer from your private key and configured hash algorithm

_10

mySigner, err := crypto.NewInMemorySigner(myPrivateKey, myAccountKey.HashAlgo)

_10

if err != nil {

_10

panic("failed to create a signer")

_10

}

_10

_10

err = tx.SignEnvelope(myAddress, myAccountKey.Index, mySigner)

_10

if err != nil {

_10

panic("failed to sign transaction")

_10

}`

Flow supports great flexibility when it comes to transaction signing, we can define multiple authorizers (multi-sig transactions) and have different payer account than proposer. We will explore advanced signing scenarios bellow.

### [Single party, single signature](/build/basics/transactions#single-party-single-signature)[​](#single-party-single-signature "Direct link to single-party-single-signature")

* Proposer, payer and authorizer are the same account (`0x01`).
* Only the envelope must be signed.
* Proposal key must have full signing weight.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#single-party-single-signature)**

`_22

account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))

_22

_22

key1 := account1.Keys[0]

_22

_22

// create signer from securely-stored private key

_22

key1Signer := getSignerForKey1()

_22

_22

referenceBlock, _ := flow.GetLatestBlock(ctx, true)

_22

tx := flow.NewTransaction().

_22

SetScript([]byte(`

_22

transaction {

_22

prepare(signer: &Account) { log(signer.address) }

_22

}

_22

`)).

_22

SetComputeLimit(100).

_22

SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber).

_22

SetReferenceBlockID(referenceBlock.ID).

_22

SetPayer(account1.Address).

_22

AddAuthorizer(account1.Address)

_22

_22

// account 1 signs the envelope with key 1

_22

err := tx.SignEnvelope(account1.Address, key1.Index, key1Signer)`

### [Single party, multiple signatures](/build/basics/transactions#single-party-multiple-signatures)[​](#single-party-multiple-signatures "Direct link to single-party-multiple-signatures")

* Proposer, payer and authorizer are the same account (`0x01`).
* Only the envelope must be signed.
* Each key has weight 500, so two signatures are required.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 500 |
| `0x01` | 2 | 500 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#single-party-multiple-signatures)**

`_27

account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))

_27

_27

key1 := account1.Keys[0]

_27

key2 := account1.Keys[1]

_27

_27

// create signers from securely-stored private keys

_27

key1Signer := getSignerForKey1()

_27

key2Signer := getSignerForKey2()

_27

_27

referenceBlock, _ := flow.GetLatestBlock(ctx, true)

_27

tx := flow.NewTransaction().

_27

SetScript([]byte(`

_27

transaction {

_27

prepare(signer: &Account) { log(signer.address) }

_27

}

_27

`)).

_27

SetComputeLimit(100).

_27

SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber).

_27

SetReferenceBlockID(referenceBlock.ID).

_27

SetPayer(account1.Address).

_27

AddAuthorizer(account1.Address)

_27

_27

// account 1 signs the envelope with key 1

_27

err := tx.SignEnvelope(account1.Address, key1.Index, key1Signer)

_27

_27

// account 1 signs the envelope with key 2

_27

err = tx.SignEnvelope(account1.Address, key2.Index, key2Signer)`

### [Multiple parties](/build/basics/transactions#multiple-parties)[​](#multiple-parties "Direct link to multiple-parties")

* Proposer and authorizer are the same account (`0x01`).
* Payer is a separate account (`0x02`).
* Account `0x01` signs the payload.
* Account `0x02` signs the envelope.
  + Account `0x02` must sign last since it is the payer.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |
| `0x02` | 3 | 1000 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#multiple-parties)**

`_29

account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))

_29

account2, _ := c.GetAccount(ctx, flow.HexToAddress("02"))

_29

_29

key1 := account1.Keys[0]

_29

key3 := account2.Keys[0]

_29

_29

// create signers from securely-stored private keys

_29

key1Signer := getSignerForKey1()

_29

key3Signer := getSignerForKey3()

_29

_29

referenceBlock, _ := flow.GetLatestBlock(ctx, true)

_29

tx := flow.NewTransaction().

_29

SetScript([]byte(`

_29

transaction {

_29

prepare(signer: &Account) { log(signer.address) }

_29

}

_29

`)).

_29

SetComputeLimit(100).

_29

SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber).

_29

SetReferenceBlockID(referenceBlock.ID).

_29

SetPayer(account2.Address).

_29

AddAuthorizer(account1.Address)

_29

_29

// account 1 signs the payload with key 1

_29

err := tx.SignPayload(account1.Address, key1.Index, key1Signer)

_29

_29

// account 2 signs the envelope with key 3

_29

// note: payer always signs last

_29

err = tx.SignEnvelope(account2.Address, key3.Index, key3Signer)`

### [Multiple parties, two authorizers](/build/basics/transactions#multiple-parties)[​](#multiple-parties-two-authorizers "Direct link to multiple-parties-two-authorizers")

* Proposer and authorizer are the same account (`0x01`).
* Payer is a separate account (`0x02`).
* Account `0x01` signs the payload.
* Account `0x02` signs the envelope.
  + Account `0x02` must sign last since it is the payer.
* Account `0x02` is also an authorizer to show how to include two `&Account` objects into an transaction

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |
| `0x02` | 3 | 1000 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#multiple-parties-two-authorizers)**

`_33

account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))

_33

account2, _ := c.GetAccount(ctx, flow.HexToAddress("02"))

_33

_33

key1 := account1.Keys[0]

_33

key3 := account2.Keys[0]

_33

_33

// create signers from securely-stored private keys

_33

key1Signer := getSignerForKey1()

_33

key3Signer := getSignerForKey3()

_33

_33

referenceBlock, _ := flow.GetLatestBlock(ctx, true)

_33

tx := flow.NewTransaction().

_33

SetScript([]byte(`

_33

transaction {

_33

prepare(signer1: &Account, signer2: &Account) {

_33

log(signer.address)

_33

log(signer2.address)

_33

}

_33

}

_33

`)).

_33

SetComputeLimit(100).

_33

SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber).

_33

SetReferenceBlockID(referenceBlock.ID).

_33

SetPayer(account2.Address).

_33

AddAuthorizer(account1.Address).

_33

AddAuthorizer(account2.Address)

_33

_33

// account 1 signs the payload with key 1

_33

err := tx.SignPayload(account1.Address, key1.Index, key1Signer)

_33

_33

// account 2 signs the envelope with key 3

_33

// note: payer always signs last

_33

err = tx.SignEnvelope(account2.Address, key3.Index, key3Signer)`

### [Multiple parties, multiple signatures](/build/basics/transactions#multiple-parties)[​](#multiple-parties-multiple-signatures "Direct link to multiple-parties-multiple-signatures")

* Proposer and authorizer are the same account (`0x01`).
* Payer is a separate account (`0x02`).
* Account `0x01` signs the payload.
* Account `0x02` signs the envelope.
  + Account `0x02` must sign last since it is the payer.
* Both accounts must sign twice (once with each of their keys).

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 500 |
| `0x01` | 2 | 500 |
| `0x02` | 3 | 500 |
| `0x02` | 4 | 500 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#multiple-parties-multiple-signatures)**

`_40

account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))

_40

account2, _ := c.GetAccount(ctx, flow.HexToAddress("02"))

_40

_40

key1 := account1.Keys[0]

_40

key2 := account1.Keys[1]

_40

key3 := account2.Keys[0]

_40

key4 := account2.Keys[1]

_40

_40

// create signers from securely-stored private keys

_40

key1Signer := getSignerForKey1()

_40

key2Signer := getSignerForKey1()

_40

key3Signer := getSignerForKey3()

_40

key4Signer := getSignerForKey4()

_40

_40

referenceBlock, _ := flow.GetLatestBlock(ctx, true)

_40

tx := flow.NewTransaction().

_40

SetScript([]byte(`

_40

transaction {

_40

prepare(signer: &Account) { log(signer.address) }

_40

}

_40

`)).

_40

SetComputeLimit(100).

_40

SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber).

_40

SetReferenceBlockID(referenceBlock.ID).

_40

SetPayer(account2.Address).

_40

AddAuthorizer(account1.Address)

_40

_40

// account 1 signs the payload with key 1

_40

err := tx.SignPayload(account1.Address, key1.Index, key1Signer)

_40

_40

// account 1 signs the payload with key 2

_40

err = tx.SignPayload(account1.Address, key2.Index, key2Signer)

_40

_40

// account 2 signs the envelope with key 3

_40

// note: payer always signs last

_40

err = tx.SignEnvelope(account2.Address, key3.Index, key3Signer)

_40

_40

// account 2 signs the envelope with key 4

_40

// note: payer always signs last

_40

err = tx.SignEnvelope(account2.Address, key4.Index, key4Signer)`

### Send Transactions[​](#send-transactions "Direct link to Send Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.SendTransaction)

After a transaction has been [built](#build-the-transaction) and [signed](#sign-transactions), it can be sent to the Flow blockchain where it will be executed. If sending was successful you can then [retrieve the transaction result](#get-transactions).

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/send_transactions/main.go)**

`_10

func demo(tx *flow.Transaction) {

_10

ctx := context.Background()

_10

flowClient := examples.NewFlowClient()

_10

_10

err := flowClient.SendTransaction(ctx, *tx)

_10

if err != nil {

_10

fmt.Println("error sending transaction", err)

_10

}

_10

}`

### Create Accounts[​](#create-accounts "Direct link to Create Accounts")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/templates#CreateAccount)

On Flow, account creation happens inside a transaction. Because the network allows for a many-to-many relationship between public keys and accounts, it's not possible to derive a new account address from a public key offline.

The Flow VM uses a deterministic address generation algorithm to assign account addresses on chain. You can find more details about address generation in the [accounts & keys documentation](/build/basics/accounts).

#### Public Key[​](#public-key "Direct link to Public Key")

Flow uses ECDSA key pairs to control access to user accounts. Each key pair can be used in combination with the SHA2-256 or SHA3-256 hashing algorithms.

⚠️ You'll need to authorize at least one public key to control your new account.

Flow represents ECDSA public keys in raw form without additional metadata. Each key is a single byte slice containing a concatenation of its X and Y components in big-endian byte form.

A Flow account can contain zero (not possible to control) or more public keys, referred to as account keys. Read more about [accounts in the documentation](/build/basics/accounts).

An account key contains the following data:

* Raw public key (described above)
* Signature algorithm
* Hash algorithm
* Weight (integer between 0-1000)

Account creation happens inside a transaction, which means that somebody must pay to submit that transaction to the network. We'll call this person the account creator. Make sure you have read [sending a transaction section](#send-transactions) first.

`_40

var (

_40

creatorAddress flow.Address

_40

creatorAccountKey *flow.AccountKey

_40

creatorSigner crypto.Signer

_40

)

_40

_40

var accessAPIHost string

_40

_40

// Establish a connection with an access node

_40

flowClient := examples.NewFlowClient()

_40

_40

// Use the templates package to create a new account creation transaction

_40

tx := templates.CreateAccount([]*flow.AccountKey{accountKey}, nil, creatorAddress)

_40

_40

// Set the transaction payer and proposal key

_40

tx.SetPayer(creatorAddress)

_40

tx.SetProposalKey(

_40

creatorAddress,

_40

creatorAccountKey.Index,

_40

creatorAccountKey.SequenceNumber,

_40

)

_40

_40

// Get the latest sealed block to use as a reference block

_40

latestBlock, err := flowClient.GetLatestBlockHeader(context.Background(), true)

_40

if err != nil {

_40

panic("failed to fetch latest block")

_40

}

_40

_40

tx.SetReferenceBlockID(latestBlock.ID)

_40

_40

// Sign and submit the transaction

_40

err = tx.SignEnvelope(creatorAddress, creatorAccountKey.Index, creatorSigner)

_40

if err != nil {

_40

panic("failed to sign transaction envelope")

_40

}

_40

_40

err = flowClient.SendTransaction(context.Background(), *tx)

_40

if err != nil {

_40

panic("failed to send transaction to network")

_40

}`

After the account creation transaction has been submitted you can retrieve the new account address by [getting the transaction result](#get-transactions).

The new account address will be emitted in a system-level `flow.AccountCreated` event.

`_17

result, err := flowClient.GetTransactionResult(ctx, tx.ID())

_17

if err != nil {

_17

panic("failed to get transaction result")

_17

}

_17

_17

var newAddress flow.Address

_17

_17

if result.Status != flow.TransactionStatusSealed {

_17

panic("address not known until transaction is sealed")

_17

}

_17

_17

for _, event := range result.Events {

_17

if event.Type == flow.EventAccountCreated {

_17

newAddress = flow.AccountCreatedEvent(event).Address()

_17

break

_17

}

_17

}`

### Generate Keys[​](#generate-keys "Direct link to Generate Keys")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/build/basics/accounts#signature-and-hash-algorithms)

Flow uses [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) signatures to control access to user accounts. Each key pair can be used in combination with the `SHA2-256` or `SHA3-256` hashing algorithms.

Here's how to generate an ECDSA private key for the P-256 (secp256r1) curve.

`_12

import "github.com/onflow/flow-go-sdk/crypto"

_12

_12

// deterministic seed phrase

_12

// note: this is only an example, please use a secure random generator for the key seed

_12

seed := []byte("elephant ears space cowboy octopus rodeo potato cannon pineapple")

_12

_12

privateKey, err := crypto.GeneratePrivateKey(crypto.ECDSA_P256, seed)

_12

_12

// the private key can then be encoded as bytes (i.e. for storage)

_12

encPrivateKey := privateKey.Encode()

_12

// the private key has an accompanying public key

_12

publicKey := privateKey.PublicKey()`

The example above uses an ECDSA key pair on the P-256 (secp256r1) elliptic curve. Flow also supports the secp256k1 curve used by Bitcoin and Ethereum. Read more about [supported algorithms here](/build/basics/accounts#signature-and-hash-algorithms).

### Transfering Flow[​](#transfering-flow "Direct link to Transfering Flow")

This is an example of how to construct a FLOW token transfer transaction
with the Flow Go SDK.

## Cadence Script[​](#cadence-script "Direct link to Cadence Script")

The following Cadence script will transfer FLOW tokens from a sender
to a recipient.

*Note: this transaction is only compatible with Flow Mainnet.*

`_36

// This transaction is a template for a transaction that

_36

// could be used by anyone to send tokens to another account

_36

// that has been set up to receive tokens.

_36

//

_36

// The withdraw amount and the account from getAccount

_36

// would be the parameters to the transaction

_36

_36

import "FungibleToken"

_36

import "FlowToken"

_36

_36

transaction(amount: UFix64, to: Address) {

_36

_36

// The Vault resource that holds the tokens that are being transferred

_36

let sentVault: @{FungibleToken.Vault}

_36

_36

prepare(signer: auth(BorrowValue) &Account) {

_36

_36

// Get a reference to the signer's stored vault

_36

let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)

_36

?? panic("Could not borrow reference to the owner's Vault!")

_36

_36

// Withdraw tokens from the signer's stored vault

_36

self.sentVault <- vaultRef.withdraw(amount: amount)

_36

}

_36

_36

execute {

_36

_36

// Get a reference to the recipient's Receiver

_36

let receiverRef = getAccount(to)

_36

.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)

_36

?? panic("Could not borrow receiver reference to the recipient's Vault")

_36

_36

// Deposit the withdrawn tokens in the recipient's receiver

_36

receiverRef.deposit(from: <-self.sentVault)

_36

}

_36

}`

## Build the Transaction[​](#build-the-transaction "Direct link to Build the Transaction")

`_39

import (

_39

"github.com/onflow/cadence"

_39

"github.com/onflow/flow-go-sdk"

_39

)

_39

_39

// Replace with script above

_39

const transferScript string = TOKEN_TRANSFER_CADENCE_SCRIPT

_39

_39

var (

_39

senderAddress flow.Address

_39

senderAccountKey flow.AccountKey

_39

senderPrivateKey crypto.PrivateKey

_39

)

_39

_39

func main() {

_39

tx := flow.NewTransaction().

_39

SetScript([]byte(transferScript)).

_39

SetComputeLimit(100).

_39

SetPayer(senderAddress).

_39

SetAuthorizer(senderAddress).

_39

SetProposalKey(senderAddress, senderAccountKey.Index, senderAccountKey.SequenceNumber)

_39

_39

amount, err := cadence.NewUFix64("123.4")

_39

if err != nil {

_39

panic(err)

_39

}

_39

_39

recipient := cadence.NewAddress(flow.HexToAddress("0xabc..."))

_39

_39

err = tx.AddArgument(amount)

_39

if err != nil {

_39

panic(err)

_39

}

_39

_39

err = tx.AddArgument(recipient)

_39

if err != nil {

_39

panic(err)

_39

}

_39

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/flow-go-sdk/index.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)[Next

Migration Guide v0.25.0](/tools/clients/flow-go-sdk/migration-v0.25.0)

###### Rate this page

😞😐😊

* [Overview](#overview)
* [Getting Started](#getting-started)
  + [Installing](#installing)
  + [Importing the Library](#importing-the-library)
* [Connect](#connect)
* [Querying the Flow Network](#querying-the-flow-network)
  + [Get Blocks](#get-blocks)
  + [Get Account](#get-account)
  + [Get Transactions](#get-transactions)
  + [Get Events](#get-events)
  + [Get Collections](#get-collections)
  + [Execute Scripts](#execute-scripts)
* [Mutate Flow Network](#mutate-flow-network)
* [Transactions](#transactions)
  + [Build Transactions](#build-transactions)
  + [Sign Transactions](#sign-transactions)
  + [Single party, single signature](#single-party-single-signature)
  + [Single party, multiple signatures](#single-party-multiple-signatures)
  + [Multiple parties](#multiple-parties)
  + [Multiple parties, two authorizers](#multiple-parties-two-authorizers)
  + [Multiple parties, multiple signatures](#multiple-parties-multiple-signatures)
  + [Send Transactions](#send-transactions)
  + [Create Accounts](#create-accounts)
  + [Generate Keys](#generate-keys)
  + [Transfering Flow](#transfering-flow)
* [Cadence Script](#cadence-script)
* [Build the Transaction](#build-the-transaction)

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
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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