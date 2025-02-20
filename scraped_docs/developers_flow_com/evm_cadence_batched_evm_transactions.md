# Source: https://developers.flow.com/evm/cadence/batched-evm-transactions




Batched EVM Transactions Using Cadence | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
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
* Batched EVM Transactions
On this page
# Batched EVM Transactions Using Cadence

Integrating Cadence into EVM applications on Flow enables developers to leverage the best of both worlds. This guide
demonstrates how to batch EVM transactions using Cadence, allowing applications to embed multiple EVM transactions in a
single Cadence transaction while conditioning final execution on the success of all EVM transactions.

This feature can supercharge your EVM application by unlocking experiences otherwise impossible on traditional EVM
platforms.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to

* Construct a Cadence transaction that executes several EVM transactions such that if any EVM transaction fails, the
  entire set will revert
* Read and write from smart contract functions on [EVM Flowscan](https://evm.flowscan.io/)
* Run a Cadence transaction from the browser using [Flow Runner](https://run.dnz.dev/)
* Install conceptual understanding of Cadence X EVM interactions
* Inspect multiple EVM transactions embedded in a Cadence transaction with [Flowscan](https://www.flowscan.io/) block explorer
* Write code that interacts with the EVM via a CadenceOwnedAccount (COA)

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you dive in, make sure you have the following configured:

* [MetaMask](https://metamask.io/download/) installed in your browser with an active account
* [Flow Wallet extension](https://wallet.flow.com/download) installed in your browser with an active account
* Both wallets funded with Testnet FLOW. See the [Faucet guide](/ecosystem/faucets) for more information.

## Overview[​](#overview "Direct link to Overview")

For the purposes of demonstration, this walkthrough will focus on relatively simple EVM operations in addition to first
creating a [Cadence-controlled EVM account (COA)](/evm/cadence/interacting-with-coa). Specifically, we will:

* Wrap FLOW as WFLOW
* Approve an ERC721 to transfer WFLOW in exchange for an NFT mint
* Mint an ERC721 token - this ERC721 has a 50% chance of failing (using [onchain VRF](/evm/guides/vrf) to determine success)

These operations let us focus on the **core concepts** of this guide:

1. **Batching EVM transactions** using Cadence
2. **Conditioning execution** on the results of those EVM transactions.

However, using these same principles, you'll have the power to address more complex use cases. For instance, replace
wrapping FLOW with a DEX swap. Or instead of minting an ERC721, purchase an NFT listing from a marketplace. Combine
these two and suddenly you can purchase NFTs with any ERC20 token, all in a single Cadence transaction, reverting
everything if a single step fails.

The point is, while a simple use case, this guide will give you the tools to build much more complex and interesting
applications. So let's get started!

## Components[​](#components "Direct link to Components")

As mentioned in the [Overview](#overview), this guide involves three main actions:

* Wrapping FLOW as WFLOW
* Approving an ERC721 to transfer WFLOW in exchange for an NFT mint
* Minting an ERC721 token

Before interacting with these contracts, let's dig bit more into the components of this guide.

### Wrap FLOW as WFLOW[​](#wrap-flow-as-wflow "Direct link to Wrap FLOW as WFLOW")

On Flow EVM, FLOW is the native currency and similar to other EVM platforms, the native currency is not accessible as an
ERC20 token. To interact with ERC20 contracts, you need to wrap FLOW as WFLOW (Wrapped FLOW). This is Flow's equivalent
of WETH on Ethereum.

tip

You can find WFLOW deployed to `0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e` on Flow [Testnet](https://evm-testnet.flowscan.io/token/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e?tab=contract) & [Mainnet](https://evm.flowscan.io/token/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e?tab=contract) and source
code in the [`@onflow/flow-sol-utils` repository](https://github.com/onflow/flow-sol-utils).

### Approve ERC721 Transfer[​](#approve-erc721-transfer "Direct link to Approve ERC721 Transfer")

Our example `MaybeMintERC721` contract accepts WFLOW in exchange for minting an NFT. However, the contract cannot move
WFLOW without your permission. To allow the contract to move your WFLOW, you must approve the contract to transfer
enough of your WFLOW to mint the NFT.

### Mint ERC721 Token[​](#mint-erc721-token "Direct link to Mint ERC721 Token")

Finally, we'll mint an ERC721 token using the `MaybeMintERC721` contract. This contract has a 50% chance of failing,
simulating a real-world scenario where purchasing an NFT might fail - say a listing was purchased before your
transaction was processed.

Importantly, if this transaction fails, we want to revert the entire sequence of transactions. After all, you wrapped
FLOW to WFLOW and approved the ERC721 transfer specifically to mint this NFT. If the mint fails, you want to unwind
everything. As we'll see shortly, this is where batching EVM transactions using Cadence is extremely powerful.

## Interacting with the Contracts[​](#interacting-with-the-contracts "Direct link to Interacting with the Contracts")

Before taking the easy route, let's first interact with the contracts individually to better understand the process and
status quo user experience. Realistically, this is your only option for completing the whole process on other EVM
platforms.

tip

Recall in [Prerequisites](#prerequisites) that you need to have both [MetaMask](https://metamask.io/download/) and [Flow Wallet extension](https://wallet.flow.com/download) installed and funded with
Testnet FLOW. Make sure you've done so before proceeding.

### Using MetaMask[​](#using-metamask "Direct link to Using MetaMask")

#### 1. Wrap FLOW[​](#1-wrap-flow "Direct link to 1. Wrap FLOW")

Our first action will be to wrap enough FLOW to cover the cost of minting the `MaybeMintERC721` token. To do this, we'll
interact with the `WFLOW` contract on Testnet. There are a number of ways we could interact with this contract - Remix
IDE, Foundry's CLI, Hardhat, etc. - but for the purposes of this guide, we'll use the [Flowscan EVM block explorer](https://www.evm-testnet.flowscan.io/).

Navigate to the WFLOW Testnet contract on Flowscan: [WFLOW](https://evm-testnet.flowscan.io/token/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e?tab=write_contract). Ensure you're on the `Write Contract` tab which allows you
to interact with the contract's mutating functions.

Before you can interact with the contract, you need to connect your MetaMask wallet to the [Flowscan EVM block
explorer](https://www.evm-testnet.flowscan.io/). Click the `Connect` button in the top right corner and follow the prompts to connect your MetaMask wallet.

warning

There are two **separate** block explorers for Flow - one for Cadence activity and another for EVM activity. This is
unique to Flow and is due to the fact that Cadence & EVM are separate runtimes, with EVM effectively emulated within
Cadence. This orientation - that of EVM running within Cadence - means that the Cadence-side explorer has visibility to
EVM transactions embedded within a Cadence transaction.

Practically, this means that any transactions ran using a Flow native account can be viewed on the Cadence explorer
while any transactions run using an EVM account can be viewed on the EVM explorer.

![Connect wallet to Flowscan](/assets/images/flowscan-connect-1a66f1d3de0605c1f50e5b12dc999e5b.png)

Once connected, you should see your address in the top right corner and above the contract's functions.

Now we can wrap FLOW. Click on the `deposit` method which will drop down an input field for the amount of FLOW you want
to wrap. The mint amount for the `MaybeMintERC721` contract is 1 whole FLOW which in EVM terms is `1e18 wei` - `wei`
being the smallest unit of an EVM's native currency (inherited from Ethereum's units - more on Ether units [here](https://docs.soliditylang.org/en/v0.8.28/units-and-global-variables.html#ether-units)).

As shown below, put `1 000 000 000 000 000 000` in the input field for `deposit`.

![Deposit 1 FLOW to WFLOW contract](/assets/images/wflow-deposit-faa8000b3d64f6c51944fe42c8c787a3.png)

You can now click the `Write` button to submit the transaction. Once MetaMask prompts you to sign the transaction, click
`Confirm` and give it a few seconds to process.

![Confirm WFLOW deposit in MetaMask](/assets/images/wflow-deposit-confirm-8efbd4712ebe19f67b57db4ea5a8c53c.png)

Once confirmed, you should be able to see WFLOW balance in your tokens list in MetaMask - if not, you can click on
`Import Tokens` and paste the WFLOW contract address found on the Flowscan page and refresh your list.

![WFLOW in MetaMask](/assets/images/wflow-in-metamask-tokens-32aa78afff8d2c022b5f19d420301e9f.png)

#### 2. Approve WFLOW Transfer[​](#2-approve-wflow-transfer "Direct link to 2. Approve WFLOW Transfer")

Now that you have your WFLOW, you'll need to approve the `MaybeMintERC721` contract to transfer your WFLOW. From the
same WFLOW page in Flowscan, click on the `approve` method. This time, you'll need to input the `MaybeMintERC721`
contract address - `0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2` - and the amount of WFLOW you want to approve - again `1 000 000 000 000 000 000` WFLOW.

![Approve MaybeMintERC721 for 1 WFLOW in Flowscan](/assets/images/wflow-approve-5fe2ae5b8ee30b6414519a5662bcb161.png)

Click `Write` to submit the transaction. To be clear, this does not complete a transfer, but allows the
`MaybeMintERC721` contract to transfer your WFLOW on your behalf which will execute in the next step.

#### 3. Mint ERC721 Token[​](#3-mint-erc721-token "Direct link to 3. Mint ERC721 Token")

Finally, we'll attempt to mint the ERC721 token using the `MaybeMintERC721` contract. Navigate to the `MaybeMintERC721`
contract on Flowscan: [MaybeMintERC721](https://evm-testnet.flowscan.io/address/0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2?tab=write_contract).

Again, you'll be met with the contract functions on the `Write Contract` tab. Click on the `mint` function which takes
no arguments - just click on `Write` and then `Confirm` in the resulting MetaMask window.

This contract has a 50% chance of failing on mint using onchain randomness. If it fails, simply mint again until it
succeeds.

On success, you can click on your NFTs in MetaMask to see your newly minted token.

![MaybeMintERC721 in MetaMask NFT list](/assets/images/maybe-mint-in-metamask-2585f9419df7a3696239528d91ec1874.png)

#### Recap[​](#recap "Direct link to Recap")

This process is cumbersome and requires multiple transactions, each of which could fail. Given the intent of the process -
minting an NFT - if this were a case where the NFT was a limited edition or time-sensitive, you'd be left with WFLOW
wrapped and approved for transfer, but no NFT and would need to manually unwind the process.

Or you could just use Cadence to batch these transactions and revert everything if the mint fails. Let's do that.

### Using Flow Wallet[​](#using-flow-wallet "Direct link to Using Flow Wallet")

Before diving into the "how", let's execute the batched version of everything we just did using Flow Wallet. This will
give you a sense of the power of Cadence and the Flow blockchain.

The transaction below, like all Cadence transactions, is scripted, allowing us to execute a series of actions. It may
look like a lot at first, but we will break it down step by step in the following sections.

wrap\_and\_mint.cdc `_140// TESTNET IMPORTS_140import FungibleToken from 0x9a0766d93b6608b7_140import FlowToken from 0x7e60df042a9c0868_140import EVM from 0x8c5303eaa26202d6_140_140/// This transaction demonstrates how multiple EVM calls can be batched in a single Cadence transaction via_140/// CadenceOwnedAccount (COA), performing the following actions:_140///_140/// 1. Configures a COA in the signer's account if needed_140/// 2. Funds the signer's COA with enough FLOW to cover the WFLOW cost of minting an ERC721 token_140/// 3. Wraps FLOW as WFLOW - EVM call 1_140/// 4. Approves the example MaybeMintERC721 contract which accepts WFLOW to move the mint amount - EVM call 2_140/// 5. Attempts to mint an ERC721 token - EVM call 3_140///_140/// Importantly, the transaction is reverted if any of the EVM interactions fail returning the account to the original_140/// state before the transaction was executed across Cadence & EVM._140///_140/// For more context, see https://github.com/onflow/batched-evm-exec-example_140///_140/// @param wflowAddressHex: The EVM address hex of the WFLOW contract as a String_140/// @param maybeMintERC721AddressHex: The EVM address hex of the ERC721 contract as a String_140///_140transaction(wflowAddressHex: String, maybeMintERC721AddressHex: String) {_140 _140 let coa: auth(EVM.Call) &EVM.CadenceOwnedAccount_140 let mintCost: UFix64_140 let wflowAddress: EVM.EVMAddress_140 let erc721Address: EVM.EVMAddress_140_140 prepare(signer: auth(SaveValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, UnpublishCapability) &Account) {_140 /* COA configuration & assigment */_140 //_140 let storagePath = /storage/evm_140 let publicPath = /public/evm_140 // Configure a COA if one is not found in storage at the default path_140 if signer.storage.type(at: storagePath) == nil {_140 // Create & save the CadenceOwnedAccount (COA) Resource_140 let newCOA <- EVM.createCadenceOwnedAccount()_140 signer.storage.save(<-newCOA, to: storagePath)_140_140 // Unpublish any existing Capability at the public path if it exists_140 signer.capabilities.unpublish(publicPath)_140 // Issue & publish the public, unentitled COA Capability_140 let coaCapability = signer.capabilities.storage.issue<&EVM.CadenceOwnedAccount>(storagePath)_140 signer.capabilities.publish(coaCapability, at: publicPath)_140 }_140_140 // Assign the COA reference to the transaction's coa field_140 self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: storagePath)_140 ?? panic("A CadenceOwnedAccount (COA) Resource could not be found at path ".concat(storagePath.toString())_140 .concat(" - ensure the COA Resource is created and saved at this path to enable EVM interactions"))_140_140 /* Fund COA with cost of mint */_140 //_140 // Borrow authorized reference to signer's FlowToken Vault_140 let sourceVault = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(_140 from: /storage/flowTokenVault_140 ) ?? panic("The signer does not store a FlowToken Vault object at the path "_140 .concat("/storage/flowTokenVault. ")_140 .concat("The signer must initialize their account with this vault first!"))_140 // Withdraw from the signer's FlowToken Vault_140 self.mintCost = 1.0_140 let fundingVault <- sourceVault.withdraw(amount: self.mintCost) as! @FlowToken.Vault_140 // Deposit the mint cost into the COA_140 self.coa.deposit(from: <-fundingVault)_140_140 /* Set the WFLOW contract address */_140 //_140 // View the cannonical WFLOW contract at:_140 // https://evm-testnet.flowscan.io/address/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e_140 self.wflowAddress = EVM.addressFromString(wflowAddressHex)_140_140 /* Assign the ERC721 EVM Address */_140 //_140 // Deserialize the provided ERC721 hex string to an EVM address_140 self.erc721Address = EVM.addressFromString(maybeMintERC721AddressHex)_140 }_140_140 pre {_140 self.coa.balance().inFLOW() >= self.mintCost:_140 "CadenceOwnedAccount holds insufficient FLOW balance to mint - "_140 .concat("Ensure COA has at least ".concat(self.mintCost.toString()).concat(" FLOW"))_140 }_140_140 execute {_140 /* Wrap FLOW in EVM as WFLOW */_140 //_140 // Encode calldata & set value_140 let depositCalldata = EVM.encodeABIWithSignature("deposit()", [])_140 let value = EVM.Balance(attoflow: 0)_140 value.setFLOW(flow: self.mintCost)_140 // Call the WFLOW contract, wrapping the sent FLOW_140 let wrapResult = self.coa.call(_140 to: self.wflowAddress,_140 data: depositCalldata,_140 gasLimit: 15_000_000,_140 value: value_140 )_140 assert(_140 wrapResult.status == EVM.Status.successful,_140 message: "Wrapping FLOW as WFLOW failed: ".concat(wrapResult.errorMessage)_140 )_140_140 /* Approve the ERC721 address for the mint amount */_140 //_140 // Encode calldata approve(address,uint) calldata, providing the ERC721 address & mint amount_140 let approveCalldata = EVM.encodeABIWithSignature(_140 "approve(address,uint256)",_140 [self.erc721Address, UInt256(1_000_000_000_000_000_000)]_140 )_140 // Call the WFLOW contract, approving the ERC721 address to move the mint amount_140 let approveResult = self.coa.call(_140 to: self.wflowAddress,_140 data: approveCalldata,_140 gasLimit: 15_000_000,_140 value: EVM.Balance(attoflow: 0)_140 )_140 assert(_140 approveResult.status == EVM.Status.successful,_140 message: "Approving ERC721 address on WFLOW contract failed: ".concat(approveResult.errorMessage)_140 )_140_140 /* Attempt to mint ERC721 */_140 //_140 // Encode the mint() calldata_140 let mintCalldata = EVM.encodeABIWithSignature("mint()", [])_140 // Call the ERC721 contract, attempting to mint_140 let mintResult = self.coa.call(_140 to: self.erc721Address,_140 data: mintCalldata,_140 gasLimit: 15_000_000,_140 value: EVM.Balance(attoflow: 0)_140 )_140 // If mint fails, all other actions in this transaction are reverted_140 assert(_140 mintResult.status == EVM.Status.successful,_140 message: "Minting ERC721 token failed: ".concat(mintResult.errorMessage)_140 )_140 }_140}`

You can run the transaction at the following link using the community-developed Flow Runner tool: [`wrap_and_mint.cdc`](https://run.dnz.dev/snippet/c99b25e04a2d1f28).

This transaction takes two arguments:

* WFLOW contract address: `0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e`
* MaybeMintERC721 contract address: `0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2`

Before running, ensure that the network section - bottom right corner - displays Testnet. If not, click and select
`Testnet` as your network and refresh. Once you've confirmed you're Flow Runner is targeting Testnet, copy these
addresses and paste them into the respective fields on the Flow Runner page. Click `Run` on the top left and follow the
prompts to connect your Flow Wallet and sign the transaction.

warning

Although we are running a manual transaction for the purposes of this walkthrough, you should always be careful to
review the transaction details before signing and submitting.

Again, since the ERC721 has a 50% chance of failing, you may need to run the transaction multiple times until it
succeeds. However note that if the mint fails, the entire transaction will revert, unwinding the wrapped FLOW and
approval.

Again, since the ERC721 has a 50% chance of failure and the success of the transaction is conditioned on successfully
minting, your transaction may fail. If it does fail, importantly the entire transaction reverts, unwinding the wrapped
FLOW deposit and approval - the wrapping and approval transactions **do not execute** in the event of mint failure! This
is the main takeaway of this guide, that you embed a whole sequence of EVM transactions into one atomic operation using
Cadence and if the primary intent (or intents) does not execute, everything else is reverted as well.

In our case, you'll want to submit a transaction until one succeeds. Once you submit a successful transaction, you'll
see a transaction ID with event logs in the Flow Runner output. Let's take a closer look at the transaction and its
results in the Flowscan block explorer.

![Flow Runner output on successful transaction execution](/assets/images/flow-runner-successful-output-78bdb9f935de4ae2be16b6ed913607b7.png)

Copy your transaction ID and go to the Flowscan Testnet Cadence block explorer: [Flowscan Cadence](https://testnet.flowscan.io/).

Pasting your transaction ID into the search bar will show you the transaction details, including the Cadence script,
execution status, and event logs. Click on the `EVM` tab to view the EVM transactions batched in the Cadence
transaction.

![Embedded EVM transactions on Flowscan](/assets/images/evm-embed-flowscan-9602d090f492f38f551262105d556e64.png)

Clicking on the transactions will open up the EVM transaction in Flowscan's EVM block explorer. If you view the EVM
transactions in order, you'll notice that they aggregate the same actions we took manually in the MetaMask section, but
this time in a single Cadence transaction!

## Breaking it Down[​](#breaking-it-down "Direct link to Breaking it Down")

Now that we can relate to the pain of manually executing these transactions and we've seen the magic you can work with
Cadence, let's understand what's going on under the hood.

To recap, our Cadence transaction does the following, reverting if any step fails:

1. Wraps FLOW as WFLOW
2. Approves the `MaybeMintERC721` contract to move WFLOW
3. Attempts to mint a `MaybeMintERC721` token

But how does our Flow account interact with EVM from the Cadence runtime? As you'll recall from the [Interacting with
COA](/evm/cadence/interacting-with-coa) guide, we use a Cadence-owned account (COA) to interact with EVM contracts from Cadence.

A COA is a [resource](https://cadence-lang.org/docs/solidity-to-cadence#resources) providing an interface through which Cadence can interact with the EVM runtime. This is
importantly ***in addition*** to the traditional routes you'd normally access normal EVMs - e.g. via the JSON-RPC API.
And with this interface, we can take advantage of all of the benefits of Cadence - namely here scripted transactions and
conditional execution.

So in addition to the above steps, our transaction first configures a COA in the signer's account if one doesn't already
exist. It then funds the COA with enough FLOW to cover the mint cost, sourcing funds from the signing Flow account's
Cadence Vault. Finally, it wraps FLOW as WFLOW, approves the ERC721 contract to move the mint amount, and attempts to
mint the ERC721 token.

Let's see what each step looks like in the transaction code.

### COA Configuration[​](#coa-configuration "Direct link to COA Configuration")

The first step in our transaction is to configure a COA in the signer's account if one doesn't already exist. This is
done by creating a new COA resource and saving it to the signer account's storage. A public Capability on the COA is
then issued and published on the signer's account, allowing anyone to deposit FLOW into the COA, affecting its EVM
balance.

 `_21/* COA configuration & assignment */_21//_21let storagePath = /storage/evm_21let publicPath = /public/evm_21// Configure a COA if one is not found in storage at the default path_21if signer.storage.type(at: storagePath) == nil {_21 // Create & save the CadenceOwnedAccount (COA) Resource_21 let newCOA <- EVM.createCadenceOwnedAccount()_21 signer.storage.save(<-newCOA, to: storagePath)_21_21 // Unpublish any existing Capability at the public path if it exists_21 signer.capabilities.unpublish(publicPath)_21 // Issue & publish the public, unentitled COA Capability_21 let coaCapability = signer.capabilities.storage.issue<&EVM.CadenceOwnedAccount>(storagePath)_21 signer.capabilities.publish(coaCapability, at: publicPath)_21}_21_21// Assign the COA reference to the transaction's coa field_21self.coa = signer.storage.borrow<auth(EVM.Call) &EVM.CadenceOwnedAccount>(from: storagePath)_21 ?? panic("A CadenceOwnedAccount (COA) Resource could not be found at path ".concat(storagePath.toString())_21 .concat(" - ensure the COA Resource is created and saved at this path to enable EVM interactions"))`

At the end of this section, the transaction now has an reference authorized with the `EVM.Call` [entitlement](https://cadence-lang.org/docs/language/access-control#entitlements) to use in
the `execute` block which can be used call into EVM.

You can run a transaction that does just this step here: [`setup_coa.cdc`](https://run.dnz.dev/snippet/4ec75e1f4165fa05)

Since you ran the all-in-one transaction previously, your account already has a COA configured in which case the linked
transaction won't do anything. You can lookup your Testnet account's EVM address with the script below to confirm you
have a COA configured. Simply input your Testnet Flow address and click `Run`.

### Funding the COA[​](#funding-the-coa "Direct link to Funding the COA")

Next, we fund the COA with enough FLOW to cover the mint cost. This is done by withdrawing FLOW from the signer's
FlowToken Vault and depositing it into the COA.

 `_13/* Fund COA with cost of mint */_13//_13// Borrow authorized reference to signer's FlowToken Vault_13let sourceVault = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(_13 from: /storage/flowTokenVault_13 ) ?? panic("The signer does not store a FlowToken Vault object at the path "_13 .concat("/storage/flowTokenVault. ")_13 .concat("The signer must initialize their account with this vault first!"))_13// Withdraw from the signer's FlowToken Vault_13self.mintCost = 1.0_13let fundingVault <- sourceVault.withdraw(amount: self.mintCost) as! @FlowToken.Vault_13// Deposit the mint cost into the COA_13self.coa.deposit(from: <-fundingVault)`

Taking a look at the full transaction, we can see an explicit check that the COA has enough FLOW to cover the mint cost
before proceeding into the transaction's `execute` block.

 `_10pre {_10 self.coa.balance().inFLOW() >= self.mintCost:_10 "CadenceOwnedAccount holds insufficient FLOW balance to mint - "_10 .concat("Ensure COA has at least ".concat(self.mintCost.toString()).concat(" FLOW"))_10}`

This isn't absolutely necessary as successive steps would fail on this condition, but helps provide enhanced error
messages in the event of insufficient funds.

You can run the above block in a transaction here which will move 1 FLOW from your account's Cadence FLOW balance to
your account's EVM balance, depositing it directly to your pre-configured COA: [`fund_coa.cdc`](https://run.dnz.dev/snippet/0e7370601bd9123b)

After running the linked transaction, you can check your COA's FLOW balance with the script below, just enter your COA's
EVM address (which you can get from the previous script). The resulting balance should be 1.0 (unless you've funded your
COA prior to this walkthrough).

### Setting our EVM Contract Targets[​](#setting-our-evm-contract-targets "Direct link to Setting our EVM Contract Targets")

The last step in our transaction's `prepare` block is to deserialize the provided WFLOW and ERC721 contract addresses
from hex strings to EVM addresses.

 `_10/* Set the WFLOW contract address */_10//_10// View the cannonical WFLOW contract at:_10// https://evm-testnet.flowscan.io/address/0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e_10self.wflowAddress = EVM.addressFromString(wflowAddressHex)_10_10/* Assign the ERC721 EVM Address */_10//_10// Deserialize the provided ERC721 hex string to an EVM address_10self.erc721Address = EVM.addressFromString(maybeMintERC721AddressHex)`
### Wrapping FLOW as WFLOW[​](#wrapping-flow-as-wflow "Direct link to Wrapping FLOW as WFLOW")

Next, we're on to the first EVM interaction - wrapping FLOW as WFLOW. This is done by encoding the `deposit()` function
call and setting the call value to the mint cost. The COA then calls the WFLOW contract with the encoded calldata, gas
limit, and value.

 `_17/* Wrap FLOW in EVM as WFLOW */_17//_17// Encode calldata & set value_17let depositCalldata = EVM.encodeABIWithSignature("deposit()", [])_17let value = EVM.Balance(attoflow: 0)_17value.setFLOW(flow: self.mintCost)_17// Call the WFLOW contract, wrapping the sent FLOW_17let wrapResult = self.coa.call(_17 to: self.wflowAddress,_17 data: depositCalldata,_17 gasLimit: 15_000_000,_17 value: value_17)_17assert(_17 wrapResult.status == EVM.Status.successful,_17 message: "Wrapping FLOW as WFLOW failed: ".concat(wrapResult.errorMessage)_17)`

Setting the value of the call transmits FLOW along with the call to the contract, accessible in solidity as `msg.value`.

tip

You'll notice a general pattern among all EVM calls in this transaction:

1. Encoding the calldata
2. Calling the contract
3. Asserting the call was successful

Here we're just interested in a successful call, but we could access return data if it were expected and relevant for
our Cadence transaction. This returned data is accessible from the `data` field on the `EVM.Result` object returned from
`coa.call(...)`. This data would then be decoded using `EVM.decodeABI(...)`. More on this in later guides.

You can run the above code as a transaction here: [`wrap_flow.cdc`](https://run.dnz.dev/snippet/9dbfb784da5300fb)

After running the transaction, your COA should have a WFLOW balance of 1.0 WFLOW. Confirm your WFLOW balance by running
the script below, providing your Flow account address, the WFLOW address of `0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e`
and your COA's EVM address (retrieved from a previous script):

Since Solidity does not support decimal precision, the returned balance will look like a large number. In the case of
WFLOW, we can recover the decimals by shifting the decimal place 18 digits to the left. Your account should have `1`
WFLOW or `1000000000000000000` as returned.

warning

Note that the number of places to shift varies by ERC20 implementation -- the default value is 18, but it's not safe to
assume this value. You can check a token's decimal places by calling `ERC20.decimals()(uint8)`.

### Approving the ERC721 Contract[​](#approving-the-erc721-contract "Direct link to Approving the ERC721 Contract")

Once the FLOW is wrapped as WFLOW, we approve the ERC721 contract to move the mint amount. This is done by encoding the
`approve(address,uint256)` calldata and calling the WFLOW contract with the encoded calldata.

 `_18/* Approve the ERC721 address for the mint amount */_18//_18// Encode calldata approve(address,uint) calldata, providing the ERC721 address & mint amount_18let approveCalldata = EVM.encodeABIWithSignature(_18 "approve(address,uint256)",_18 [self.erc721Address, UInt256(1_000_000_000_000_000_000)]_18 )_18// Call the WFLOW contract, approving the ERC721 address to move the mint amount_18let approveResult = self.coa.call(_18 to: self.wflowAddress,_18 data: approveCalldata,_18 gasLimit: 15_000_000,_18 value: EVM.Balance(attoflow: 0)_18)_18assert(_18 approveResult.status == EVM.Status.successful,_18 message: "Approving ERC721 address on WFLOW contract failed: ".concat(approveResult.errorMessage)_18)`

You can run this approval using the transaction, passing the WFLOW address of
`0xd3bF53DAC106A0290B0483EcBC89d40FcC961f3e` and MaybeMintERC721 address of `0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2`
: [`approve_maybe_mint_erc721.cdc`](https://run.dnz.dev/snippet/1b503d82f9a2c5a7)

The linked transaction will perform the approval step, authorizing the ERC721 to transfer WFLOW to cover the mint cost
when `mint()` is called. Confirm the contract allowance by running the script below. Pass your Flow address, WFLOW
address, ERC721 address, and your COA's EVM address.

The result is the amount of your WFLOW balance the ERC721 is allowed to transfer, which after the transaction should be
`1` WFLOW, or `1000000000000000000` as returned.

### Minting the ERC721 Token[​](#minting-the-erc721-token "Direct link to Minting the ERC721 Token")

Finally, we attempt to mint the ERC721 token. This is done by encoding the `mint()` calldata and calling the ERC721
contract with the encoded calldata. If the mint fails, the entire transaction is reverted.

 `_16/* Attempt to mint ERC721 */_16//_16// Encode the mint() calldata_16let mintCalldata = EVM.encodeABIWithSignature("mint()", [])_16// Call the ERC721 contract, attempting to mint_16let mintResult = self.coa.call(_16 to: self.erc721Address,_16 data: mintCalldata,_16 gasLimit: 15_000_000,_16 value: EVM.Balance(attoflow: 0)_16)_16// If mint fails, all other actions in this transaction are reverted_16assert(_16 mintResult.status == EVM.Status.successful,_16 message: "Minting ERC721 token failed: ".concat(mintResult.errorMessage)_16)`

You can run the minting transaction here, passing the ERC721 address of `0x2E2Ed0Cfd3AD2f1d34481277b3204d807Ca2F8c2`:
[`mint.cdc`](https://run.dnz.dev/snippet/fd7c4dda536d006e)

Again, this transaction may fail. But if you executed all the prior stepwise transactions according to the walkthrough,
you can try again until the mint succeeds. Recall that you can view your transaction details using Cadence [Flowscan](https://www.flowscan.io/)
which will also let you view the embedded EVM transactions in the `EVM` tab. Try it out, and see if you can figure out
how to get your minted NFT's URI with the script below.

### Recap[​](#recap-1 "Direct link to Recap")

All of the stepwise transactions you just executed are compiled in the first Cadence transaction we ran. Hopefully,
going through the process step by step illuminates the power and flexibility of Cadence, allowing you to write
transactions as simple or as complex as you want.

While lengthy transactions can be intimidating and even a bit verbose at times, the flexibility afforded by the language
means you are only limited by your imagination. Cadence transactions allow you to support the most streamlined of
experiences, incorporating as many contracts as needed to support your use case.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this guide, we've demonstrated how to batch EVM transactions using Cadence, allowing you to conditionally execute
multiple EVM transactions in a single Cadence transaction. While this guide focused on relatively simple EVM operations,
the principles can be applied to much more complex and interesting applications.

In the process, you learned how to:

* Read and write from smart contract functions on EVM Flowscan
* Run a Cadence transaction from the browser using [Flow Runner](https://run.dnz.dev/)
* Execute batched EVM transactions via a COA in a Cadence transaction
* Condition final transaction execution on success of all EVM transactions
* Inspect multiple EVM transactions embedded in a Cadence transaction with [Flowscan](https://www.flowscan.io/) block explorer

The biggest takeaway here isn't the specific actions taken in this walkthrough, but the overarching concept that you can
use **Cadence as an orchestration layer** to **extend existing EVM contracts**, creating unique user experiences with
the power **to differentiate your Web3 application**.

With these basics in hand, you're ready to start building more complex applications that leverage the power of Cadence
and the Flow blockchain. How will you use these features to build Web3's next killer app?

## Further Reading[​](#further-reading "Direct link to Further Reading")

Now that you've experienced the power of Cadence and EVM interactions firsthand, we recommend checking out the following
guides to deepen your understanding:

* [How Flow EVM Works](/evm/how-it-works) - Learn more about the Flow EVM and how it differs from traditional EVM platforms
* [Interacting with COAs](/evm/cadence/interacting-with-coa) - Get a fuller picture of how Cadence interacts with EVM contracts via Cadence-owned accounts
* [Cadence Transactions](/build/basics/transactions) - Learn more about the Cadence transaction model

Ready to level up your Cadence skills? Take a look at [these Cadence tutorials](https://cadence-lang.org/docs/tutorial/first-steps).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/cadence/batched-evm-transactions.md)Last updated on **Feb 18, 2025** by **Brian Doyle**[PreviousDirect Calls to Flow EVM](/evm/cadence/direct-calls)[NextCross-VM Bridge](/evm/cadence/vm-bridge)
###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
* [Overview](#overview)
* [Components](#components)
  + [Wrap FLOW as WFLOW](#wrap-flow-as-wflow)
  + [Approve ERC721 Transfer](#approve-erc721-transfer)
  + [Mint ERC721 Token](#mint-erc721-token)
* [Interacting with the Contracts](#interacting-with-the-contracts)
  + [Using MetaMask](#using-metamask)
  + [Using Flow Wallet](#using-flow-wallet)
* [Breaking it Down](#breaking-it-down)
  + [COA Configuration](#coa-configuration)
  + [Funding the COA](#funding-the-coa)
  + [Setting our EVM Contract Targets](#setting-our-evm-contract-targets)
  + [Wrapping FLOW as WFLOW](#wrapping-flow-as-wflow)
  + [Approving the ERC721 Contract](#approving-the-erc721-contract)
  + [Minting the ERC721 Token](#minting-the-erc721-token)
  + [Recap](#recap-1)
* [Conclusion](#conclusion)
* [Further Reading](#further-reading)
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

