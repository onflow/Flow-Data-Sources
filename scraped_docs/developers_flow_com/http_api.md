# Source: https://developers.flow.com/http-api




Access API | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* Blocks
  + getGets Blocks by Height
  + getGet Blocks by ID.
  + getGet Block Payload by Block ID.
* Transactions
  + getGet a Transaction by ID.
  + getGet a Transaction Result by ID.
  + postSubmit a Transaction
* Collections
  + getGets a Collection by ID
* Execution Results
  + getGet Execution Results by Block ID
  + getGet Execution Result by ID
* Accounts
  + getGet an Account By Address
  + getGet an individual Account Key By Address and Index
* Scripts
  + postExecute a Cadence Script
* Events
  + getGet Events
* Network
  + getGet Network Parameters
* NodeVersionInfo
  + getGet Node Version Information
* Subscribe events
  + getSubscribe events

[API docs by Redocly](https://redocly.com/redoc/)
# Access API (1.0.0)

Download OpenAPI specification:[Download](https://raw.githubusercontent.com/onflow/flow/master/openapi/access.yaml)

[Find out more about the Access API](https://docs.onflow.org/access-api/)
## Blocks

## Gets Blocks by Height

Get block data by the provided height range or list of heights.

##### query Parameters

| height | Array of strings or strings (BlockHeight)   non-empty  unique   A comma-separated list of block heights to get. This parameter is incompatible with `start_height` and `end_height`. |
| --- | --- |
| start\_height | string or string (BlockHeight)   The start height of the block range to get. Must be used together with `end_height`. This parameter is incompatible with `height`. |
| end\_height | string or string (BlockHeight)   The ending height of the block range to get. Must be used together with `start_height`. This parameter is incompatible with `height`. |
| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/blocks

Flow Canary

https://rest-canary.onflow.org/v1/blocks

Flow Testnet

https://rest-testnet.onflow.org/v1/blocks

Flow Mainnet

https://rest-mainnet.onflow.org/v1/blocks
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `[

* {
  + "header": {
    - "id": "string",
    - "parent_id": "string",
    - "height": "string",
    - "timestamp": "2019-08-24T14:15:22Z",
    - "parent_voter_signature": "string"},
  + "payload": {
    - "collection_guarantees": [
      * {
        + "collection_id": "string",
        + "signer_ids": [
          - "string"],
        + "signature": "string"}],
    - "block_seals": [
      * {
        + "block_id": "string",
        + "result_id": "string",
        + "final_state": "string",
        + "aggregated_approval_signatures": [
          - {
            * "verifier_signatures": [
              + "string"],
            * "signer_ids": [
              + "string"]}]}]},
  + "execution_result": {
    - "id": "string",
    - "block_id": "string",
    - "events": [
      * {
        + "type": "string",
        + "transaction_id": "string",
        + "transaction_index": "string",
        + "event_index": "string",
        + "payload": "string"}],
    - "chunks": [
      * {
        + "block_id": "string",
        + "collection_index": "string",
        + "start_state": "string",
        + "end_state": "string",
        + "event_collection": "string",
        + "index": "string",
        + "number_of_transactions": "string",
        + "total_computation_used": "string"}],
    - "previous_result_id": "string",
    - "_links": {
      * "_self": "string"}},
  + "_expandable": {
    - "payload": "string",
    - "execution_result": "<http://example.com>"},
  + "_links": {
    - "_self": "string"},
  + "block_status": "BLOCK_UNKNOWN"}

]`
## Get Blocks by ID.

Get a block data or list of blocks by the provided ID or list of IDs.

##### path Parameters

| idrequired | Array of strings <hexadecimal>  (Identifier)   [ 1 .. 50 ] items  unique [[a-fA-F0-9]{64}]  A block ID or comma-separated list of block IDs. |
| --- | --- |

##### query Parameters

| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| --- | --- |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/blocks/{id}

Flow Canary

https://rest-canary.onflow.org/v1/blocks/{id}

Flow Testnet

https://rest-testnet.onflow.org/v1/blocks/{id}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/blocks/{id}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `[

* {
  + "header": {
    - "id": "string",
    - "parent_id": "string",
    - "height": "string",
    - "timestamp": "2019-08-24T14:15:22Z",
    - "parent_voter_signature": "string"},
  + "payload": {
    - "collection_guarantees": [
      * {
        + "collection_id": "string",
        + "signer_ids": [
          - "string"],
        + "signature": "string"}],
    - "block_seals": [
      * {
        + "block_id": "string",
        + "result_id": "string",
        + "final_state": "string",
        + "aggregated_approval_signatures": [
          - {
            * "verifier_signatures": [
              + "string"],
            * "signer_ids": [
              + "string"]}]}]},
  + "execution_result": {
    - "id": "string",
    - "block_id": "string",
    - "events": [
      * {
        + "type": "string",
        + "transaction_id": "string",
        + "transaction_index": "string",
        + "event_index": "string",
        + "payload": "string"}],
    - "chunks": [
      * {
        + "block_id": "string",
        + "collection_index": "string",
        + "start_state": "string",
        + "end_state": "string",
        + "event_collection": "string",
        + "index": "string",
        + "number_of_transactions": "string",
        + "total_computation_used": "string"}],
    - "previous_result_id": "string",
    - "_links": {
      * "_self": "string"}},
  + "_expandable": {
    - "payload": "string",
    - "execution_result": "<http://example.com>"},
  + "_links": {
    - "_self": "string"},
  + "block_status": "BLOCK_UNKNOWN"}

]`
## Get Block Payload by Block ID.

Get a block payload data by the provided block ID.

##### path Parameters

| idrequired | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  A block ID. |
| --- | --- |

##### query Parameters

| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| --- | --- |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/blocks/{id}/payload

Flow Canary

https://rest-canary.onflow.org/v1/blocks/{id}/payload

Flow Testnet

https://rest-testnet.onflow.org/v1/blocks/{id}/payload

Flow Mainnet

https://rest-mainnet.onflow.org/v1/blocks/{id}/payload
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "collection_guarantees": [
  + {
    - "collection_id": "string",
    - "signer_ids": [
      * "string"],
    - "signature": "string"}],
* "block_seals": [
  + {
    - "block_id": "string",
    - "result_id": "string",
    - "final_state": "string",
    - "aggregated_approval_signatures": [
      * {
        + "verifier_signatures": [
          - "string"],
        + "signer_ids": [
          - "string"]}]}]

}`
## Transactions

## Get a Transaction by ID.

Get a transaction data by the provided transaction ID.

##### path Parameters

| idrequired | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  The ID of the transaction to get. |
| --- | --- |

##### query Parameters

| block\_id | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  A block ID optional parameter |
| --- | --- |
| collection\_id | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  A collection ID optional parameter. |
| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/transactions/{id}

Flow Canary

https://rest-canary.onflow.org/v1/transactions/{id}

Flow Testnet

https://rest-testnet.onflow.org/v1/transactions/{id}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/transactions/{id}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "id": "string",
* "script": "string",
* "arguments": [
  + "string"],
* "reference_block_id": "string",
* "gas_limit": "string",
* "payer": "string",
* "proposal_key": {
  + "address": "string",
  + "key_index": "string",
  + "sequence_number": "string"},
* "authorizers": [
  + "string"],
* "payload_signatures": [
  + {
    - "address": "string",
    - "key_index": "string",
    - "signature": "string"}],
* "envelope_signatures": [
  + {
    - "address": "string",
    - "key_index": "string",
    - "signature": "string"}],
* "result": {
  + "block_id": "string",
  + "collection_id": "string",
  + "execution": "Pending",
  + "status": "Pending",
  + "status_code": 0,
  + "error_message": "string",
  + "computation_used": "string",
  + "events": [
    - {
      * "type": "string",
      * "transaction_id": "string",
      * "transaction_index": "string",
      * "event_index": "string",
      * "payload": "string"}],
  + "_links": {
    - "_self": "string"}},
* "_expandable": {
  + "result": "<http://example.com>"},
* "_links": {
  + "_self": "string"}

}`
## Get a Transaction Result by ID.

Get transaction result by the transaction result ID.

##### path Parameters

| transaction\_idrequired | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  The transaction ID of the transaction result. |
| --- | --- |

##### query Parameters

| block\_id | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  A block ID optional parameter |
| --- | --- |
| collection\_id | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  A collection ID optional parameter. |
| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/transaction\_results/{transaction\_id}

Flow Canary

https://rest-canary.onflow.org/v1/transaction\_results/{transaction\_id}

Flow Testnet

https://rest-testnet.onflow.org/v1/transaction\_results/{transaction\_id}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/transaction\_results/{transaction\_id}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "block_id": "string",
* "collection_id": "string",
* "execution": "Pending",
* "status": "Pending",
* "status_code": 0,
* "error_message": "string",
* "computation_used": "string",
* "events": [
  + {
    - "type": "string",
    - "transaction_id": "string",
    - "transaction_index": "string",
    - "event_index": "string",
    - "payload": "string"}],
* "_links": {
  + "_self": "string"}

}`
## Submit a Transaction

Send a new signed transaction payload to the network with [required transaction fields](https://docs.onflow.org/flow-go-sdk/#transactions).

##### Request Body schema: application/jsonrequired

The transaction to submit.

| scriptrequired | string <base64>   Base64 encoded content of the Cadence script. |
| --- | --- |
| argumentsrequired | Array of strings <base64> [ items <base64 > ]  A list of arguments each encoded as Base64 passed in the [JSON-Cadence interchange format](https://docs.onflow.org/cadence/json-cadence-spec/). |
| reference\_block\_idrequired | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  A 32-byte unique identifier for an entity. |
| gas\_limitrequired | string <uint64>   The limit on the amount of computation a transaction is allowed to preform. |
| payerrequired | string <hexadecimal>  (Address) [a-fA-F0-9]{16}  The 8-byte address of an account. |
| proposal\_keyrequired | object (ProposalKey) |
| authorizersrequired | Array of strings <hexadecimal>  (Address) [[a-fA-F0-9]{16}] |
| payload\_signaturesrequired | Array of objects (TransactionSignature)   A list of Base64 encoded signatures. |
| envelope\_signaturesrequired | Array of objects (TransactionSignature)   A list of Base64 encoded signatures. |

### Responses

**201** 

Created

**400** 

Bad Request

**500** 

Internal Server Error

post/transactions

Flow Canary

https://rest-canary.onflow.org/v1/transactions

Flow Testnet

https://rest-testnet.onflow.org/v1/transactions

Flow Mainnet

https://rest-mainnet.onflow.org/v1/transactions
### Request samples

* Payload

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "script": "string",
* "arguments": [
  + "string"],
* "reference_block_id": "string",
* "gas_limit": "string",
* "payer": "string",
* "proposal_key": {
  + "address": "string",
  + "key_index": "string",
  + "sequence_number": "string"},
* "authorizers": [
  + "string"],
* "payload_signatures": [
  + {
    - "address": "string",
    - "key_index": "string",
    - "signature": "string"}],
* "envelope_signatures": [
  + {
    - "address": "string",
    - "key_index": "string",
    - "signature": "string"}]

}`
### Response samples

* 201
* 400
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "id": "string",
* "script": "string",
* "arguments": [
  + "string"],
* "reference_block_id": "string",
* "gas_limit": "string",
* "payer": "string",
* "proposal_key": {
  + "address": "string",
  + "key_index": "string",
  + "sequence_number": "string"},
* "authorizers": [
  + "string"],
* "payload_signatures": [
  + {
    - "address": "string",
    - "key_index": "string",
    - "signature": "string"}],
* "envelope_signatures": [
  + {
    - "address": "string",
    - "key_index": "string",
    - "signature": "string"}],
* "result": {
  + "block_id": "string",
  + "collection_id": "string",
  + "execution": "Pending",
  + "status": "Pending",
  + "status_code": 0,
  + "error_message": "string",
  + "computation_used": "string",
  + "events": [
    - {
      * "type": "string",
      * "transaction_id": "string",
      * "transaction_index": "string",
      * "event_index": "string",
      * "payload": "string"}],
  + "_links": {
    - "_self": "string"}},
* "_expandable": {
  + "result": "<http://example.com>"},
* "_links": {
  + "_self": "string"}

}`
## Collections

## Gets a Collection by ID

Get a collection by provided collection ID.

##### path Parameters

| idrequired | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  The collection ID. |
| --- | --- |

##### query Parameters

| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| --- | --- |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/collections/{id}

Flow Canary

https://rest-canary.onflow.org/v1/collections/{id}

Flow Testnet

https://rest-testnet.onflow.org/v1/collections/{id}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/collections/{id}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "id": "string",
* "transactions": [
  + {
    - "id": "string",
    - "script": "string",
    - "arguments": [
      * "string"],
    - "reference_block_id": "string",
    - "gas_limit": "string",
    - "payer": "string",
    - "proposal_key": {
      * "address": "string",
      * "key_index": "string",
      * "sequence_number": "string"},
    - "authorizers": [
      * "string"],
    - "payload_signatures": [
      * {
        + "address": "string",
        + "key_index": "string",
        + "signature": "string"}],
    - "envelope_signatures": [
      * {
        + "address": "string",
        + "key_index": "string",
        + "signature": "string"}],
    - "result": {
      * "block_id": "string",
      * "collection_id": "string",
      * "execution": "Pending",
      * "status": "Pending",
      * "status_code": 0,
      * "error_message": "string",
      * "computation_used": "string",
      * "events": [
        + {
          - "type": "string",
          - "transaction_id": "string",
          - "transaction_index": "string",
          - "event_index": "string",
          - "payload": "string"}],
      * "_links": {
        + "_self": "string"}},
    - "_expandable": {
      * "result": "<http://example.com>"},
    - "_links": {
      * "_self": "string"}}],
* "_expandable": {
  + "transactions": [
    - "<http://example.com>"]},
* "_links": {
  + "_self": "string"}

}`
## Execution Results

## Get Execution Results by Block ID

Get execution result by provided block ID or multiple block IDs provided as comma-seperated list.

##### query Parameters

| block\_idrequired | Array of strings <hexadecimal>  (Identifier)   non-empty  unique [[a-fA-F0-9]{64}]  Single ID or comma-separated list of block IDs. |
| --- | --- |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/execution\_results

Flow Canary

https://rest-canary.onflow.org/v1/execution\_results

Flow Testnet

https://rest-testnet.onflow.org/v1/execution\_results

Flow Mainnet

https://rest-mainnet.onflow.org/v1/execution\_results
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `[

* {
  + "id": "string",
  + "block_id": "string",
  + "events": [
    - {
      * "type": "string",
      * "transaction_id": "string",
      * "transaction_index": "string",
      * "event_index": "string",
      * "payload": "string"}],
  + "chunks": [
    - {
      * "block_id": "string",
      * "collection_index": "string",
      * "start_state": "string",
      * "end_state": "string",
      * "event_collection": "string",
      * "index": "string",
      * "number_of_transactions": "string",
      * "total_computation_used": "string"}],
  + "previous_result_id": "string",
  + "_links": {
    - "_self": "string"}}

]`
## Get Execution Result by ID

Get execution result by provided execution result ID.

##### path Parameters

| idrequired | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  The ID of the execution result. |
| --- | --- |

##### query Parameters

| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |
| --- | --- |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/execution\_results/{id}

Flow Canary

https://rest-canary.onflow.org/v1/execution\_results/{id}

Flow Testnet

https://rest-testnet.onflow.org/v1/execution\_results/{id}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/execution\_results/{id}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "id": "string",
* "block_id": "string",
* "events": [
  + {
    - "type": "string",
    - "transaction_id": "string",
    - "transaction_index": "string",
    - "event_index": "string",
    - "payload": "string"}],
* "chunks": [
  + {
    - "block_id": "string",
    - "collection_index": "string",
    - "start_state": "string",
    - "end_state": "string",
    - "event_collection": "string",
    - "index": "string",
    - "number_of_transactions": "string",
    - "total_computation_used": "string"}],
* "previous_result_id": "string",
* "_links": {
  + "_self": "string"}

}`
## Accounts

## Get an Account By Address

Get an account data by provided address in latest "sealed" block or by provided block height.

##### path Parameters

| addressrequired | string <hexadecimal>  (Address) [a-fA-F0-9]{16}  The address of the account. |
| --- | --- |

##### query Parameters

| block\_height | string or string (BlockHeight)   The block height to query for the account details at the "sealed" is used by default. |
| --- | --- |
| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/accounts/{address}

Flow Canary

https://rest-canary.onflow.org/v1/accounts/{address}

Flow Testnet

https://rest-testnet.onflow.org/v1/accounts/{address}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/accounts/{address}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "address": "string",
* "balance": "string",
* "keys": [
  + {
    - "index": "string",
    - "public_key": "string",
    - "signing_algorithm": "BLSBLS12381",
    - "hashing_algorithm": "SHA2_256",
    - "sequence_number": "string",
    - "weight": "string",
    - "revoked": true}],
* "contracts": {
  + "property1": "string",
  + "property2": "string"},
* "_expandable": {
  + "keys": "string",
  + "contracts": "string"},
* "_links": {
  + "_self": "string"}

}`
## Get an individual Account Key By Address and Index

Get an account data by provided address in latest "sealed" block or by provided block height.

##### path Parameters

| addressrequired | string <hexadecimal>  (Address) [a-fA-F0-9]{16}  The address of the account. |
| --- | --- |
| indexrequired | string <uint64>   The index of the account key. |

##### query Parameters

| block\_height | string or string (BlockHeight)   The block height to query for the account details at the "sealed" is used by default. |
| --- | --- |
| expand | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to expand. |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/accounts/{address}/keys/{index}

Flow Canary

https://rest-canary.onflow.org/v1/accounts/{address}/keys/{index}

Flow Testnet

https://rest-testnet.onflow.org/v1/accounts/{address}/keys/{index}

Flow Mainnet

https://rest-mainnet.onflow.org/v1/accounts/{address}/keys/{index}
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy`{

* "index": "string",
* "public_key": "string",
* "signing_algorithm": "BLSBLS12381",
* "hashing_algorithm": "SHA2_256",
* "sequence_number": "string",
* "weight": "string",
* "revoked": true

}`
## Scripts

## Execute a Cadence Script

Executes a read-only Cadence script against the execution state at the given block height or ID. If block height or ID is not specified, then the script is executed at the latest sealed block height.

##### query Parameters

| block\_id | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  The ID of the block to execute the script against. For a specific block height, use `block_height` instead. |
| --- | --- |
| block\_height | string or string (BlockHeight)   The height of the block to execute the script against. This parameter is incompatible with `block_id`. |

##### Request Body schema: application/jsonrequired

The script to execute.

| script | string <base64>   Base64 encoded content of the Cadence script. |
| --- | --- |
| arguments | Array of strings <byte> [ items <byte > ]  An list of arguments each encoded as Base64 passed in the [JSON-Cadence interchange format](https://docs.onflow.org/cadence/json-cadence-spec/). |

### Responses

**200** 

OK

**400** 

Bad Request

**500** 

Internal Server Error

post/scripts

Flow Canary

https://rest-canary.onflow.org/v1/scripts

Flow Testnet

https://rest-testnet.onflow.org/v1/scripts

Flow Mainnet

https://rest-mainnet.onflow.org/v1/scripts
### Request samples

* Payload

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "script": "string",
* "arguments": [
  + "string"]

}`
### Response samples

* 200
* 400
* 500

Content typeapplication/jsonCopy`{

* "value": "string"

}`
## Events

## Get Events

Query on-chain events by their name in the specified blocks heights or block IDs.

##### query Parameters

| typerequired | string (EventType)   The event type is [identifier of the event as defined here](https://docs.onflow.org/core-contracts/flow-token/#events). |
| --- | --- |
| start\_height | string or string (BlockHeight)   The start height of the block range for events. Must be used together with `end_height`. This parameter is incompatible with `block_ids`. |
| end\_height | string or string (BlockHeight)   The end height of the block range for events. Must be used together with `start_height`. This parameter is incompatible with `block_ids`. |
| block\_ids | Array of strings <hexadecimal>  (Identifier)   [ 1 .. 50 ] items  unique [[a-fA-F0-9]{64}]  List of block IDs. Either provide this parameter or both height parameters. This parameter is incompatible with heights parameters. |
| select | Array of strings  non-empty  unique   A comma-separated list indicating which properties of the content to return. |

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/events

Flow Canary

https://rest-canary.onflow.org/v1/events

Flow Testnet

https://rest-testnet.onflow.org/v1/events

Flow Mainnet

https://rest-mainnet.onflow.org/v1/events
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "block_id": "string",
* "block_height": "string",
* "block_timestamp": "2019-08-24T14:15:22Z",
* "events": [
  + {
    - "type": "string",
    - "transaction_id": "string",
    - "transaction_index": "string",
    - "event_index": "string",
    - "payload": "string"}],
* "_links": {
  + "_self": "string"}

}`
## Network

## Get Network Parameters

Get network-wide parameters of the blockchain

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/network/parameters

Flow Canary

https://rest-canary.onflow.org/v1/network/parameters

Flow Testnet

https://rest-testnet.onflow.org/v1/network/parameters

Flow Mainnet

https://rest-mainnet.onflow.org/v1/network/parameters
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy`{

* "chain_id": "string"

}`
## NodeVersionInfo

## Get Node Version Information

Get node version information, such as semver, commit, sporkID and protocol version.

### Responses

**200** 

OK

**400** 

Bad Request

**404** 

Not Found

**500** 

Internal Server Error

get/node\_version\_info

Flow Canary

https://rest-canary.onflow.org/v1/node\_version\_info

Flow Testnet

https://rest-testnet.onflow.org/v1/node\_version\_info

Flow Mainnet

https://rest-mainnet.onflow.org/v1/node\_version\_info
### Response samples

* 200
* 400
* 404
* 500

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "semver": "string",
* "commit": "string",
* "spork_id": "string",
* "protocol_version": "string",
* "spork_root_block_height": "string",
* "node_root_block_height": "string",
* "compatible_range": {
  + "start_height": "string",
  + "end_height": "string"}

}`
## Subscribe events

## Subscribe events

IMPORTANT NOTE: This is a WebSocket connection, so the `ws://` or `wss://` schema should be used to subscribe to this endpoint.

This endpoint streams on-chain events for all blocks starting at the requested start block, up until the latest available block. Once the latest block is reached, the stream will remain open, and responses will be sent for each new block as it becomes available.

##### query Parameters

| start\_height | string or string (BlockHeight)   The block height of the events being streamed. Either provide this parameter or `start_block_id` parameter. This parameter is incompatible with `start_block_id` parameter. |
| --- | --- |
| start\_block\_id | string <hexadecimal>  (Identifier) [a-fA-F0-9]{64}  The block id of the events being streamed. Either provide this parameter or `start_height` parameter. This parameter is incompatible with `start_height` parameter. |
| heartbeat\_interval | string <uint64>   Interval in block heights at which the server should return a heartbeat message to the client. |
| event\_types | Array of strings (EventType)   non-empty  unique   A comma-separated list of events type to include. |
| addresses | Array of strings  non-empty  unique   A comma-separated list of addresses who's events should be included. |
| contracts | Array of strings  non-empty  unique   A comma-separated list of contracts who's events should be included. |

### Responses

**200** 

OK

**400** 

Bad Request

As OpenAPI does not support WebSocket description, the error code (1003) is actually returned in a close message instead of (400).

**408** 

Server Timeout

As OpenAPI does not support WebSocket description, this error code (1001) is actually returned in a close message instead of (408).

**500** 

Internal Server Error

As OpenAPI does not support WebSocket description, this error code (1011) is actually returned in a close message instead of (500).

**503** 

Service Unavailable

As OpenAPI does not support WebSocket description, this error code (1013) is actually returned in a close message instead of (503).

get/subscribe\_events

Flow Canary

https://rest-canary.onflow.org/v1/subscribe\_events

Flow Testnet

https://rest-testnet.onflow.org/v1/subscribe\_events

Flow Mainnet

https://rest-mainnet.onflow.org/v1/subscribe\_events
### Response samples

* 200
* 400
* 408
* 500
* 503

Content typeapplication/jsonCopy Expand all  Collapse all `{

* "BlockId": "string",
* "Height": "string",
* "Events": [
  + {
    - "type": "string",
    - "transaction_id": "string",
    - "transaction_index": "string",
    - "event_index": "string",
    - "payload": "string"}]

}`Documentation

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

