# Source: https://developers.flow.com/evm/cadence/interacting-with-coa




Interacting with COAs from Cadence | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using EVM](/evm/using)
* [Networks](/evm/networks)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Data Indexers](/evm/data-indexers)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)
* [Clients](/evm/clients/ethers)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)
  + [Interacting with COAs](/evm/cadence/interacting-with-coa)
  + [Direct Calls to Flow EVM](/evm/cadence/direct-calls)
  + [Batched EVM Transactions](/evm/cadence/batched-evm-transactions)
  + [Cross-VM Bridge](/evm/cadence/vm-bridge)


* Using EVM with Cadence
* Interacting with COAs
On this page
# Interacting with COAs from Cadence

[Cadence Owned Accounts (COAs)](/evm/accounts#cadence-owned-accounts) are EVM accounts owned by a Cadence resource and are used to interact with Flow EVM from Cadence.

COAs expose two interfaces for interaction: one on the Cadence side and one on the EVM side. In this guide, we will focus on how to interact with COAs with Cadence.

In this guide we will walk through some basic examples creating and interacting with a COA in Cadence. Your specific usage of the COA resource will depend on your own application's requirements (e.g. the COA resource may not live directly in `/storage/evm` as in these examples, but may instead be a part of a more complex resource structure).

## COA Interface[​](#coa-interface "Direct link to COA Interface")

To begin, we can take a look at a simplified version of the `EVM` contract, highlighting parts specific to COAs.

You can learn more about the `EVM` contract [here](/build/core-contracts/evm) and the full contract code can be found on [GitHub](https://github.com/onflow/flow-go/tree/master/fvm/evm/stdlib/contract.cdc).

 `_56access(all)_56contract EVM {_56 //..._56 access(all)_56 resource CadenceOwnedAccount: Addressable {_56 /// The EVM address of the cadence owned account_56 /// -> could be used to query balance, code, nonce, etc._56 access(all)_56 view fun address(): EVM.EVMAddress_56_56 /// Get balance of the cadence owned account_56 /// This balance_56 access(all)_56 view fun balance(): EVM.Balance_56_56 /// Deposits the given vault into the cadence owned account's balance_56 access(all)_56 fun deposit(from: @FlowToken.Vault)_56_56 /// The EVM address of the cadence owned account behind an entitlement, acting as proof of access_56 access(EVM.Owner | EVM.Validate)_56 view fun protectedAddress(): EVM.EVMAddress_56_56 /// Withdraws the balance from the cadence owned account's balance_56 /// Note that amounts smaller than 10nF (10e-8) can't be withdrawn_56 /// given that Flow Token Vaults use UFix64s to store balances._56 /// If the given balance conversion to UFix64 results in_56 /// rounding error, this function would fail._56 access(EVM.Owner | EVM.Withdraw)_56 fun withdraw(balance: EVM.Balance): @FlowToken.Vault_56_56 /// Deploys a contract to the EVM environment._56 /// Returns the address of the newly deployed contract_56 access(EVM.Owner | EVM.Deploy)_56 fun deploy(_56 code: [UInt8],_56 gasLimit: UInt64,_56 value: Balance_56 ): EVM.EVMAddress_56_56 /// Calls a function with the given data._56 /// The execution is limited by the given amount of gas_56 access(EVM.Owner | EVM.Call)_56 fun call(_56 to: EVMAddress,_56 data: [UInt8],_56 gasLimit: UInt64,_56 value: Balance_56 ): EVM.Result_56 }_56_56 // Create a new CadenceOwnedAccount resource_56 access(all)_56 fun createCadenceOwnedAccount(): @EVM.CadenceOwnedAccount_56 // ..._56}`
## Importing the EVM Contract[​](#importing-the-evm-contract "Direct link to Importing the EVM Contract")

The `CadenceOwnedAccount` resource is a part of the `EVM` system contract, so to use any of these functions, you will need to begin by importing the `EVM` contract into your Cadence code.

To import the `EVM` contract into your Cadence code using the simple import syntax, you can use the following format (learn more about configuring contracts in `flow.json` [here](/tools/flow-cli/flow.json/configuration#contracts)):

 `_10// This assumes you are working in the in the Flow CLI, FCL, or another tool that supports this syntax_10// The contract address should be configured in your project's `flow.json` file_10import "EVM"_10// ...`

However, if you wish to use manual address imports instead, you can use the following format:

 `_10// Must use the correct address based on the network you are interacting with_10import EVM from 0x1234_10// ...`

To find the deployment addresses of the `EVM` contract, you can refer to the [EVM contract documentation](/build/core-contracts/evm).

## Creating a COA[​](#creating-a-coa "Direct link to Creating a COA")

To create a COA, we can use the `createCadenceOwnedAccount` function from the `EVM` contract. This function takes no arguments and returns a new `CadenceOwnedAccount` resource which represents this newly created EVM account.

For example, we can create this COA in a transaction, saving it to the user's storage and publishing a public capability to its reference:

 `_17import "EVM"_17_17// Note that this is a simplified example & will not handle cases where the COA already exists_17transaction() {_17 prepare(signer: auth(SaveValue, IssueStorageCapabilityController, PublishCapability) &Account) {_17 let storagePath = /storage/evm_17 let publicPath = /public/evm_17_17 // Create account & save to storage_17 let coa: @EVM.CadenceOwnedAccount <- EVM.createCadenceOwnedAccount()_17 signer.storage.save(<-coa, to: storagePath)_17_17 // Publish a public capability to the COA_17 let cap = signer.capabilities.storage.issue<&EVM.CadenceOwnedAccount>(storagePath)_17 signer.capabilities.publish(cap, at: publicPath)_17 }_17}`
## Getting the EVM Address of a COA[​](#getting-the-evm-address-of-a-coa "Direct link to Getting the EVM Address of a COA")

To get the EVM address of a COA, you can use the `address` function from the `EVM` contract. This function returns the EVM address of the COA as an `EVM.Address` struct. This struct is used to represent addresses within Flow EVM and can also be used to query the balance, code, nonce, etc. of an account.

For our example, we could query the address of the COA we just created with the following script:

 `_15import "EVM"_15_15access(all)_15fun main(address: Address): EVM.EVMAddress {_15 // Get the desired Flow account holding the COA in storage_15 let account = getAuthAccount<auth(Storage) &Account>(address)_15_15 // Borrow a reference to the COA from the storage location we saved it to_15 let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(_15 from: /storage/evm_15 ) ?? panic("Could not borrow reference to the COA")_15_15 // Return the EVM address of the COA_15 return coa.address()_15}`

If you'd prefer the hex representation of the address, you instead return using the `EVMAddress.toString()` function:

 `_10return coa.address().toString()`

The above will return the EVM address as a string; however note that Cadence does not prefix hex strings with `0x`.

## Getting the Flow Balance of a COA[​](#getting-the-flow-balance-of-a-coa "Direct link to Getting the Flow Balance of a COA")

Like any other Flow EVM or Cadence account, COAs possess a balance of FLOW tokens. To get the current balance of our COA, we can use the COA's `balance` function. It will return a `EVM.Balance` struct for the account - these are used to represent balances within Flow EVM.

This script will query the current balance of our newly created COA:

 `_15import "EVM"_15_15access(all)_15fun main(address: Address): EVM.Balance {_15 // Get the desired Flow account holding the COA in storage_15 let account = getAuthAccount<auth(Storage) &Account>(address)_15_15 // Borrow a reference to the COA from the storage location we saved it to_15 let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(_15 from: /storage/evm_15 ) ?? panic("Could not borrow reference to the COA")_15_15 // Get the current balance of this COA_15 return coa.balance()_15}`

You can also easily get the `UFix64` FLOW balance of any EVM address with this script:

 `_10import "EVM"_10_10access(all)_10fun main(addressHex: String): UFix64 {_10 let addr = EVM.addressFromString(addressHex)_10 return addr.balance().inFLOW()_10}`

The above script is helpful if you already know the COA address and can provide the hex representation directly.

## Depositing and Withdrawing Flow Tokens[​](#depositing-and-withdrawing-flow-tokens "Direct link to Depositing and Withdrawing Flow Tokens")

Tokens can be seamlessly transferred between the Flow EVM and Cadence environment using the `deposit` and `withdraw` functions provided by the COA resource. Anybody with a valid reference to a COA may deposit Flow tokens into a it, however only someone with the `Owner` or `Withdraw` entitlements can withdraw tokens.

### Depositing Flow Tokens[​](#depositing-flow-tokens "Direct link to Depositing Flow Tokens")

The `deposit` function takes a `FlowToken.Vault` resource as an argument, representing the tokens to deposit. It will transfer the tokens from the vault into the COA's balance.

This transaction will withdraw Flow tokens from a user's Cadence vault and deposit them into their COA:

 `_26import "EVM"_26import "FungibleToken"_26import "FlowToken"_26_26transaction(amount: UFix64) {_26 let coa: &EVM.CadenceOwnedAccount_26 let sentVault: @FlowToken.Vault_26_26 prepare(signer: auth(BorrowValue) &Account) {_26 // Borrow the public capability to the COA from the desired account_26 // This script could be modified to deposit into any account with a `EVM.CadenceOwnedAccount` capability_26 self.coa = signer.capabilities.borrow<&EVM.CadenceOwnedAccount>(/public/evm)_26 ?? panic("Could not borrow reference to the COA")_26_26 // Withdraw the balance from the COA, we will use this later to deposit into the receiving account_26 let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(_26 from: /storage/flowTokenVault_26 ) ?? panic("Could not borrow reference to the owner's Vault")_26 self.sentVault <- vaultRef.withdraw(amount: amount) as! @FlowToken.Vault_26 }_26_26 execute {_26 // Deposit the withdrawn tokens into the COA_26 self.coa.deposit(from: <-self.sentVault)_26 }_26}`
info

This is a basic example which only transfers tokens between a single user's COA & Flow account. It can be easily modified to transfer these tokens between any arbitrary accounts.

You can also deposit tokens directly into other types of EVM accounts using the `EVM.EVMAddress.deposit` function. See the [EVM contract documentation](/build/core-contracts/evm) for more information.

### Withdrawing Flow Tokens[​](#withdrawing-flow-tokens "Direct link to Withdrawing Flow Tokens")

The `withdraw` function takes a `EVM.Balance` struct as an argument, representing the amount of Flow tokens to withdraw, and returns a `FlowToken.Vault` resource with the withdrawn tokens.

We can run the following transaction to withdraw Flow tokens from a user's COA and deposit them into their Flow vault:

 `_31import "EVM"_31import "FungibleToken"_31import "FlowToken"_31_31transaction(amount: UFix64) {_31 let sentVault: @FlowToken.Vault_31 let receiver: &{FungibleToken.Receiver}_31_31 prepare(signer: auth(BorrowValue) &Account) {_31 // Borrow a reference to the COA from the storage location we saved it to with the `EVM.Withdraw` entitlement_31 let coa = signer.storage.borrow<auth(EVM.Withdraw) &EVM.CadenceOwnedAccount>(_31 from: /storage/evm_31 ) ?? panic("Could not borrow reference to the COA")_31_31 // We must create a `EVM.Balance` struct to represent the amount of Flow tokens to withdraw_31 let withdrawBalance = EVM.Balance(attoflow: 0)_31 withdrawBalance.setFLOW(flow: amount)_31_31 // Withdraw the balance from the COA, we will use this later to deposit into the receiving account_31 self.sentVault <- coa.withdraw(balance: withdrawBalance) as! @FlowToken.Vault_31_31 // Borrow the public capability to the receiving account (in this case the signer's own Vault)_31 // This script could be modified to deposit into any account with a `FungibleToken.Receiver` capability_31 self.receiver = signer.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!_31 }_31_31 execute {_31 // Deposit the withdrawn tokens into the receiving vault_31 self.receiver.deposit(from: <-self.sentVault)_31 }_31}`
info

This is a basic example which only transfers tokens between a single user's COA & Flow account. It can be easily modified to transfer these tokens between any arbitrary accounts.

## Direct Calls to Flow EVM[​](#direct-calls-to-flow-evm "Direct link to Direct Calls to Flow EVM")

To interact with smart contracts on the EVM, you can use the `call` function provided by the COA resource. This function takes the EVM address of the contract you want to call, the data you want to send, the gas limit, and the value you want to send. It will return a `EVM.Result` struct with the result of the call - you will need to handle this result in your Cadence code.

This transaction will use the signer's COA to call a contract method with the defined signature and args at a given EVM address, executing with the provided gas limit and value:

 `_42import "EVM"_42_42transaction(evmContractHex: String, signature: String, args: [AnyStruct], gasLimit: UInt64, flowValue: UFix64) {_42 let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount_42_42 prepare(signer: auth(BorrowValue) &Account) {_42 // Borrow an entitled reference to the COA from the storage location we saved it to_42 self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(_42 from: /storage/evm_42 ) ?? panic("Could not borrow reference to the COA")_42 }_42_42 execute {_42 // Deserialize the EVM address from the hex string_42 let contractAddress = EVM.addressFromString(evmContractHex)_42 // Construct the calldata from the signature and arguments_42 let calldata = EVM.encodeABIWithSignature(_42 signature,_42 args_42 )_42 // Define the value as EVM.Balance struct_42 let value = EVM.Balance(attoflow: 0)_42 value.setFLOW(flow: flowValue)_42 // Call the contract at the given EVM address with the given data, gas limit, and value_42 // These values could be configured through the transaction arguments or other means_42 // however, for simplicity, we will hardcode them here_42 let result: EVM.Result = self.coa.call(_42 to: contractAddress,_42 data: calldata,_42 gasLimit: gasLimit,_42 value: value_42 )_42_42 // Revert the transaction if the call was not successful_42 // Note: a failing EVM call will not automatically revert the Cadence transaction_42 // and it is up to the developer to use this result however it suits their application_42 assert(_42 result.status == EVM.Status.successful,_42 message: "EVM call failed"_42 )_42 }_42}`
info

Notice that the calldata is encoded in the scope of the transaction. While developers can encode the calldata outside the scope of the transaction and pass the encoded data as an argument, doing so compromises the human-readability of Cadence transactions.

It's encouraged to either define transactions for each COA call and encoded the hardcoded EVM signature and arguments, or to pass in the human-readable arguments and signature and encode the calldata within the transaction. This ensures a more interpretable and therefore transparent transaction.

### Deploying a Contract to Flow EVM[​](#deploying-a-contract-to-flow-evm "Direct link to Deploying a Contract to Flow EVM")

To deploy a contract to the EVM, you can use the `deploy` function provided by the COA resource. This function takes the contract code, gas limit, and value you want to send. It will return the EVM address of the newly deployed contract.

This transaction will deploy a contract with the given code using the signer's COA:

 `_21import "EVM"_21_21transaction(bytecode: String) {_21 let coa: auth(EVM.Deploy) &EVM.CadenceOwnedAccount_21_21 prepare(signer: auth(BorrowValue) &Account) {_21 // Borrow an entitled reference to the COA from the storage location we saved it to_21 self.coa = signer.storage.borrow<auth(EVM.Deploy) &EVM.CadenceOwnedAccount>(_21 from: /storage/evm_21 ) ?? panic("Could not borrow reference to the COA")_21 }_21_21 execute {_21 // Deploy the contract with the given compiled bytecode, gas limit, and value_21 self.coa.deploy(_21 code: bytecode.decodeHex(),_21 gasLimit: 15_000_000, // can be adjusted as needed, hard coded here for simplicity_21 value: EVM.Balance(attoflow: 0)_21 )_21 }_21}`
## More Information[​](#more-information "Direct link to More Information")

For more information about Cadence Owned Accounts, see [Flow EVM Accounts](/evm/accounts).

Other useful snippets for interacting with COAs can be found [here](https://fw-internal-doc.gitbook.io/evm).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/cadence/interacting-with-coa.md)Last updated on **Jan 23, 2025** by **Brian Doyle**[PreviousWeb3.js](/evm/clients/web3-js)[NextDirect Calls to Flow EVM](/evm/cadence/direct-calls)
###### Rate this page

😞😐😊

* [COA Interface](#coa-interface)
* [Importing the EVM Contract](#importing-the-evm-contract)
* [Creating a COA](#creating-a-coa)
* [Getting the EVM Address of a COA](#getting-the-evm-address-of-a-coa)
* [Getting the Flow Balance of a COA](#getting-the-flow-balance-of-a-coa)
* [Depositing and Withdrawing Flow Tokens](#depositing-and-withdrawing-flow-tokens)
  + [Depositing Flow Tokens](#depositing-flow-tokens)
  + [Withdrawing Flow Tokens](#withdrawing-flow-tokens)
* [Direct Calls to Flow EVM](#direct-calls-to-flow-evm)
  + [Deploying a Contract to Flow EVM](#deploying-a-contract-to-flow-evm)
* [More Information](#more-information)
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

