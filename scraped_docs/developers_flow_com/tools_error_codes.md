# Source: https://developers.flow.com/tools/error-codes




Error Codes | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* Error Codes
On this page
# Error Codes

List of error codes returned from failing transactions and scripts. The error code has an accompanied error message that usually gives more clarification. This list is meant to give more information and helpful hints.
[Code file](https://github.com/onflow/flow-go/blob/master/fvm/errors/codes.go)

### 1006[​](#1006 "Direct link to 1006")

**ErrCodeInvalidProposalSignatureError**

Example:
`...`

### 1007[​](#1007 "Direct link to 1007")

**ErrCodeInvalidProposalSeqNumberError**

Example:
`[Error Code: 1007] invalid proposal key: public key 0 on account xxx has sequence number xxx, but given xxx`

### 1008[​](#1008 "Direct link to 1008")

**ErrCodeInvalidPayloadSignatureError**

Example:
`[Error Code: 1008] invalid payload signature: public key 0 on account xxx does not have a valid signature: signature is not valid`

### 1009[​](#1009 "Direct link to 1009")

**ErrCodeInvalidEnvelopeSignatureError**

Example:
`[Error Code: 1009] invalid envelope key: public key 1 on account xxx does not have a valid signature: signature is not valid`

### 1051[​](#1051 "Direct link to 1051")

**ErrCodeValueError**

Example:
`[Error Code: 1051] invalid value (xxx): invalid encoded public key value: rlp: expected input list for flow.runtimeAccountPublicKeyWrapper...`

### 1052[​](#1052 "Direct link to 1052")

**ErrCodeInvalidArgumentError**

Example:
`[Error Code: 1052] transaction arguments are invalid: (argument is not json decodable: failed to decode value: runtime error: slice bounds out of range [:2] with length 0)`

### 1053[​](#1053 "Direct link to 1053")

**ErrCodeInvalidAddressError**

Example:
`...`

### 1054[​](#1054 "Direct link to 1054")

**ErrCodeInvalidLocationError**

Example:
`[Error Code: 1054] location (../contracts/FungibleToken.cdc) is not a valid location: expecting an AddressLocation, but other location types are passed ../contracts/FungibleToken.cdc`

### 1055[​](#1055 "Direct link to 1055")

**ErrCodeAccountAuthorizationError**

Example:
`[Error Code: 1055] authorization failed for account e85d442d61a611d8: payer account does not have sufficient signatures (1 < 1000)`

### 1056[​](#1056 "Direct link to 1056")

**ErrCodeOperationAuthorizationError**

Example:
`[Error Code: 1056] (RemoveContract) is not authorized: removing contracts requires authorization from specific accounts goroutine 5688834491 [running]:`

### 1057[​](#1057 "Direct link to 1057")

**ErrCodeOperationNotSupportedError**

Example:
`...`

### 1101[​](#1101 "Direct link to 1101")

**ErrCodeCadenceRunTimeError**

Example:
`[Error Code: 1101] cadence runtime error Execution failed: error: pre-condition failed: Amount withdrawn must be less than or equal than the balance of the Vault`

### 1103[​](#1103 "Direct link to 1103")

**ErrCodeStorageCapacityExceeded**

Example:
`[Error Code: 1103] The account with address (xxx) uses 96559611 bytes of storage which is over its capacity (96554500 bytes). Capacity can be increased by adding FLOW tokens to the account.`

For more information refer to [Fees](/build/basics/fees#maximum-available-balance)

### 1105[​](#1105 "Direct link to 1105")

**ErrCodeEventLimitExceededError**

Example:
`[Error Code: 1105] total event byte size (256200) exceeds limit (256000)`

### 1106[​](#1106 "Direct link to 1106")

**ErrCodeLedgerInteractionLimitExceededError**

Example:
`[Error Code: 1106] max interaction with storage has exceeded the limit (used: 20276498 bytes, limit 20000000 bytes)`

### 1107[​](#1107 "Direct link to 1107")

**ErrCodeStateKeySizeLimitError**

Example:
`...`

### 1108[​](#1108 "Direct link to 1108")

**ErrCodeStateValueSizeLimitError**

Example:
`...`

### 1109[​](#1109 "Direct link to 1109")

**ErrCodeTransactionFeeDeductionFailedError**

Example:
`[Error Code: 1109] failed to deduct 0 transaction fees from 14af75b8c487333c: Execution failed: f919ee77447b7497.FlowFees:97:24`

### 1110[​](#1110 "Direct link to 1110")

**ErrCodeComputationLimitExceededError**

Example:
`[Error Code: 1110] computation exceeds limit (100)`

### 1111[​](#1111 "Direct link to 1111")

**ErrCodeMemoryLimitExceededError**

Example:
`...`

### 1112[​](#1112 "Direct link to 1112")

**ErrCodeCouldNotDecodeExecutionParameterFromState**

Example:
`...`

### 1113[​](#1113 "Direct link to 1113")

**ErrCodeScriptExecutionTimedOutError**

Example:
`...`

### 1114[​](#1114 "Direct link to 1114")

**ErrCodeScriptExecutionCancelledError**

Example:
`...`

### 1115[​](#1115 "Direct link to 1115")

**ErrCodeEventEncodingError**

Example:
`...`

### 1116[​](#1116 "Direct link to 1116")

**ErrCodeInvalidInternalStateAccessError**

Example:
`...`

### 1118[​](#1118 "Direct link to 1118")

**ErrCodeInsufficientPayerBalance**

Example:
 `[Error Code: 1118] payer ... has insufficient balance to attempt transaction execution (required balance: 0.00100000)`

### 1201[​](#1201 "Direct link to 1201")

**ErrCodeAccountNotFoundError**

Example:
`[Error Code: 1201] account not found for address xxx`

### 1202[​](#1202 "Direct link to 1202")

**ErrCodeAccountPublicKeyNotFoundError**

Example:
`[Error Code: 1202] account public key not found for address xxx and key index 3`

### 1203[​](#1203 "Direct link to 1203")

**ErrCodeAccountAlreadyExistsError**

Example:
`...`

### 1204[​](#1204 "Direct link to 1204")

**ErrCodeFrozenAccountError**

Example:
`...`

### 1206[​](#1206 "Direct link to 1206")

**ErrCodeAccountPublicKeyLimitError**

Example:
`...`

### 1251[​](#1251 "Direct link to 1251")

**ErrCodeContractNotFoundError**

Example:
`...`

### 2000[​](#2000 "Direct link to 2000")

**FailureCodeUnknownFailure**

Example:
`...`

### 2001[​](#2001 "Direct link to 2001")

**FailureCodeEncodingFailure**

Example:
`...`

### 2002[​](#2002 "Direct link to 2002")

**FailureCodeLedgerFailure**

Example:
`...`

### 2003[​](#2003 "Direct link to 2003")

**FailureCodeStateMergeFailure**

Example:
`...`

### 2004[​](#2004 "Direct link to 2004")

**FailureCodeBlockFinderFailure**

Example:
`...`

### 2006[​](#2006 "Direct link to 2006")

**FailureCodeParseRestrictedModeInvalidAccessFailure**

Example:
`...`

### 2007[​](#2007 "Direct link to 2007")

**FailureCodePayerBalanceCheckFailure**

Example:
`...`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/error-codes.md)Last updated on **Jan 7, 2025** by **Chase Fleming**[PreviousTools](/tools)[NextFlow CLI](/tools/flow-cli)
###### Rate this page

😞😐😊

* [1006](#1006)
* [1007](#1007)
* [1008](#1008)
* [1009](#1009)
* [1051](#1051)
* [1052](#1052)
* [1053](#1053)
* [1054](#1054)
* [1055](#1055)
* [1056](#1056)
* [1057](#1057)
* [1101](#1101)
* [1103](#1103)
* [1105](#1105)
* [1106](#1106)
* [1107](#1107)
* [1108](#1108)
* [1109](#1109)
* [1110](#1110)
* [1111](#1111)
* [1112](#1112)
* [1113](#1113)
* [1114](#1114)
* [1115](#1115)
* [1116](#1116)
* [1118](#1118)
* [1201](#1201)
* [1202](#1202)
* [1203](#1203)
* [1204](#1204)
* [1206](#1206)
* [1251](#1251)
* [2000](#2000)
* [2001](#2001)
* [2002](#2002)
* [2003](#2003)
* [2004](#2004)
* [2006](#2006)
* [2007](#2007)
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

