# Source: https://developers.flow.com/tools/clients/flow-go-sdk




Flow Go SDK | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
  + [Flow Client Library (FCL)](/tools/clients/fcl-js)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
    - [Migration Guide v0.25.0](/tools/clients/flow-go-sdk/migration-v0.25.0)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* [Clients](/tools/clients)
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

 `_10go get github.com/onflow/flow-go-sdk`

It's usually good practice to pin your dependencies to a specific version.
Refer to the [SDK releases](https://github.com/onflow/flow-go-sdk/tags) page to identify the latest version.

### Importing the Library[​](#importing-the-library "Direct link to Importing the Library")

After the library has been installed you can import it.

 `_10import "github.com/onflow/flow-go-sdk"`
## Connect[​](#connect "Direct link to Connect")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#New)

The Go SDK library uses HTTP or gRPC APIs to communicate with the access nodes and it must be configured with correct access node API URL.
The library provides default factories for connecting to Flow AN APIs and you can easily switch between HTTP or gRPC if you use the provided client interface.

You can check more examples for creating clients in the examples:
**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/http_grpc_clients/main.go)**

Basic Example:

 `_10// common client interface_10var flowClient client.Client_10_10// initialize an http emulator client_10flowClient, err := http.NewClient(http.EmulatorHost)_10_10// initialize a gPRC emulator client_10flowClient, err = grpc.NewClient(grpc.EmulatorHost)`

You can also initialize an HTTP client or gRPC client directly which will offer you access to network specific options,
but be aware you won't be able to easily switch between those since they don't implement a common interface. This is only
advisable if the implementation needs the access to those advanced options.
Advanced Example:

 `_10// initialize http specific client_10httpClient, err := http.NewHTTPClient(http.EMULATOR_URL)_10_10// initialize grpc specific client_10grpcClient, err := grpc.NewGRPCClient(_10 grpc.EMULATOR_URL,_10 grpcOpts.WithTransportCredentials(insecure.NewCredentials()),_10)`
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

 `_26func demo() {_26 ctx := context.Background()_26 flowClient := examples.NewFlowClient()_26_26 // get the latest sealed block_26 isSealed := true_26 latestBlock, err := flowClient.GetLatestBlock(ctx, isSealed)_26 printBlock(latestBlock, err)_26_26 // get the block by ID_26 blockID := latestBlock.ID.String()_26 blockByID, err := flowClient.GetBlockByID(ctx, flow.HexToID(blockID))_26 printBlock(blockByID, err)_26_26 // get block by height_26 blockByHeight, err := flowClient.GetBlockByHeight(ctx, 0)_26 printBlock(blockByHeight, err)_26}_26_26func printBlock(block *flow.Block, err error) {_26 examples.Handle(err)_26_26 fmt.Printf("\nID: %s\n", block.ID)_26 fmt.Printf("height: %d\n", block.Height)_26 fmt.Printf("timestamp: %s\n\n", block.Timestamp)_26}`

Result output:

 `_13ID: 835dc83939141097aa4297aa6cf69fc600863e3b5f9241a0d7feac1868adfa4f_13height: 10_13timestamp: 2021-10-06 15:06:07.105382 +0000 UTC_13_13_13ID: 835dc83939141097aa4297aa6cf69fc600863e3b5f9241a0d7feac1868adfa4f_13height: 10_13timestamp: 2021-10-06 15:06:07.105382 +0000 UTC_13_13_13ID: 7bc42fe85d32ca513769a74f97f7e1a7bad6c9407f0d934c2aa645ef9cf613c7_13height: 0_13timestamp: 2018-12-19 22:32:30.000000042 +0000 UTC`
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

 `_22func demo() {_22 ctx := context.Background()_22 flowClient := examples.NewFlowClient()_22_22 // get account from the latest block_22 address := flow.HexToAddress("f8d6e0586b0a20c7")_22 account, err := flowClient.GetAccount(ctx, address)_22 printAccount(account, err)_22_22 // get account from the block by height 0_22 account, err = flowClient.GetAccountAtBlockHeight(ctx, address, 0)_22 printAccount(account, err)_22}_22_22func printAccount(account *flow.Account, err error) {_22 examples.Handle(err)_22_22 fmt.Printf("\nAddress: %s", account.Address.String())_22 fmt.Printf("\nBalance: %d", account.Balance)_22 fmt.Printf("\nContracts: %d", len(account.Contracts))_22 fmt.Printf("\nKeys: %d\n", len(account.Keys))_22}`

Result output:

 `_10Address: f8d6e0586b0a20c7_10Balance: 999999999999600000_10Contracts: 2_10Keys: 1_10_10Address: f8d6e0586b0a20c7_10Balance: 999999999999600000_10Contracts: 2_10Keys: 1`
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

 `_26func demo(txID flow.Identifier) {_26 ctx := context.Background()_26 flowClient := examples.NewFlowClient()_26_26 tx, err := flowClient.GetTransaction(ctx, txID)_26 printTransaction(tx, err)_26_26 txr, err := flowClient.GetTransactionResult(ctx, txID)_26 printTransactionResult(txr, err)_26}_26_26func printTransaction(tx *flow.Transaction, err error) {_26 examples.Handle(err)_26_26 fmt.Printf("\nID: %s", tx.ID().String())_26 fmt.Printf("\nPayer: %s", tx.Payer.String())_26 fmt.Printf("\nProposer: %s", tx.ProposalKey.Address.String())_26 fmt.Printf("\nAuthorizers: %s", tx.Authorizers)_26}_26_26func printTransactionResult(txr *flow.TransactionResult, err error) {_26 examples.Handle(err)_26_26 fmt.Printf("\nStatus: %s", txr.Status.String())_26 fmt.Printf("\nError: %v", txr.Error)_26}`

Example output:

 `_10ID: fb1272c57cdad79acf2fcf37576d82bf760e3008de66aa32a900c8cd16174e1c_10Payer: f8d6e0586b0a20c7_10Proposer: f8d6e0586b0a20c7_10Authorizers: []_10Status: SEALED_10Error: <nil>`
### Get Events[​](#get-events "Direct link to Get Events")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetEventsForBlockIDs)

Retrieve events by a given type in a specified block height range or through a list of block IDs.

📖 **Event type** is a string that follow a standard format:

 `_10A.{contract address}.{contract name}.{event name}`

Please read more about [events in the documentation](/build/core-contracts/flow-token). The exception to this standard are
core events, and you should read more about them in [this document](https://cadence-lang.org/docs/language/core-events).

📖 **Block height range** expresses the height of the start and end block in the chain.

#### Examples[​](#examples-2 "Direct link to Examples")

Example depicts ways to get events within block range or by block IDs:

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/get_events/main.go)**

 `_34func demo(deployedContract *flow.Account, runScriptTx *flow.Transaction) {_34 ctx := context.Background()_34 flowClient := examples.NewFlowClient()_34_34 // Query for account creation events by type_34 result, err := flowClient.GetEventsForHeightRange(ctx, "flow.AccountCreated", 0, 30)_34 printEvents(result, err)_34_34 // Query for our custom event by type_34 customType := fmt.Sprintf("AC.%s.EventDemo.EventDemo.Add", deployedContract.Address.Hex())_34 result, err = flowClient.GetEventsForHeightRange(ctx, customType, 0, 10)_34 printEvents(result, err)_34_34 // Get events directly from transaction result_34 txResult, err := flowClient.GetTransactionResult(ctx, runScriptTx.ID())_34 examples.Handle(err)_34 printEvent(txResult.Events)_34}_34_34func printEvents(result []client.BlockEvents, err error) {_34 examples.Handle(err)_34_34 for _, block := range result {_34 printEvent(block.Events)_34 }_34}_34_34func printEvent(events []flow.Event) {_34 for _, event := range events {_34 fmt.Printf("\n\nType: %s", event.Type)_34 fmt.Printf("\nValues: %v", event.Value)_34 fmt.Printf("\nTransaction ID: %s", event.TransactionID)_34 }_34}`

Example output:

 `_13Type: flow.AccountCreated_13Values: flow.AccountCreated(address: 0xfd43f9148d4b725d)_13Transaction ID: ba9d53c8dcb0f9c2f854f93da8467a22d053eab0c540bde0b9ca2f7ad95eb78e_13_13Type: flow.AccountCreated_13Values: flow.AccountCreated(address: 0xeb179c27144f783c)_13Transaction ID: 8ab7bfef3de1cf8b2ffb36559446100bf4129a9aa88d6bc59f72a467acf0c801_13_13..._13_13Type: A.eb179c27144f783c.EventDemo.Add_13Values: A.eb179c27144f783c.EventDemo.Add(x: 2, y: 3, sum: 5)_13Transaction ID: f3a2e33687ad23b0e02644ebbdcd74a7cd8ea7214065410a8007811d0bcbd353`
### Get Collections[​](#get-collections "Direct link to Get Collections")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.GetCollection)

Retrieve a batch of transactions that have been included in the same block, known as ***collections***.
Collections are used to improve consensus throughput by increasing the number of transactions per block and they act as a link between a block and a transaction.

📖 **Collection ID** is SHA3-256 hash of the collection payload.

Example retrieving a collection:

 `_15func demo(exampleCollectionID flow.Identifier) {_15 ctx := context.Background()_15 flowClient := examples.NewFlowClient()_15_15 // get collection by ID_15 collection, err := flowClient.GetCollection(ctx, exampleCollectionID)_15 printCollection(collection, err)_15}_15_15func printCollection(collection *flow.Collection, err error) {_15 examples.Handle(err)_15_15 fmt.Printf("\nID: %s", collection.ID().String())_15 fmt.Printf("\nTransactions: %s", collection.TransactionIDs)_15}`

Example output:

 `_10ID: 3d7b8037381f2497d83f2f9e09422c036aae2a59d01a7693fb6003b4d0bc3595_10Transactions: [cf1184e3de4bd9a7232ca3d0b9dd2cfbf96c97888298b81a05c086451fa52ec1]`
### Execute Scripts[​](#execute-scripts "Direct link to Execute Scripts")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.ExecuteScriptAtLatestBlock)

Scripts allow you to write arbitrary non-mutating Cadence code on the Flow blockchain and return data. You can learn more about [Cadence and scripts here](https://cadence-lang.org/docs/language), but we are now only interested in executing the script code and getting back the data.

We can execute a script using the latest state of the Flow blockchain or we can choose to execute the script at a specific time in history defined by a block height or block ID.

📖 **Block ID** is SHA3-256 hash of the entire block payload, but you can get that value from the block response properties.

📖 **Block height** expresses the height of the block in the chain.

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/execute_script/main.go)**

 `_62func demo() {_62 ctx := context.Background()_62 flowClient := examples.NewFlowClient()_62_62 script := []byte(`_62 access(all) fun main(a: Int): Int {_62 return a + 10_62 }_62 `)_62 args := []cadence.Value{ cadence.NewInt(5) }_62 value, err := flowClient.ExecuteScriptAtLatestBlock(ctx, script, args)_62_62 examples.Handle(err)_62 fmt.Printf("\nValue: %s", value.String())_62_62 complexScript := []byte(`_62 access(all) struct User {_62 access(all) var balance: UFix64_62 access(all) var address: Address_62 access(all) var name: String_62_62 init(name: String, address: Address, balance: UFix64) {_62 self.name = name_62 self.address = address_62 self.balance = balance_62 }_62 }_62_62 access(all) fun main(name: String): User {_62 return User(_62 name: name,_62 address: 0x1,_62 balance: 10.0_62 )_62 }_62 `)_62 args = []cadence.Value{ cadence.NewString("Dete") }_62 value, err = flowClient.ExecuteScriptAtLatestBlock(ctx, complexScript, args)_62 printComplexScript(value, err)_62}_62_62type User struct {_62 balance uint64_62 address flow.Address_62 name string_62}_62_62func printComplexScript(value cadence.Value, err error) {_62 examples.Handle(err)_62 fmt.Printf("\nString value: %s", value.String())_62_62 s := value.(cadence.Struct)_62 u := User{_62 balance: s.Fields[0].ToGoValue().(uint64),_62 address: s.Fields[1].ToGoValue().([flow.AddressLength]byte),_62 name: s.Fields[2].ToGoValue().(string),_62 }_62_62 fmt.Printf("\nName: %s", u.name)_62 fmt.Printf("\nAddress: %s", u.address.String())_62 fmt.Printf("\nBalance: %d", u.balance)_62}`

Example output:

 `_10Value: 15_10String value: s.34a17571e1505cf6770e6ef16ca387e345e9d54d71909f23a7ec0d671cd2faf5.User(balance: 10.00000000, address: 0x1, name: "Dete")_10Name: Dete_10Address: 0000000000000001_10Balance: 1000000000`
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

 `_10transaction(greeting: String) {_10 execute {_10 log(greeting.concat(", World!"))_10 }_10}`

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

 `_10transaction {_10 prepare(authorizer1: &Account, authorizer2: &Account) { }_10}`
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

 `_12transaction(greeting: String) {_12_12 let guest: Address_12_12 prepare(authorizer: &Account) {_12 self.guest = authorizer.address_12 }_12_12 execute {_12 log(greeting.concat(",").concat(self.guest.toString()))_12 }_12}`

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/transaction_signing/single_party/main.go)**

 `_57import (_57 "context"_57 "os"_57 "github.com/onflow/flow-go-sdk"_57 "github.com/onflow/flow-go-sdk/client"_57)_57_57func main() {_57_57 greeting, err := os.ReadFile("Greeting2.cdc")_57 if err != nil {_57 panic("failed to load Cadence script")_57 }_57_57 proposerAddress := flow.HexToAddress("9a0766d93b6608b7")_57 proposerKeyIndex := 3_57_57 payerAddress := flow.HexToAddress("631e88ae7f1d7c20")_57 authorizerAddress := flow.HexToAddress("7aad92e5a0715d21")_57_57 var accessAPIHost string_57_57 // Establish a connection with an access node_57 flowClient := examples.NewFlowClient()_57_57 // Get the latest sealed block to use as a reference block_57 latestBlock, err := flowClient.GetLatestBlockHeader(context.Background(), true)_57 if err != nil {_57 panic("failed to fetch latest block")_57 }_57_57 // Get the latest account info for this address_57 proposerAccount, err := flowClient.GetAccountAtLatestBlock(context.Background(), proposerAddress)_57 if err != nil {_57 panic("failed to fetch proposer account")_57 }_57_57 // Get the latest sequence number for this key_57 sequenceNumber := proposerAccount.Keys[proposerKeyIndex].SequenceNumber_57_57 tx := flow.NewTransaction()._57 SetScript(greeting)._57 SetComputeLimit(100)._57 SetReferenceBlockID(latestBlock.ID)._57 SetProposalKey(proposerAddress, proposerKeyIndex, sequenceNumber)._57 SetPayer(payerAddress)._57 AddAuthorizer(authorizerAddress)_57_57 // Add arguments last_57_57 hello := cadence.NewString("Hello")_57_57 err = tx.AddArgument(hello)_57 if err != nil {_57 panic("invalid argument")_57 }_57}`

After you have successfully [built a transaction](#build-the-transaction) the next step in the process is to sign it.

### Sign Transactions[​](#sign-transactions "Direct link to Sign Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk#Transaction.SignEnvelope)

Flow introduces new concepts that allow for more flexibility when creating and signing transactions.
Before trying the examples below, we recommend that you read through the [transaction signature documentation](../../../build/basics/transactions.md.

After you have successfully [built a transaction](#build-the-transaction) the next step in the process is to sign it. Flow transactions have envelope and payload signatures, and you should learn about each in the [signature documentation](/build/basics/transactions).

Quick example of building a transaction:

 `_16import (_16 "github.com/onflow/flow-go-sdk"_16 "github.com/onflow/flow-go-sdk/crypto"_16)_16_16var (_16 myAddress flow.Address_16 myAccountKey flow.AccountKey_16 myPrivateKey crypto.PrivateKey_16)_16_16tx := flow.NewTransaction()._16 SetScript([]byte("transaction { execute { log(\"Hello, World!\") } }"))._16 SetComputeLimit(100)._16 SetProposalKey(myAddress, myAccountKey.Index, myAccountKey.SequenceNumber)._16 SetPayer(myAddress)`

Transaction signing is done through the `crypto.Signer` interface. The simplest (and least secure) implementation of `crypto.Signer` is `crypto.InMemorySigner`.

Signatures can be generated more securely using keys stored in a hardware device such as an [HSM](https://en.wikipedia.org/wiki/Hardware_security_module). The `crypto.Signer` interface is intended to be flexible enough to support a variety of signer implementations and is not limited to in-memory implementations.

Simple signature example:

 `_10// construct a signer from your private key and configured hash algorithm_10mySigner, err := crypto.NewInMemorySigner(myPrivateKey, myAccountKey.HashAlgo)_10if err != nil {_10 panic("failed to create a signer")_10}_10_10err = tx.SignEnvelope(myAddress, myAccountKey.Index, mySigner)_10if err != nil {_10 panic("failed to sign transaction")_10}`

Flow supports great flexibility when it comes to transaction signing, we can define multiple authorizers (multi-sig transactions) and have different payer account than proposer. We will explore advanced signing scenarios bellow.

### [Single party, single signature](/build/basics/transactions#single-party-single-signature)[​](#single-party-single-signature "Direct link to single-party-single-signature")

* Proposer, payer and authorizer are the same account (`0x01`).
* Only the envelope must be signed.
* Proposal key must have full signing weight.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 1000 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#single-party-single-signature)**

 `_22account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))_22_22key1 := account1.Keys[0]_22_22// create signer from securely-stored private key_22key1Signer := getSignerForKey1()_22_22referenceBlock, _ := flow.GetLatestBlock(ctx, true)_22tx := flow.NewTransaction()._22 SetScript([]byte(`_22 transaction {_22 prepare(signer: &Account) { log(signer.address) }_22 }_22 `))._22 SetComputeLimit(100)._22 SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber)._22 SetReferenceBlockID(referenceBlock.ID)._22 SetPayer(account1.Address)._22 AddAuthorizer(account1.Address)_22_22// account 1 signs the envelope with key 1_22err := tx.SignEnvelope(account1.Address, key1.Index, key1Signer)`
### [Single party, multiple signatures](/build/basics/transactions#single-party-multiple-signatures)[​](#single-party-multiple-signatures "Direct link to single-party-multiple-signatures")

* Proposer, payer and authorizer are the same account (`0x01`).
* Only the envelope must be signed.
* Each key has weight 500, so two signatures are required.

| Account | Key ID | Weight |
| --- | --- | --- |
| `0x01` | 1 | 500 |
| `0x01` | 2 | 500 |

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/tree/master/examples#single-party-multiple-signatures)**

 `_27account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))_27_27key1 := account1.Keys[0]_27key2 := account1.Keys[1]_27_27// create signers from securely-stored private keys_27key1Signer := getSignerForKey1()_27key2Signer := getSignerForKey2()_27_27referenceBlock, _ := flow.GetLatestBlock(ctx, true)_27tx := flow.NewTransaction()._27 SetScript([]byte(`_27 transaction {_27 prepare(signer: &Account) { log(signer.address) }_27 }_27 `))._27 SetComputeLimit(100)._27 SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber)._27 SetReferenceBlockID(referenceBlock.ID)._27 SetPayer(account1.Address)._27 AddAuthorizer(account1.Address)_27_27// account 1 signs the envelope with key 1_27err := tx.SignEnvelope(account1.Address, key1.Index, key1Signer)_27_27// account 1 signs the envelope with key 2_27err = tx.SignEnvelope(account1.Address, key2.Index, key2Signer)`
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

 `_29account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))_29account2, _ := c.GetAccount(ctx, flow.HexToAddress("02"))_29_29key1 := account1.Keys[0]_29key3 := account2.Keys[0]_29_29// create signers from securely-stored private keys_29key1Signer := getSignerForKey1()_29key3Signer := getSignerForKey3()_29_29referenceBlock, _ := flow.GetLatestBlock(ctx, true)_29tx := flow.NewTransaction()._29 SetScript([]byte(`_29 transaction {_29 prepare(signer: &Account) { log(signer.address) }_29 }_29 `))._29 SetComputeLimit(100)._29 SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber)._29 SetReferenceBlockID(referenceBlock.ID)._29 SetPayer(account2.Address)._29 AddAuthorizer(account1.Address)_29_29// account 1 signs the payload with key 1_29err := tx.SignPayload(account1.Address, key1.Index, key1Signer)_29_29// account 2 signs the envelope with key 3_29// note: payer always signs last_29err = tx.SignEnvelope(account2.Address, key3.Index, key3Signer)`
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

 `_33account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))_33account2, _ := c.GetAccount(ctx, flow.HexToAddress("02"))_33_33key1 := account1.Keys[0]_33key3 := account2.Keys[0]_33_33// create signers from securely-stored private keys_33key1Signer := getSignerForKey1()_33key3Signer := getSignerForKey3()_33_33referenceBlock, _ := flow.GetLatestBlock(ctx, true)_33tx := flow.NewTransaction()._33 SetScript([]byte(`_33 transaction {_33 prepare(signer1: &Account, signer2: &Account) {_33 log(signer.address)_33 log(signer2.address)_33 }_33 }_33 `))._33 SetComputeLimit(100)._33 SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber)._33 SetReferenceBlockID(referenceBlock.ID)._33 SetPayer(account2.Address)._33 AddAuthorizer(account1.Address)._33 AddAuthorizer(account2.Address)_33_33// account 1 signs the payload with key 1_33err := tx.SignPayload(account1.Address, key1.Index, key1Signer)_33_33// account 2 signs the envelope with key 3_33// note: payer always signs last_33err = tx.SignEnvelope(account2.Address, key3.Index, key3Signer)`
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

 `_40account1, _ := c.GetAccount(ctx, flow.HexToAddress("01"))_40account2, _ := c.GetAccount(ctx, flow.HexToAddress("02"))_40_40key1 := account1.Keys[0]_40key2 := account1.Keys[1]_40key3 := account2.Keys[0]_40key4 := account2.Keys[1]_40_40// create signers from securely-stored private keys_40key1Signer := getSignerForKey1()_40key2Signer := getSignerForKey1()_40key3Signer := getSignerForKey3()_40key4Signer := getSignerForKey4()_40_40referenceBlock, _ := flow.GetLatestBlock(ctx, true)_40tx := flow.NewTransaction()._40 SetScript([]byte(`_40 transaction {_40 prepare(signer: &Account) { log(signer.address) }_40 }_40 `))._40 SetComputeLimit(100)._40 SetProposalKey(account1.Address, key1.Index, key1.SequenceNumber)._40 SetReferenceBlockID(referenceBlock.ID)._40 SetPayer(account2.Address)._40 AddAuthorizer(account1.Address)_40_40// account 1 signs the payload with key 1_40err := tx.SignPayload(account1.Address, key1.Index, key1Signer)_40_40// account 1 signs the payload with key 2_40err = tx.SignPayload(account1.Address, key2.Index, key2Signer)_40_40// account 2 signs the envelope with key 3_40// note: payer always signs last_40err = tx.SignEnvelope(account2.Address, key3.Index, key3Signer)_40_40// account 2 signs the envelope with key 4_40// note: payer always signs last_40err = tx.SignEnvelope(account2.Address, key4.Index, key4Signer)`
### Send Transactions[​](#send-transactions "Direct link to Send Transactions")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](https://pkg.go.dev/github.com/onflow/flow-go-sdk/client#Client.SendTransaction)

After a transaction has been [built](#build-the-transaction) and [signed](#sign-transactions), it can be sent to the Flow blockchain where it will be executed. If sending was successful you can then [retrieve the transaction result](#get-transactions).

**[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/try.svg)](https://github.com/onflow/flow-go-sdk/blob/master/examples/send_transactions/main.go)**

 `_10func demo(tx *flow.Transaction) {_10 ctx := context.Background()_10 flowClient := examples.NewFlowClient()_10_10 err := flowClient.SendTransaction(ctx, *tx)_10 if err != nil {_10 fmt.Println("error sending transaction", err)_10 }_10}`
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

 `_40var (_40 creatorAddress flow.Address_40 creatorAccountKey *flow.AccountKey_40 creatorSigner crypto.Signer_40)_40_40var accessAPIHost string_40_40// Establish a connection with an access node_40flowClient := examples.NewFlowClient()_40_40// Use the templates package to create a new account creation transaction_40tx := templates.CreateAccount([]*flow.AccountKey{accountKey}, nil, creatorAddress)_40_40// Set the transaction payer and proposal key_40tx.SetPayer(creatorAddress)_40tx.SetProposalKey(_40 creatorAddress,_40 creatorAccountKey.Index,_40 creatorAccountKey.SequenceNumber,_40)_40_40// Get the latest sealed block to use as a reference block_40latestBlock, err := flowClient.GetLatestBlockHeader(context.Background(), true)_40if err != nil {_40 panic("failed to fetch latest block")_40}_40_40tx.SetReferenceBlockID(latestBlock.ID)_40_40// Sign and submit the transaction_40err = tx.SignEnvelope(creatorAddress, creatorAccountKey.Index, creatorSigner)_40if err != nil {_40 panic("failed to sign transaction envelope")_40}_40_40err = flowClient.SendTransaction(context.Background(), *tx)_40if err != nil {_40 panic("failed to send transaction to network")_40}`

After the account creation transaction has been submitted you can retrieve the new account address by [getting the transaction result](#get-transactions).

The new account address will be emitted in a system-level `flow.AccountCreated` event.

 `_17result, err := flowClient.GetTransactionResult(ctx, tx.ID())_17if err != nil {_17 panic("failed to get transaction result")_17}_17_17var newAddress flow.Address_17_17if result.Status != flow.TransactionStatusSealed {_17 panic("address not known until transaction is sealed")_17}_17_17for _, event := range result.Events {_17 if event.Type == flow.EventAccountCreated {_17 newAddress = flow.AccountCreatedEvent(event).Address()_17 break_17 }_17}`
### Generate Keys[​](#generate-keys "Direct link to Generate Keys")

[![](https://raw.githubusercontent.com/onflow/sdks/main/templates/documentation/ref.svg)](/build/basics/accounts#signature-and-hash-algorithms)

Flow uses [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) signatures to control access to user accounts. Each key pair can be used in combination with the `SHA2-256` or `SHA3-256` hashing algorithms.

Here's how to generate an ECDSA private key for the P-256 (secp256r1) curve.

 `_12import "github.com/onflow/flow-go-sdk/crypto"_12_12// deterministic seed phrase_12// note: this is only an example, please use a secure random generator for the key seed_12seed := []byte("elephant ears space cowboy octopus rodeo potato cannon pineapple")_12_12privateKey, err := crypto.GeneratePrivateKey(crypto.ECDSA_P256, seed)_12_12// the private key can then be encoded as bytes (i.e. for storage)_12encPrivateKey := privateKey.Encode()_12// the private key has an accompanying public key_12publicKey := privateKey.PublicKey()`

The example above uses an ECDSA key pair on the P-256 (secp256r1) elliptic curve. Flow also supports the secp256k1 curve used by Bitcoin and Ethereum. Read more about [supported algorithms here](/build/basics/accounts#signature-and-hash-algorithms).

### Transfering Flow[​](#transfering-flow "Direct link to Transfering Flow")

This is an example of how to construct a FLOW token transfer transaction
with the Flow Go SDK.

## Cadence Script[​](#cadence-script "Direct link to Cadence Script")

The following Cadence script will transfer FLOW tokens from a sender
to a recipient.

*Note: this transaction is only compatible with Flow Mainnet.*

 `_36// This transaction is a template for a transaction that_36// could be used by anyone to send tokens to another account_36// that has been set up to receive tokens._36//_36// The withdraw amount and the account from getAccount_36// would be the parameters to the transaction_36_36import "FungibleToken"_36import "FlowToken"_36_36transaction(amount: UFix64, to: Address) {_36_36 // The Vault resource that holds the tokens that are being transferred_36 let sentVault: @{FungibleToken.Vault}_36_36 prepare(signer: auth(BorrowValue) &Account) {_36_36 // Get a reference to the signer's stored vault_36 let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)_36 ?? panic("Could not borrow reference to the owner's Vault!")_36_36 // Withdraw tokens from the signer's stored vault_36 self.sentVault <- vaultRef.withdraw(amount: amount)_36 }_36_36 execute {_36_36 // Get a reference to the recipient's Receiver_36 let receiverRef = getAccount(to)_36 .capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)_36 ?? panic("Could not borrow receiver reference to the recipient's Vault")_36_36 // Deposit the withdrawn tokens in the recipient's receiver_36 receiverRef.deposit(from: <-self.sentVault)_36 }_36}`
## Build the Transaction[​](#build-the-transaction "Direct link to Build the Transaction")

 `_39import (_39 "github.com/onflow/cadence"_39 "github.com/onflow/flow-go-sdk"_39)_39_39// Replace with script above_39const transferScript string = TOKEN_TRANSFER_CADENCE_SCRIPT_39_39var (_39 senderAddress flow.Address_39 senderAccountKey flow.AccountKey_39 senderPrivateKey crypto.PrivateKey_39)_39_39func main() {_39 tx := flow.NewTransaction()._39 SetScript([]byte(transferScript))._39 SetComputeLimit(100)._39 SetPayer(senderAddress)._39 SetAuthorizer(senderAddress)._39 SetProposalKey(senderAddress, senderAccountKey.Index, senderAccountKey.SequenceNumber)_39_39 amount, err := cadence.NewUFix64("123.4")_39 if err != nil {_39 panic(err)_39 }_39_39 recipient := cadence.NewAddress(flow.HexToAddress("0xabc..."))_39_39 err = tx.AddArgument(amount)_39 if err != nil {_39 panic(err)_39 }_39_39 err = tx.AddArgument(recipient)_39 if err != nil {_39 panic(err)_39 }_39}`[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/flow-go-sdk/index.md)Last updated on **Jan 22, 2025** by **Chase Fleming**[PreviousWalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)[NextMigration Guide v0.25.0](/tools/clients/flow-go-sdk/migration-v0.25.0)
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

