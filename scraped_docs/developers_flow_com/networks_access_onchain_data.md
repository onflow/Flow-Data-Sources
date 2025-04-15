# Source: https://developers.flow.com/networks/access-onchain-data

Flow Access API Specification | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)

  + [Access HTTP API ↗️](/networks/access-onchain-data/access-http-api)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* Accessing Data

On this page

# Flow Access API Specification

The Access API is implemented as a [gRPC service](https://grpc.io/).

A language-agnostic specification for this API is defined using [Protocol Buffers](https://developers.google.com/protocol-buffers), which can be used to generate client libraries in a variety of programming languages.

* [Flow Access API protobuf source files](https://github.com/onflow/flow/tree/master/protobuf)

## Flow Access Node Endpoints[​](#flow-access-node-endpoints "Direct link to Flow Access Node Endpoints")

| Network | GRPC | Web GRPC | REST |
| --- | --- | --- | --- |
| Mainnet | `access.mainnet.nodes.onflow.org:9000` | `mainnet.onflow.org` | `rest-mainnet.onflow.org` |
| Testnet | `access.devnet.nodes.onflow.org:9000` | `testnet.onflow.org` | `rest-testnet.onflow.org` |

---

## Ping[​](#ping "Direct link to Ping")

`Ping` will return a successful response if the Access API is ready and available.

`_10

rpc Ping(PingRequest) returns (PingResponse)`

If a ping request returns an error or times out, it can be assumed that the Access API is unavailable.

#### Request[​](#request "Direct link to Request")

`_10

message PingRequest {}`

#### Response[​](#response "Direct link to Response")

`_10

message PingResponse {}`

---

## Block Headers[​](#block-headers "Direct link to Block Headers")

The following methods query information about [block headers](#block-header).

### GetLatestBlockHeader[​](#getlatestblockheader "Direct link to GetLatestBlockHeader")

`GetLatestBlockHeader` gets the latest sealed or unsealed [block header](#block-header).

`_10

rpc GetLatestBlockHeader (GetLatestBlockHeaderRequest) returns (BlockHeaderResponse)`

#### Request[​](#request-1 "Direct link to Request")

`_10

message GetLatestBlockHeaderRequest {

_10

bool is_sealed = 1;

_10

}`

#### Response[​](#response-1 "Direct link to Response")

`_10

message BlockHeaderResponse {

_10

entities.BlockHeader block = 1;

_10

entities.BlockStatus block_status = 2;

_10

entities.Metadata metadata = 3;

_10

}`

### GetBlockHeaderByID[​](#getblockheaderbyid "Direct link to GetBlockHeaderByID")

`GetBlockHeaderByID` gets a [block header](#block-header) by ID.

`_10

rpc GetBlockHeaderByID (GetBlockHeaderByIDRequest) returns (BlockHeaderResponse)`

#### Request[​](#request-2 "Direct link to Request")

`_10

message GetBlockHeaderByIDRequest {

_10

bytes id = 1;

_10

}`

#### Response[​](#response-2 "Direct link to Response")

`_10

message BlockHeaderResponse {

_10

entities.BlockHeader block = 1;

_10

entities.BlockStatus block_status = 2;

_10

entities.Metadata metadata = 3;

_10

}`

### GetBlockHeaderByHeight[​](#getblockheaderbyheight "Direct link to GetBlockHeaderByHeight")

`GetBlockHeaderByHeight` gets a [block header](#block-header) by height.

`_10

rpc GetBlockHeaderByHeight (GetBlockHeaderByHeightRequest) returns (BlockHeaderResponse)`

#### Request[​](#request-3 "Direct link to Request")

`_10

message GetBlockHeaderByHeightRequest {

_10

uint64 height = 1;

_10

}`

#### Response[​](#response-3 "Direct link to Response")

`_10

message BlockHeaderResponse {

_10

entities.BlockHeader block = 1;

_10

entities.BlockStatus block_status = 2;

_10

entities.Metadata metadata = 3;

_10

}`

---

## Blocks[​](#blocks "Direct link to Blocks")

The following methods query information about [full blocks](#block).

### GetLatestBlock[​](#getlatestblock "Direct link to GetLatestBlock")

`GetLatestBlock` gets the full payload of the latest sealed or unsealed [block](#block).

`_10

rpc GetLatestBlock (GetLatestBlockRequest) returns (BlockResponse)`

#### Request[​](#request-4 "Direct link to Request")

`_10

message GetLatestBlockRequest {

_10

bool is_sealed = 1;

_10

bool full_block_response = 2;

_10

}`

#### Response[​](#response-4 "Direct link to Response")

`_10

message BlockResponse {

_10

entities.Block block = 1;

_10

entities.BlockStatus block_status = 2;

_10

entities.Metadata metadata = 3;

_10

}`

### GetBlockByID[​](#getblockbyid "Direct link to GetBlockByID")

`GetBlockByID` gets a [full block](#block) by ID.

`_10

rpc GetBlockByID (GetBlockByIDRequest) returns (BlockResponse)`

#### Request[​](#request-5 "Direct link to Request")

`_10

message GetBlockByIDRequest {

_10

bytes id = 1;

_10

bool full_block_response = 2;

_10

}`

#### Response[​](#response-5 "Direct link to Response")

`_10

message BlockResponse {

_10

entities.Block block = 1;

_10

entities.BlockStatus block_status = 2;

_10

entities.Metadata metadata = 3;

_10

}`

### GetBlockByHeight[​](#getblockbyheight "Direct link to GetBlockByHeight")

`GetBlockByHeight` gets a [full block](#block) by height.

`_10

rpc GetBlockByHeight (GetBlockByHeightRequest) returns (BlockResponse)`

#### Request[​](#request-6 "Direct link to Request")

`_10

message GetBlockByHeightRequest {

_10

uint64 height = 1;

_10

bool full_block_response = 2;

_10

}`

#### Response[​](#response-6 "Direct link to Response")

`_10

message BlockResponse {

_10

entities.Block block = 1;

_10

entities.BlockStatus block_status = 2;

_10

entities.Metadata metadata = 3;

_10

}`

---

## Collections[​](#collections "Direct link to Collections")

The following methods query information about [collections](#collection).

### GetCollectionByID[​](#getcollectionbyid "Direct link to GetCollectionByID")

`GetCollectionByID` gets a [collection](#collection) by ID.

`_10

rpc GetCollectionByID (GetCollectionByIDRequest) returns (CollectionResponse)`

#### Request[​](#request-7 "Direct link to Request")

`_10

message GetCollectionByIDRequest {

_10

bytes id = 1;

_10

}`

#### Response[​](#response-7 "Direct link to Response")

`_10

message CollectionResponse {

_10

entities.Collection collection = 1;

_10

entities.Metadata metadata = 2;

_10

}`

---

### GetFullCollectionByID[​](#getfullcollectionbyid "Direct link to GetFullCollectionByID")

`GetFullCollectionByID` gets a collection by ID, which contains a set of [transactions](#transaction).

`_10

rpc GetFullCollectionByID(GetFullCollectionByIDRequest) returns (FullCollectionResponse);`

#### Request[​](#request-8 "Direct link to Request")

`_10

message GetFullCollectionByIDRequest {

_10

bytes id = 1;

_10

}`

#### Response[​](#response-8 "Direct link to Response")

`_10

message FullCollectionResponse {

_10

repeated entities.Transaction transactions = 1;

_10

entities.Metadata metadata = 2;

_10

}`

---

## Transactions[​](#transactions "Direct link to Transactions")

The following methods can be used to submit [transactions](#transaction) and fetch their results.

### SendTransaction[​](#sendtransaction "Direct link to SendTransaction")

`SendTransaction` submits a transaction to the network.

`_10

rpc SendTransaction (SendTransactionRequest) returns (SendTransactionResponse)`

`SendTransaction` determines the correct cluster of collection nodes that is responsible for collecting the transaction based on the hash of the transaction and forwards the transaction to that cluster.

#### Request[​](#request-9 "Direct link to Request")

`SendTransactionRequest` message contains the transaction that is being request to be executed.

`_10

message SendTransactionRequest {

_10

entities.Transaction transaction = 1;

_10

}`

#### Response[​](#response-9 "Direct link to Response")

`SendTransactionResponse` message contains the ID of the submitted transaction.

`_10

message SendTransactionResponse {

_10

bytes id = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetTransaction[​](#gettransaction "Direct link to GetTransaction")

`GetTransaction` gets a [transaction](#transaction) by ID.

If the transaction is not found in the access node cache, the request is forwarded to a collection node.

*Currently, only transactions within the current epoch can be queried.*

`_10

rpc GetTransaction (GetTransactionRequest) returns (TransactionResponse)`

#### Request[​](#request-10 "Direct link to Request")

`GetTransactionRequest` contains the ID of the transaction that is being queried.

`_10

message GetTransactionRequest {

_10

bytes id = 1;

_10

bytes block_id = 2;

_10

bytes collection_id = 3;

_10

entities.EventEncodingVersion event_encoding_version = 4;

_10

}`

#### Response[​](#response-10 "Direct link to Response")

`TransactionResponse` contains the basic information about a transaction, but does not include post-execution results.

`_10

message TransactionResponse {

_10

entities.Transaction transaction = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetTransactionsByBlockID[​](#gettransactionsbyblockid "Direct link to GetTransactionsByBlockID")

`GetTransactionsByBlockID` gets all the [transactions](#transaction) for a specified block.

`_10

rpc GetTransactionsByBlockID(GetTransactionsByBlockIDRequest) returns (TransactionsResponse);`

#### Request[​](#request-11 "Direct link to Request")

`_10

message GetTransactionsByBlockIDRequest {

_10

bytes block_id = 1;

_10

entities.EventEncodingVersion event_encoding_version = 2;

_10

}`

#### Response[​](#response-11 "Direct link to Response")

`_10

message TransactionsResponse {

_10

repeated entities.Transaction transactions = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetTransactionResult[​](#gettransactionresult "Direct link to GetTransactionResult")

`GetTransactionResult` gets the execution result of a transaction.

`_10

rpc GetTransactionResult (GetTransactionRequest) returns (TransactionResultResponse)`

#### Request[​](#request-12 "Direct link to Request")

`_10

message GetTransactionRequest {

_10

bytes id = 1;

_10

bytes block_id = 2;

_10

bytes collection_id = 3;

_10

entities.EventEncodingVersion event_encoding_version = 4;

_10

}`

#### Response[​](#response-12 "Direct link to Response")

`_12

message TransactionResultResponse {

_12

entities.TransactionStatus status = 1;

_12

uint32 status_code = 2;

_12

string error_message = 3;

_12

repeated entities.Event events = 4;

_12

bytes block_id = 5;

_12

bytes transaction_id = 6;

_12

bytes collection_id = 7;

_12

uint64 block_height = 8;

_12

entities.Metadata metadata = 9;

_12

uint64 computation_usage = 10;

_12

}`

### GetTransactionResultByIndex[​](#gettransactionresultbyindex "Direct link to GetTransactionResultByIndex")

`GetTransactionResultByIndex` gets a transaction's result at a specified block and index.

`_10

rpc GetTransactionResultByIndex(GetTransactionByIndexRequest) returns (TransactionResultResponse);`

#### Request[​](#request-13 "Direct link to Request")

`_10

message GetTransactionByIndexRequest {

_10

bytes block_id = 1;

_10

uint32 index = 2;

_10

entities.EventEncodingVersion event_encoding_version = 3;

_10

}`

#### Response[​](#response-13 "Direct link to Response")

`_12

message TransactionResultResponse {

_12

entities.TransactionStatus status = 1;

_12

uint32 status_code = 2;

_12

string error_message = 3;

_12

repeated entities.Event events = 4;

_12

bytes block_id = 5;

_12

bytes transaction_id = 6;

_12

bytes collection_id = 7;

_12

uint64 block_height = 8;

_12

entities.Metadata metadata = 9;

_12

uint64 computation_usage = 10;

_12

}`

### GetTransactionResultsByBlockID[​](#gettransactionresultsbyblockid "Direct link to GetTransactionResultsByBlockID")

`GetTransactionResultsByBlockID` gets all the transaction results for a specified block.

`_10

rpc GetTransactionResultsByBlockID(GetTransactionsByBlockIDRequest) returns (TransactionResultsResponse);`

#### Request[​](#request-14 "Direct link to Request")

`_10

message GetTransactionsByBlockIDRequest {

_10

bytes block_id = 1;

_10

entities.EventEncodingVersion event_encoding_version = 2;

_10

}`

#### Response[​](#response-14 "Direct link to Response")

`_10

message TransactionResultsResponse {

_10

repeated TransactionResultResponse transaction_results = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetSystemTransaction[​](#getsystemtransaction "Direct link to GetSystemTransaction")

`GetSystemTransaction` gets the system transaction for a block.

`_10

rpc GetSystemTransaction(GetSystemTransactionRequest) returns (TransactionResponse);`

#### Request[​](#request-15 "Direct link to Request")

`_10

message GetSystemTransactionRequest {

_10

bytes block_id = 1;

_10

}`

#### Response[​](#response-15 "Direct link to Response")

`_10

message TransactionResponse {

_10

entities.Transaction transaction = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetSystemTransactionResult[​](#getsystemtransactionresult "Direct link to GetSystemTransactionResult")

`GetSystemTransactionResult` gets the system transaction result for a block.

`_10

rpc GetSystemTransactionResult(GetSystemTransactionResultRequest) returns (TransactionResultResponse);`

#### Request[​](#request-16 "Direct link to Request")

`_10

message GetSystemTransactionResultRequest {

_10

bytes block_id = 1;

_10

entities.EventEncodingVersion event_encoding_version = 2;

_10

}`

#### Response[​](#response-16 "Direct link to Response")

`_12

message TransactionResultResponse {

_12

entities.TransactionStatus status = 1;

_12

uint32 status_code = 2;

_12

string error_message = 3;

_12

repeated entities.Event events = 4;

_12

bytes block_id = 5;

_12

bytes transaction_id = 6;

_12

bytes collection_id = 7;

_12

uint64 block_height = 8;

_12

entities.Metadata metadata = 9;

_12

uint64 computation_usage = 10;

_12

}`

---

## Accounts[​](#accounts "Direct link to Accounts")

### GetAccount[​](#getaccount "Direct link to GetAccount")

`GetAccount` gets an [account](#account) by address at the latest sealed block.

⚠️ Warning: this function is deprecated. It behaves identically to `GetAccountAtLatestBlock` and will be removed in a future version.

`_10

rpc GetAccount(GetAccountRequest) returns (GetAccountResponse)`

#### Request[​](#request-17 "Direct link to Request")

`_10

message GetAccountRequest {

_10

bytes address = 1;

_10

}`

#### Response[​](#response-17 "Direct link to Response")

`_10

message GetAccountResponse {

_10

entities.Account account = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountAtLatestBlock[​](#getaccountatlatestblock "Direct link to GetAccountAtLatestBlock")

`GetAccountAtLatestBlock` gets an [account](#account) by address.

The access node queries an execution node for the account details, which are stored as part of the sealed execution state.

`_10

rpc GetAccountAtLatestBlock(GetAccountAtLatestBlockRequest) returns (AccountResponse)`

#### Request[​](#request-18 "Direct link to Request")

`_10

message GetAccountAtLatestBlockRequest {

_10

bytes address = 1;

_10

}`

#### Response[​](#response-18 "Direct link to Response")

`_10

message AccountResponse {

_10

entities.Account account = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountAtBlockHeight[​](#getaccountatblockheight "Direct link to GetAccountAtBlockHeight")

`GetAccountAtBlockHeight` gets an [account](#accounts) by address at the given block height.

The access node queries an execution node for the account details, which are stored as part of the execution state.

`_10

rpc GetAccountAtBlockHeight(GetAccountAtBlockHeightRequest) returns (AccountResponse)`

#### Request[​](#request-19 "Direct link to Request")

`_10

message GetAccountAtBlockHeightRequest {

_10

bytes address = 1;

_10

uint64 block_height = 2;

_10

}`

#### Response[​](#response-19 "Direct link to Response")

`_10

message AccountResponse {

_10

entities.Account account = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountBalanceAtLatestBlock[​](#getaccountbalanceatlatestblock "Direct link to GetAccountBalanceAtLatestBlock")

`GetAccountBalanceAtLatestBlock` gets an account's balance by address from the latest sealed block.

`_10

rpc GetAccountBalanceAtLatestBlock(GetAccountBalanceAtLatestBlockRequest) returns (AccountBalanceResponse);`

#### Request[​](#request-20 "Direct link to Request")

`_10

message GetAccountBalanceAtLatestBlockRequest {

_10

bytes address = 1

_10

}`

#### Response[​](#response-20 "Direct link to Response")

`_10

message AccountBalanceResponse {

_10

uint64 balance = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountBalanceAtBlockHeight[​](#getaccountbalanceatblockheight "Direct link to GetAccountBalanceAtBlockHeight")

`GetAccountBalanceAtBlockHeight` gets an account's balance by address at the given block height.

`_10

rpc GetAccountBalanceAtBlockHeight(GetAccountBalanceAtBlockHeightRequest) returns (AccountBalanceResponse);`

#### Request[​](#request-21 "Direct link to Request")

`_10

message GetAccountBalanceAtBlockHeightRequest {

_10

bytes address = 1;

_10

uint64 block_height = 2;

_10

}`

#### Response[​](#response-21 "Direct link to Response")

`_10

message AccountBalanceResponse {

_10

uint64 balance = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountKeyAtLatestBlock[​](#getaccountkeyatlatestblock "Direct link to GetAccountKeyAtLatestBlock")

`GetAccountKeyAtLatestBlock` gets an account's public key by address and key index from the latest sealed block.

`_10

rpc GetAccountKeyAtLatestBlock(GetAccountKeyAtLatestBlockRequest) returns (AccountKeyResponse);`

#### Request[​](#request-22 "Direct link to Request")

`_10

message GetAccountKeyAtLatestBlockRequest {

_10

// address of account

_10

bytes address = 1;

_10

// index of key to return

_10

uint32 index = 2;

_10

}`

#### Response[​](#response-22 "Direct link to Response")

`_10

message AccountKeyResponse {

_10

entities.AccountKey account_key = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountKeyAtBlockHeight[​](#getaccountkeyatblockheight "Direct link to GetAccountKeyAtBlockHeight")

`GetAccountKeyAtBlockHeight` gets an account's public key by address and key index at the given block height.

`_10

rpc GetAccountKeyAtBlockHeight(GetAccountKeyAtBlockHeightRequest) returns (AccountKeyResponse);`

#### Request[​](#request-23 "Direct link to Request")

`_10

message GetAccountKeyAtBlockHeightRequest {

_10

// address of account

_10

bytes address = 1;

_10

// height of the block

_10

uint64 block_height = 2;

_10

// index of key to return

_10

uint32 index = 3;

_10

}`

#### Response[​](#response-23 "Direct link to Response")

`_10

message AccountKeyResponse {

_10

entities.AccountKey account_key = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountKeysAtLatestBlock[​](#getaccountkeysatlatestblock "Direct link to GetAccountKeysAtLatestBlock")

`GetAccountKeysAtLatestBlock` gets an account's public keys by address from the latest sealed block.

`_10

rpc GetAccountKeysAtLatestBlock(GetAccountKeysAtLatestBlockRequest) returns (AccountKeysResponse);`

#### Request[​](#request-24 "Direct link to Request")

`_10

message GetAccountKeysAtLatestBlockRequest {

_10

// address of account

_10

bytes address = 1;

_10

}`

#### Response[​](#response-24 "Direct link to Response")

`_10

message AccountKeysResponse {

_10

repeated entities.AccountKey account_keys = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetAccountKeysAtBlockHeight[​](#getaccountkeysatblockheight "Direct link to GetAccountKeysAtBlockHeight")

`GetAccountKeysAtBlockHeight` gets an account's public keys by address at the given block height.

`_10

rpc GetAccountKeysAtBlockHeight(GetAccountKeysAtBlockHeightRequest) returns (AccountKeysResponse);`

#### Request[​](#request-25 "Direct link to Request")

`_10

message GetAccountKeysAtBlockHeightRequest {

_10

// address of account

_10

bytes address = 1;

_10

uint64 block_height = 2;

_10

}`

#### Response[​](#response-25 "Direct link to Response")

`_10

message AccountKeysResponse {

_10

repeated entities.AccountKey account_keys = 1;

_10

entities.Metadata metadata = 2;

_10

}`

## 

## Scripts[​](#scripts "Direct link to Scripts")

### ExecuteScriptAtLatestBlock[​](#executescriptatlatestblock "Direct link to ExecuteScriptAtLatestBlock")

`ExecuteScriptAtLatestBlock` executes a read-only Cadence script against the latest sealed execution state.

This method can be used to read execution state from the blockchain. The script is executed on an execution node and the return value is encoded using the [JSON-Cadence data interchange format](https://cadencelang.dev/docs/1.0/json-cadence-spec).

`_10

rpc ExecuteScriptAtLatestBlock (ExecuteScriptAtLatestBlockRequest) returns (ExecuteScriptResponse)`

This method is a shortcut for the following:

`_10

header = GetLatestBlockHeader()

_10

value = ExecuteScriptAtBlockID(header.ID, script)`

#### Request[​](#request-26 "Direct link to Request")

`_10

message ExecuteScriptAtLatestBlockRequest {

_10

bytes script = 1;

_10

repeated bytes arguments = 2;

_10

}`

#### Response[​](#response-26 "Direct link to Response")

`_10

message ExecuteScriptResponse {

_10

bytes value = 1;

_10

entities.Metadata metadata = 2;

_10

uint64 computation_usage = 3;

_10

}`

### ExecuteScriptAtBlockID[​](#executescriptatblockid "Direct link to ExecuteScriptAtBlockID")

`ExecuteScriptAtBlockID` executes a ready-only Cadence script against the execution state at the block with the given ID.

This method can be used to read account state from the blockchain. The script is executed on an execution node and the return value is encoded using the [JSON-Cadence data interchange format](https://cadencelang.dev/docs/1.0/json-cadence-spec).

`_10

rpc ExecuteScriptAtBlockID (ExecuteScriptAtBlockIDRequest) returns (ExecuteScriptResponse)`

#### Request[​](#request-27 "Direct link to Request")

`_10

message ExecuteScriptAtBlockIDRequest {

_10

bytes block_id = 1;

_10

bytes script = 2;

_10

repeated bytes arguments = 3;

_10

}`

#### Response[​](#response-27 "Direct link to Response")

`_10

message ExecuteScriptResponse {

_10

bytes value = 1;

_10

entities.Metadata metadata = 2;

_10

uint64 computation_usage = 3;

_10

}`

### ExecuteScriptAtBlockHeight[​](#executescriptatblockheight "Direct link to ExecuteScriptAtBlockHeight")

`ExecuteScriptAtBlockHeight` executes a ready-only Cadence script against the execution state at the given block height.

This method can be used to read account state from the blockchain. The script is executed on an execution node and the return value is encoded using the [JSON-Cadence data interchange format](https://cadencelang.dev/docs/1.0/json-cadence-spec).

`_10

rpc ExecuteScriptAtBlockHeight (ExecuteScriptAtBlockHeightRequest) returns (ExecuteScriptResponse)`

#### Request[​](#request-28 "Direct link to Request")

`_10

message ExecuteScriptAtBlockHeightRequest {

_10

uint64 block_height = 1;

_10

bytes script = 2;

_10

repeated bytes arguments = 3;

_10

}`

#### Response[​](#response-28 "Direct link to Response")

`_10

message ExecuteScriptResponse {

_10

bytes value = 1;

_10

entities.Metadata metadata = 2;

_10

uint64 computation_usage = 3;

_10

}`

---

## Events[​](#events "Direct link to Events")

The following methods can be used to query for on-chain [events](#event).

### GetEventsForHeightRange[​](#geteventsforheightrange "Direct link to GetEventsForHeightRange")

`GetEventsForHeightRange` retrieves [events](#event) emitted within the specified block range.

`_10

rpc GetEventsForHeightRange(GetEventsForHeightRangeRequest) returns (GetEventsForHeightRangeResponse)`

Events can be requested for a specific sealed block range via the `start_height` and `end_height` (inclusive) fields and further filtered by event type via the `type` field.

If `start_height` is greater than the current sealed chain height, then this method will return an error.

If `end_height` is greater than the current sealed chain height, then this method will return events up to and including the latest sealed block.

The event results are grouped by block, with each group specifying a block ID, height and block timestamp.

Event types are name-spaced with the address of the account and contract in which they are declared.

#### Request[​](#request-29 "Direct link to Request")

`_10

message GetEventsForHeightRangeRequest {

_10

string type

_10

uint64 start_height = 2;

_10

uint64 end_height = 3;

_10

entities.EventEncodingVersion event_encoding_version = 4;

_10

}`

#### Response[​](#response-29 "Direct link to Response")

`_10

message EventsResponse {

_10

message Result {

_10

bytes block_id = 1;

_10

uint64 block_height = 2;

_10

repeated entities.Event events = 3;

_10

google.protobuf.Timestamp block_timestamp = 4;

_10

}

_10

repeated Result results = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetEventsForBlockIDs[​](#geteventsforblockids "Direct link to GetEventsForBlockIDs")

`GetEventsForBlockIDs` retrieves [events](#event) for the specified block IDs and event type.

`_10

rpc GetEventsForBlockIDs(GetEventsForBlockIDsRequest) returns (GetEventsForBlockIDsResponse)`

Events can be requested for a list of block IDs via the `block_ids` field and further filtered by event type via the `type` field.

The event results are grouped by block, with each group specifying a block ID, height and block timestamp.

#### Request[​](#request-30 "Direct link to Request")

`_10

message GetEventsForBlockIDsRequest {

_10

string type = 1;

_10

repeated bytes block_ids = 2;

_10

entities.EventEncodingVersion event_encoding_version = 3;

_10

}`

#### Response[​](#response-30 "Direct link to Response")

`_10

message EventsResponse {

_10

message Result {

_10

bytes block_id = 1;

_10

uint64 block_height = 2;

_10

repeated entities.Event events = 3;

_10

google.protobuf.Timestamp block_timestamp = 4;

_10

}

_10

repeated Result results = 1;

_10

entities.Metadata metadata = 2;

_10

}`

---

## Network Parameters[​](#network-parameters "Direct link to Network Parameters")

Network parameters provide information about the Flow network. Currently, it only includes the chain ID.
The following method can be used to query for network parameters.

### GetNetworkParameters[​](#getnetworkparameters "Direct link to GetNetworkParameters")

`GetNetworkParameters` retrieves the network parameters.

`_10

rpc GetNetworkParameters (GetNetworkParametersRequest) returns (GetNetworkParametersResponse)`

#### Request[​](#request-31 "Direct link to Request")

`_10

message GetNetworkParametersRequest {}`

#### Response[​](#response-31 "Direct link to Response")

`_10

message GetNetworkParametersResponse {

_10

string chain_id = 1;

_10

}`

| Field | Description |
| --- | --- |
| chain\_id | Chain ID helps identify the Flow network. It can be one of `flow-mainnet`, `flow-testnet` or `flow-emulator` |

---

### GetNodeVersionInfo[​](#getnodeversioninfo "Direct link to GetNodeVersionInfo")

`GetNodeVersionInfo` gets information about a node's current versions.

`_10

rpc GetNodeVersionInfo (GetNodeVersionInfoRequest) returns (GetNodeVersionInfoResponse);`

#### Request[​](#request-32 "Direct link to Request")

`_10

message GetNodeVersionInfoRequest {}`

#### Response[​](#response-32 "Direct link to Response")

`_10

message GetNodeVersionInfoResponse {

_10

entities.NodeVersionInfo info = 1;

_10

}`

---

## Protocol state snapshot[​](#protocol-state-snapshot "Direct link to Protocol state snapshot")

The following method can be used to query the latest protocol state [snapshot](https://github.com/onflow/flow-go/blob/master/state/protocol/snapshot.go).

### GetLatestProtocolStateSnapshot[​](#getlatestprotocolstatesnapshot "Direct link to GetLatestProtocolStateSnapshot")

`GetLatestProtocolStateSnapshot` retrieves the latest Protocol state snapshot serialized as a byte array.
It is used by Flow nodes joining the network to bootstrap a space-efficient local state.

`_10

rpc GetLatestProtocolStateSnapshot (GetLatestProtocolStateSnapshotRequest) returns (ProtocolStateSnapshotResponse);`

#### Request[​](#request-33 "Direct link to Request")

`_10

message GetLatestProtocolStateSnapshotRequest {}`

#### Response[​](#response-33 "Direct link to Response")

`_10

message ProtocolStateSnapshotResponse {

_10

bytes serializedSnapshot = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetProtocolStateSnapshotByBlockID[​](#getprotocolstatesnapshotbyblockid "Direct link to GetProtocolStateSnapshotByBlockID")

`GetProtocolStateSnapshotByBlockID` retrieves the latest sealed protocol state snapshot by block ID.
Used by Flow nodes joining the network to bootstrap a space-efficient local state.

`_10

rpc GetProtocolStateSnapshotByBlockID(GetProtocolStateSnapshotByBlockIDRequest) returns (ProtocolStateSnapshotResponse);`

#### Request[​](#request-34 "Direct link to Request")

`_10

message GetProtocolStateSnapshotByBlockIDRequest {

_10

bytes block_id = 1;

_10

}`

#### Response[​](#response-34 "Direct link to Response")

`_10

message ProtocolStateSnapshotResponse {

_10

bytes serializedSnapshot = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetProtocolStateSnapshotByHeight[​](#getprotocolstatesnapshotbyheight "Direct link to GetProtocolStateSnapshotByHeight")

`GetProtocolStateSnapshotByHeight` retrieves the latest sealed protocol state snapshot by block height.
Used by Flow nodes joining the network to bootstrap a space-efficient local state.

`_10

rpc GetProtocolStateSnapshotByHeight(GetProtocolStateSnapshotByHeightRequest) returns (ProtocolStateSnapshotResponse);`

#### Request[​](#request-35 "Direct link to Request")

`_10

message GetProtocolStateSnapshotByHeightRequest {

_10

uint64 block_height = 1;

_10

}`

#### Response[​](#response-35 "Direct link to Response")

`_10

message ProtocolStateSnapshotResponse {

_10

bytes serializedSnapshot = 1;

_10

entities.Metadata metadata = 2;

_10

}`

## Execution results[​](#execution-results "Direct link to Execution results")

The following method can be used to query the for [execution results](https://github.com/onflow/flow-go/blob/master/model/flow/execution_result.go) for a given block.

### GetExecutionResultForBlockID[​](#getexecutionresultforblockid "Direct link to GetExecutionResultForBlockID")

`GetExecutionResultForBlockID` retrieves execution result for given block. It is different from Transaction Results,
and contain data about chunks/collection level execution results rather than particular transactions.
Particularly, it contains `EventsCollection` hash for every chunk which can be used to verify the events for a block.

`_10

rpc GetExecutionResultForBlockID(GetExecutionResultForBlockIDRequest) returns (ExecutionResultForBlockIDResponse);`

#### Request[​](#request-36 "Direct link to Request")

`_10

message GetExecutionResultForBlockIDRequest {

_10

bytes block_id = 1;

_10

}`

#### Response[​](#response-36 "Direct link to Response")

`_10

message ExecutionResultForBlockIDResponse {

_10

flow.ExecutionResult execution_result = 1;

_10

entities.Metadata metadata = 2;

_10

}`

### GetExecutionResultByID[​](#getexecutionresultbyid "Direct link to GetExecutionResultByID")

`GetExecutionResultByID` returns Execution Result by its ID. It is different from Transaction Results,
and contain data about chunks/collection level execution results rather than particular transactions.
Particularly, it contains `EventsCollection` hash for every chunk which can be used to verify the events for a block.

`_10

rpc GetExecutionResultByID(GetExecutionResultByIDRequest) returns (ExecutionResultByIDResponse);`

#### Request[​](#request-37 "Direct link to Request")

`_10

message GetExecutionResultByIDRequest {

_10

bytes id = 1;

_10

}`

#### Response[​](#response-37 "Direct link to Response")

`_10

message ExecutionResultByIDResponse {

_10

flow.ExecutionResult execution_result = 1;

_10

entities.Metadata metadata = 2;

_10

}`

## Entities[​](#entities "Direct link to Entities")

Below are in-depth descriptions of each of the data entities returned or accepted by the Access API.

### Block[​](#block "Direct link to Block")

`_13

message Block {

_13

bytes id = 1;

_13

bytes parent_id = 2;

_13

uint64 height = 3;

_13

google.protobuf.Timestamp timestamp = 4;

_13

repeated CollectionGuarantee collection_guarantees = 5;

_13

repeated BlockSeal block_seals = 6;

_13

repeated bytes signatures = 7;

_13

repeated ExecutionReceiptMeta execution_receipt_metaList = 8;

_13

repeated ExecutionResult execution_result_list = 9;

_13

BlockHeader block_header = 10;

_13

bytes protocol_state_id = 11;

_13

}`

| Field | Description |
| --- | --- |
| id | SHA3-256 hash of the entire block payload |
| height | Height of the block in the chain |
| parent\_id | ID of the previous block in the chain |
| timestamp | Timestamp of when the proposer claims it constructed the block.   **NOTE**: It is included by the proposer, there are no guarantees on how much the time stamp can deviate from the true time the block was published.   Consider observing blocks' status changes yourself to get a more reliable value |
| collection\_guarantees | List of [collection guarantees](#collection-guarantee) |
| block\_seals | List of [block seals](#block-seal) |
| signatures | BLS signatures of consensus nodes |
| execution\_receipt\_metaList | List of [execution-receipt-meta](#execution-receipt-meta) |
| execution\_result\_list | List of [execution results](#execution-result) |
| block\_header | A summary of a [block](#block-header) |
| protocol\_state\_id | The root hash of protocol state. |

The detailed semantics of block formation are covered in the [block formation guide](/build/basics/blocks).

### Block Header[​](#block-header "Direct link to Block Header")

A block header is a summary of a [block](#block) and contains only the block ID, height, and parent block ID.

`_16

message BlockHeader {

_16

bytes id = 1;

_16

bytes parent_id = 2;

_16

uint64 height = 3;

_16

google.protobuf.Timestamp timestamp = 4;

_16

bytes payload_hash = 5;

_16

uint64 view = 6;

_16

repeated bytes parent_voter_ids = 7;

_16

bytes parent_voter_sig_data = 8;

_16

bytes proposer_id = 9;

_16

bytes proposer_sig_data = 10;

_16

string chain_id = 11;

_16

bytes parent_voter_indices = 12;

_16

TimeoutCertificate last_view_tc = 13;

_16

uint64 parent_view = 14;

_16

}`

| Field | Description |
| --- | --- |
| id | SHA3-256 hash of the entire block payload |
| parent\_id | ID of the previous block in the chain |
| height | Height of the block in the chain |
| timestamp | The time at which this block was proposed |
| payload\_hash | A hash of the payload of this block |
| view | View number during which this block was proposed. |
| parent\_voter\_ids | An array that represents all the voters ids for the parent block |
| parent\_voter\_sig\_data | An aggregated signature over the parent block |
| chain\_id | Chain ID helps identify the Flow network. It can be one of `flow-mainnet`, `flow-testnet` or `flow-emulator` |
| parent\_voter\_indices | A bitvector that represents all the voters for the parent block |
| last\_view\_tc | A timeout certificate for previous view, it can be nil. It has to be present if previous round ended with timeout |
| parent\_view | A number at which parent block was proposed |

### Block Seal[​](#block-seal "Direct link to Block Seal")

A block seal is an attestation that the execution result of a specific [block](#block) has been verified and approved by a quorum of verification nodes.

`_10

message BlockSeal {

_10

bytes block_id = 1;

_10

bytes execution_receipt_id = 2;

_10

repeated bytes execution_receipt_signatures = 3;

_10

repeated bytes result_approval_signatures = 4;

_10

}`

| Field | Description |
| --- | --- |
| block\_id | ID of the block being sealed |
| execution\_receipt\_id | ID execution receipt being sealed |
| execution\_receipt\_signatures | BLS signatures of verification nodes on the execution receipt contents |
| result\_approval\_signatures | BLS signatures of verification nodes on the result approval contents |

### Block Status[​](#block-status "Direct link to Block Status")

`_10

enum BlockStatus {

_10

UNKNOWN = 0;

_10

FINALIZED = 1;

_10

SEALED = 2;

_10

}`

| Value | Description |
| --- | --- |
| UNKNOWN | The block status is not known |
| FINALIZED | The consensus nodes have finalized the block |
| SEALED | The verification nodes have verified the block |

### Collection[​](#collection "Direct link to Collection")

A collection is a batch of [transactions](#transaction) that have been included in a block. Collections are used to improve consensus throughput by increasing the number of transactions per block.

`_10

message Collection {

_10

bytes id = 1;

_10

repeated bytes transaction_ids = 2;

_10

}`

| Field | Description |
| --- | --- |
| id | SHA3-256 hash of the collection contents |
| transaction\_ids | Ordered list of transaction IDs in the collection |

### Collection Guarantee[​](#collection-guarantee "Direct link to Collection Guarantee")

A collection guarantee is a signed attestation that specifies the collection nodes that have guaranteed to store and respond to queries about a collection.

`_10

message CollectionGuarantee {

_10

bytes collection_id = 1;

_10

repeated bytes signatures = 2;

_10

bytes reference_block_id = 3;

_10

bytes signature = 4;

_10

repeated bytes signer_ids = 5; // deprecated!! value will be empty. replaced by signer_indices

_10

bytes signer_indices = 6;

_10

}`

| Field | Description |
| --- | --- |
| collection\_id | SHA3-256 hash of the collection contents |
| signatures | BLS signatures of the collection nodes guaranteeing the collection |
| reference\_block\_id | Defines expiry of the collection |
| signature | Guarantor signatures |
| signer\_ids | An array that represents all the signer ids |
| signer\_indices | Encoded indices of the signers |

### Transaction[​](#transaction "Direct link to Transaction")

A transaction represents a unit of computation that is submitted to the Flow network.

`_23

message Transaction {

_23

bytes script = 1;

_23

repeated bytes arguments = 2;

_23

bytes reference_block_id = 3;

_23

uint64 gas_limit = 4;

_23

ProposalKey proposal_key = 5;

_23

bytes payer = 6;

_23

repeated bytes authorizers = 7;

_23

repeated Signature payload_signatures = 8;

_23

repeated Signature envelope_signatures = 9;

_23

}

_23

_23

message TransactionProposalKey {

_23

bytes address = 1;

_23

uint32 key_id = 2;

_23

uint64 sequence_number = 3;

_23

}

_23

_23

message TransactionSignature {

_23

bytes address = 1;

_23

uint32 key_id = 2;

_23

bytes signature = 3;

_23

}`

| Field | Description |
| --- | --- |
| script | Raw source code for a Cadence script, encoded as UTF-8 bytes |
| arguments | Arguments passed to the Cadence script, encoded as [JSON-Cadence](https://cadencelang.dev/docs/1.0/json-cadence-spec) bytes |
| reference\_block\_id | Block ID used to determine transaction expiry |
| [proposal\_key](#proposal-key) | Account key used to propose the transaction |
| payer | Address of the payer account |
| authorizers | Addresses of the transaction authorizers |
| signatures | [Signatures](#transaction-signature) from all signer accounts |

The detailed semantics of transaction creation, signing and submission are covered in the [transaction submission guide](/build/basics/transactions#signing-a-transaction).

#### Proposal Key[​](#proposal-key "Direct link to Proposal Key")

The proposal key is used to specify a sequence number for the transaction. Sequence numbers are covered in more detail [here](/build/basics/transactions#sequence-numbers).

| Field | Description |
| --- | --- |
| address | Address of proposer account |
| key\_id | ID of proposal key on the proposal account |
| sequence\_number | [Sequence number](/build/basics/transactions#sequence-numbers) for the proposal key |

#### Transaction Signature[​](#transaction-signature "Direct link to Transaction Signature")

| Field | Description |
| --- | --- |
| address | Address of the account for this signature |
| key\_id | ID of the account key |
| signature | Raw signature byte data |

#### Transaction Status[​](#transaction-status "Direct link to Transaction Status")

`_10

enum TransactionStatus {

_10

UNKNOWN = 0;

_10

PENDING = 1;

_10

FINALIZED = 2;

_10

EXECUTED = 3;

_10

SEALED = 4;

_10

EXPIRED = 5;

_10

}`

| Value | Description |
| --- | --- |
| UNKNOWN | The transaction status is not known. |
| PENDING | The transaction has been received by a collector but not yet finalized in a block. |
| FINALIZED | The consensus nodes have finalized the block that the transaction is included in |
| EXECUTED | The execution nodes have produced a result for the transaction |
| SEALED | The verification nodes have verified the transaction (the block in which the transaction is) and the seal is included in the latest block |
| EXPIRED | The transaction was submitted past its expiration block height. |

### Account[​](#account "Direct link to Account")

An account is a user's identity on Flow. It contains a unique address, a balance, a list of public keys and the code that has been deployed to the account.

`_10

message Account {

_10

bytes address = 1;

_10

uint64 balance = 2;

_10

bytes code = 3;

_10

repeated AccountKey keys = 4;

_10

map<string, bytes> contracts = 5;

_10

}`

| Field | Description |
| --- | --- |
| address | A unique account identifier |
| balance | The account balance |
| code | The code deployed to this account (**deprecated**, use `contracts` instead) |
| keys | A list of keys configured on this account |
| contracts | A map of contracts or contract interfaces deployed on this account |

The `code` and `contracts` fields contain the raw Cadence source code, encoded as UTF-8 bytes.

More information on accounts can be found [here](/build/basics/accounts).

#### Account Key[​](#account-key "Direct link to Account Key")

An account key is a reference to a public key associated with a Flow account. Accounts can be configured with zero or more public keys, each of which can be used for signature verification when authorizing a transaction.

`_10

message AccountKey {

_10

uint32 index = 1;

_10

bytes public_key = 2;

_10

uint32 sign_algo = 3;

_10

uint32 hash_algo = 4;

_10

uint32 weight = 5;

_10

uint32 sequence_number = 6;

_10

bool revoked = 7;

_10

}`

| Field | Description |
| --- | --- |
| id | Index of the key within the account, used as a unique identifier |
| public\_key | Public key encoded as bytes |
| sign\_algo | [Signature algorithm](/build/basics/accounts#signature-and-hash-algorithms) |
| hash\_algo | [Hash algorithm](/build/basics/accounts#signature-and-hash-algorithms) |
| weight | [Weight assigned to the key](/build/basics/accounts#account-keys) |
| sequence\_number | [Sequence number for the key](/build/basics/transactions#sequence-numbers) |
| revoked | Flag indicating whether or not the key has been revoked |

More information on account keys, key weights and sequence numbers can be found [here](/build/basics/accounts).

### Event[​](#event "Direct link to Event")

An event is emitted as the result of a [transaction](#transaction) execution. Events are either user-defined events originating from a Cadence smart contract, or built-in Flow system events.

`_10

message Event {

_10

string type = 1;

_10

bytes transaction_id = 2;

_10

uint32 transaction_index = 3;

_10

uint32 event_index = 4;

_10

bytes payload = 5;

_10

}`

| Field | Description |
| --- | --- |
| type | Fully-qualified unique type identifier for the event |
| transaction\_id | ID of the transaction the event was emitted from |
| transaction\_index | Zero-based index of the transaction within the block |
| event\_index | Zero-based index of the event within the transaction |
| payload | Event fields encoded as [JSON-Cadence values](https://cadencelang.dev/docs/1.0/json-cadence-spec) |

### Execution Result[​](#execution-result "Direct link to Execution Result")

Execution result for a particular block.

`_10

message ExecutionResult {

_10

bytes previous_result_id = 1;

_10

bytes block_id = 2;

_10

repeated Chunk chunks = 3;

_10

repeated ServiceEvent service_events = 4;

_10

}`

| Field | Description |
| --- | --- |
| previous\_result\_id | Identifier of parent block execution result |
| block\_id | ID of the block this execution result corresponds to |
| chunks | Zero or more chunks |
| service\_events | Zero or more service events |

### Execution Receipt Meta[​](#execution-receipt-meta "Direct link to Execution Receipt Meta")

ExecutionReceiptMeta contains the fields from the Execution Receipts that vary from one executor to another

`_10

message ExecutionReceiptMeta {

_10

bytes executor_id = 1;

_10

bytes result_id = 2;

_10

repeated bytes spocks = 3;

_10

bytes executor_signature = 4;

_10

}`

| Field | Description |
| --- | --- |
| executor\_id | Identifier of the executor node |
| result\_id | Identifier of block execution result |
| spocks | SPoCK |
| executor\_signature | Signature of the executor |

#### Chunk[​](#chunk "Direct link to Chunk")

Chunk described execution information for given collection in a block

`_12

message Chunk {

_12

uint32 CollectionIndex = 1;

_12

bytes start_state = 2;

_12

bytes event_collection = 3;

_12

bytes block_id = 4;

_12

uint64 total_computation_used = 5;

_12

uint32 number_of_transactions = 6;

_12

uint64 index = 7;

_12

bytes end_state = 8;

_12

bytes execution_data_id = 9;

_12

bytes state_delta_commitment = 10;

_12

}`

| Field | Description |
| --- | --- |
| CollectionIndex | Identifier of a collection |
| start\_state | State commitment at start of the chunk |
| event\_collection | Hash of events emitted by transactions in this chunk |
| block\_id | Identifier of a block |
| total\_computation\_used | Total computation used by transactions in this chunk |
| number\_of\_transactions | Number of transactions in a chunk |
| index | Index of chunk inside a block (zero-based) |
| end\_state | State commitment after executing chunk |
| execution\_data\_id | Identifier of a execution data |
| state\_delta\_commitment | A commitment over sorted list of register changes |

#### Service Event[​](#service-event "Direct link to Service Event")

Special type of events emitted in system chunk used for controlling Flow system.

`_10

message ServiceEvent {

_10

string type = 1;

_10

bytes payload = 2;

_10

}`

| Field | Description |
| --- | --- |
| type | Type of an event |
| payload | JSON-serialized content of an event |

## Subscriptions[​](#subscriptions "Direct link to Subscriptions")

### SubscribeEvents[​](#subscribeevents "Direct link to SubscribeEvents")

`SubscribeEvents` streams events for all blocks starting at the requested start block, up until the latest available block. Once the latest is
reached, the stream will remain open and responses are sent for each new block as it becomes available.

Events within each block are filtered by the provided [EventFilter](#eventfilter), and only those events that match the filter are returned. If no filter is provided,
all events are returned.

Responses are returned for each block containing at least one event that matches the filter. Additionally, heatbeat responses (SubscribeEventsResponse
with no events) are returned periodically to allow clients to track which blocks were searched. Clients can use this information to determine
which block to start from when reconnecting.

`_10

rpc SubscribeEvents(SubscribeEventsRequest) returns (stream SubscribeEventsResponse)`

#### Request[​](#request-38 "Direct link to Request")

`_10

message SubscribeEventsRequest {

_10

bytes start_block_id = 1;

_10

uint64 start_block_height = 2;

_10

EventFilter filter = 3;

_10

uint64 heartbeat_interval = 4;

_10

entities.EventEncodingVersion event_encoding_version = 5;

_10

}`

| Field | Description |
| --- | --- |
| start\_block\_id | The first block to search for events. Only one of start\_block\_id and start\_block\_height may be provided, otherwise an InvalidArgument error is returned. If neither are provided, the latest sealed block is used |
| start\_block\_height | Block height of the first block to search for events. Only one of start\_block\_id and start\_block\_height may be provided, otherwise an InvalidArgument error is returned. If neither are provided, the latest sealed block is used |
| filter | Filter to apply to events for each block searched. If no filter is provided, all events are returned |
| heartbeat\_interval | Interval in block heights at which the server should return a heartbeat message to the client |
| event\_encoding\_version | Preferred event encoding version of the block events payload. Possible variants: CCF, JSON-CDC |

#### Response[​](#response-38 "Direct link to Response")

`_10

message SubscribeEventsResponse {

_10

bytes block_id = 1;

_10

uint64 block_height = 2;

_10

repeated entities.Event events = 3;

_10

google.protobuf.Timestamp block_timestamp = 4;

_10

uint64 message_index = 5;

_10

}`

### SubscribeExecutionData[​](#subscribeexecutiondata "Direct link to SubscribeExecutionData")

`SubscribeExecutionData` streams execution data for all blocks starting at the requested start block, up until the latest available block. Once the latest is reached, the stream will remain open and responses are sent for each new execution data as it becomes available.

`_10

rpc SubscribeExecutionData(SubscribeExecutionDataRequest) returns (stream SubscribeExecutionDataResponse)`

#### Request[​](#request-39 "Direct link to Request")

`_10

message SubscribeExecutionDataRequest {

_10

bytes start_block_id = 1;

_10

uint64 start_block_height = 2;

_10

entities.EventEncodingVersion event_encoding_version = 3;

_10

}`

| Field | Description |
| --- | --- |
| start\_block\_id | The first block to get execution data for. Only one of start\_block\_id and start\_block\_height may be provided, otherwise an InvalidArgument error is returned. If neither are provided, the latest sealed block is used |
| start\_block\_height | Block height of the first block to get execution data for. Only one of start\_block\_id and start\_block\_height may be provided, otherwise an InvalidArgument error is returned. If neither are provided, the latest sealed block is used |
| event\_encoding\_version | Preferred event encoding version of the block events payload. Possible variants: CCF, JSON-CDC |

#### Response[​](#response-39 "Direct link to Response")

`_10

message SubscribeExecutionDataResponse {

_10

uint64 block_height = 1;

_10

entities.BlockExecutionData block_execution_data = 2;

_10

google.protobuf.Timestamp block_timestamp = 3;

_10

}`

## Execution data[​](#execution-data "Direct link to Execution data")

### EventFilter[​](#eventfilter "Direct link to EventFilter")

`EventFilter` defines the filter to apply to block events. Filters are applied as an OR operation, i.e. any event matching any of the filters is returned.
If no filters are provided, all events are returned. If there are any invalid filters, the API will return an InvalidArgument error.

`_10

message EventFilter {

_10

repeated string event_type = 1;

_10

repeated string contract = 2;

_10

repeated string address = 3;

_10

}`

| Field | Description |
| --- | --- |
| event\_type | A list of full event types to include.   Event types have 2 formats:  \_ Protocol events: `flow.[event name]`  \_ Smart contract events: `A.[contract address].[contract name].[event name]` |
| contract | A list of contracts who's events should be included. Contracts have the following name formats:  \_ Protocol events: `flow`  \_ Smart contract events: `A.[contract address].[contract name]`  This filter matches on the full contract including its address, not just the contract's name |
| address | A list of addresses who's events should be included. Addresses must be Flow account addresses in hex format and valid for the network the node is connected to. i.e. only a mainnet address is valid for a mainnet node. Addresses may optionally include the `0x` prefix |

## Execution data streaming API[​](#execution-data-streaming-api "Direct link to Execution data streaming API")

### Execution Data API[​](#execution-data-api "Direct link to Execution Data API")

The `ExecutionDataAPI` provides access to block execution data over gRPC, including transactions, events, and register data (account state). It’s an optional API, which makes use of the Execution Sync protocol to trustlessly download data from peers on the network.

[execution data protobuf file](https://github.com/onflow/flow/blob/master/protobuf/flow/executiondata/executiondata.proto)

> The API is disabled by default. To enable it, specify a listener address with the cli flag `--state-stream-addr`.

ℹ️ Currently, the api must be started on a separate port from the regular gRPC endpoint. There is work underway to add support for using the same port.

Below is a list of the available CLI flags to control the behavior of the API

| Flag | Type | Description |
| --- | --- | --- |
| state-stream-addr | string | Listener address for API. e.g. 0.0.0.0:9003. If no value is provided, the API is disabled. Default is disabled. |
| execution-data-cache-size | uint32 | Number of block execution data objects to store in the cache. Default is 100. |
| state-stream-global-max-streams | uint32 | Global maximum number of concurrent streams. Default is 1000. |
| state-stream-max-message-size | uint | Maximum size for a gRPC response message containing block execution data. Default is 20*1024*1024 (20MB). |
| state-stream-event-filter-limits | string | Event filter limits for ExecutionData SubscribeEvents API. These define the max number of filters for each type. e.g. EventTypes=100,Addresses=20,Contracts=50. Default is 1000 for each. |
| state-stream-send-timeout | duration | Maximum wait before timing out while sending a response to a streaming client. Default is 30s. |
| state-stream-send-buffer-size | uint | Maximum number of unsent responses to buffer for a stream. Default is 10. |
| state-stream-response-limit | float64 | Max number of responses per second to send over streaming endpoints. This effectively applies a rate limit to responses to help manage resources consumed by each client. This is mostly used when clients are querying data past data. e.g. 3 or 0.5. Default is 0 which means no limit. |

ℹ️ This API provides access to Execution Data, which can be very large (100s of MB) for a given block. Given the large amount of data, operators should consider their expected usage patters and tune the available settings to limit the resources a single client can use. It may also be useful to use other means of managing traffic, such as reverse proxies or QoS tools.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/access-onchain-data/index.md)

Last updated on **Apr 3, 2025** by **Brian Doyle**

[Previous

Managing disk space](/networks/node-ops/node-operation/reclaim-disk)[Next

Access HTTP API ↗️](/networks/access-onchain-data/access-http-api)

###### Rate this page

😞😐😊

* [Flow Access Node Endpoints](#flow-access-node-endpoints)
* [Ping](#ping)
* [Block Headers](#block-headers)
  + [GetLatestBlockHeader](#getlatestblockheader)
  + [GetBlockHeaderByID](#getblockheaderbyid)
  + [GetBlockHeaderByHeight](#getblockheaderbyheight)
* [Blocks](#blocks)
  + [GetLatestBlock](#getlatestblock)
  + [GetBlockByID](#getblockbyid)
  + [GetBlockByHeight](#getblockbyheight)
* [Collections](#collections)
  + [GetCollectionByID](#getcollectionbyid)
  + [GetFullCollectionByID](#getfullcollectionbyid)
* [Transactions](#transactions)
  + [SendTransaction](#sendtransaction)
  + [GetTransaction](#gettransaction)
  + [GetTransactionsByBlockID](#gettransactionsbyblockid)
  + [GetTransactionResult](#gettransactionresult)
  + [GetTransactionResultByIndex](#gettransactionresultbyindex)
  + [GetTransactionResultsByBlockID](#gettransactionresultsbyblockid)
  + [GetSystemTransaction](#getsystemtransaction)
  + [GetSystemTransactionResult](#getsystemtransactionresult)
* [Accounts](#accounts)
  + [GetAccount](#getaccount)
  + [GetAccountAtLatestBlock](#getaccountatlatestblock)
  + [GetAccountAtBlockHeight](#getaccountatblockheight)
  + [GetAccountBalanceAtLatestBlock](#getaccountbalanceatlatestblock)
  + [GetAccountBalanceAtBlockHeight](#getaccountbalanceatblockheight)
  + [GetAccountKeyAtLatestBlock](#getaccountkeyatlatestblock)
  + [GetAccountKeyAtBlockHeight](#getaccountkeyatblockheight)
  + [GetAccountKeysAtLatestBlock](#getaccountkeysatlatestblock)
  + [GetAccountKeysAtBlockHeight](#getaccountkeysatblockheight)
* [Scripts](#scripts)
  + [ExecuteScriptAtLatestBlock](#executescriptatlatestblock)
  + [ExecuteScriptAtBlockID](#executescriptatblockid)
  + [ExecuteScriptAtBlockHeight](#executescriptatblockheight)
* [Events](#events)
  + [GetEventsForHeightRange](#geteventsforheightrange)
  + [GetEventsForBlockIDs](#geteventsforblockids)
* [Network Parameters](#network-parameters)
  + [GetNetworkParameters](#getnetworkparameters)
  + [GetNodeVersionInfo](#getnodeversioninfo)
* [Protocol state snapshot](#protocol-state-snapshot)
  + [GetLatestProtocolStateSnapshot](#getlatestprotocolstatesnapshot)
  + [GetProtocolStateSnapshotByBlockID](#getprotocolstatesnapshotbyblockid)
  + [GetProtocolStateSnapshotByHeight](#getprotocolstatesnapshotbyheight)
* [Execution results](#execution-results)
  + [GetExecutionResultForBlockID](#getexecutionresultforblockid)
  + [GetExecutionResultByID](#getexecutionresultbyid)
* [Entities](#entities)
  + [Block](#block)
  + [Block Header](#block-header)
  + [Block Seal](#block-seal)
  + [Block Status](#block-status)
  + [Collection](#collection)
  + [Collection Guarantee](#collection-guarantee)
  + [Transaction](#transaction)
  + [Account](#account)
  + [Event](#event)
  + [Execution Result](#execution-result)
  + [Execution Receipt Meta](#execution-receipt-meta)
* [Subscriptions](#subscriptions)
  + [SubscribeEvents](#subscribeevents)
  + [SubscribeExecutionData](#subscribeexecutiondata)
* [Execution data](#execution-data)
  + [EventFilter](#eventfilter)
* [Execution data streaming API](#execution-data-streaming-api)
  + [Execution Data API](#execution-data-api)

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