# Source: https://cadence-lang.org/docs/tutorial/voting




9. Voting Contract | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
  + [1. First Steps](/docs/tutorial/first-steps)
  + [2. Hello World](/docs/tutorial/hello-world)
  + [3. Resource Contract Tutorial](/docs/tutorial/resources)
  + [4. Capability Tutorial](/docs/tutorial/capabilities)
  + [5.1 Non-Fungible Token Tutorial Part 1](/docs/tutorial/non-fungible-tokens-1)
  + [5.2 Non-Fungible Token Tutorial Part 2](/docs/tutorial/non-fungible-tokens-2)
  + [6. Fungible Token Tutorial](/docs/tutorial/fungible-tokens)
  + [7. Marketplace Setup](/docs/tutorial/marketplace-setup)
  + [8. Marketplace](/docs/tutorial/marketplace-compose)
  + [9. Voting Contract](/docs/tutorial/voting)
  + [10. Composable Resources](/docs/tutorial/resources-compose)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Tutorial
* 9. Voting Contract
On this page
# 9. Voting Contract

In this tutorial, we're going to deploy a contract that allows users to vote on multiple proposals that a voting administrator controls.

---


info

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/e8e2af39-370d-4a52-9f0b-bfb3b12c7eff>](https://play.flow.com/e8e2af39-370d-4a52-9f0b-bfb3b12c7eff)

The tutorial will be asking you to take various actions to interact with this code.


Action

Instructions that require you to take action are always included in a callout box like this one.
These highlighted actions are all that you need to do to get your code running,
but reading the rest is necessary to understand the language's design.

With the advent of blockchain technology and smart contracts,
it has become popular to try to create decentralized voting mechanisms that allow large groups of users to vote completely on chain.
This tutorial will provide a trivial example for how this might be achieved by using a resource-oriented programming model.

We'll take you through these steps to get comfortable with the Voting contract.

1. Deploy the contract to account `0x06`
2. Create proposals for users to vote on
3. Use a transaction with multiple signers to directly transfer the `Ballot` resource to another account.
4. Record and cast your vote in the central Voting contract
5. Read the results of the vote

Before proceeding with this tutorial, we highly recommend following the instructions in [Getting Started](/docs/tutorial/first-steps)
and [Hello, World!](/docs/tutorial/hello-world) to learn how to use the Playground tools and to learn the fundamentals of Cadence.

## A Voting Contract in Cadence[​](#a-voting-contract-in-cadence "Direct link to A Voting Contract in Cadence")

In this contract, a Ballot is represented as a resource.

An administrator can give Ballots to other accounts, then those accounts mark which proposals they vote for
and submit the Ballot to the central smart contract to have their votes recorded.

Using a [resource](/docs/language/resources) type is logical for this application, because if a user wants to delegate their vote,
they can send that Ballot to another account, and the use case of voting ballots benefits from the uniqueness and existence guarantees
inherent to resources.

## Write the Contract[​](#write-the-contract "Direct link to Write the Contract")

Time to see the contract we'll be working with:

Action

1. Open Contract 1 - the `ApprovalVoting` contract.

The contract should have the following contents:

ApprovalVoting.cdc `_61/*_61*_61* In this example, we want to create a simple approval voting contract_61* where a polling place issues ballots to addresses._61*_61* The run a vote, the Admin deploys the smart contract,_61* then initializes the proposals_61* using the initialize_proposals.cdc transaction._61* The array of proposals cannot be modified after it has been initialized._61*_61* Then they will give ballots to users by_61* using the issue_ballot.cdc transaction._61*_61* Every user with a ballot is allowed to approve any number of proposals._61* A user can choose their votes and cast them_61* with the cast_vote.cdc transaction._61*_61*. See if you can code it yourself!_61*_61*/_61_61access(all)_61contract ApprovalVoting {_61_61 // Field: An array of strings representing proposals to be approved_61_61 // Field: A dictionary mapping the proposal index to the number of votes per proposal_61_61 // Entitlement: Admin entitlement that restricts the privileged fields_61 // of the Admin resource_61_61 // Resource: Ballot resource that is issued to users._61 // When a user gets a Ballot object, they call the `vote` function_61 // to include their votes for each proposal, and then cast it in the smart contract_61 // using the `cast` function to have their vote included in the polling_61 // Remember to track which proposals a user has voted yes for in the Ballot resource_61 // and remember to include proper pre and post conditions to ensure that no mistakes are made_61 // when a user submits their vote_61 access(all) resource Ballot {_61_61 }_61_61 // Resource: Administrator of the voting process_61 // initialize the proposals and to provide a function for voters_61 // to get a ballot resource_61 // Remember to include proper conditions for each function!_61 // Also make sure that the privileged fields are secured with entitlements!_61 access(all) resource Administrator {_61 _61 }_61_61 // Public function: A user can create a capability to their ballot resource_61 // and send it to this function so its votes are tallied_61 // Remember to include a provision so that a ballot can only be cast once!_61_61 // initialize the contract fields by setting the proposals and votes to empty_61 // and create a new Admin resource to put in storage_61 init() {_61 _61 }_61}`

Now is your chance to write some of your own Cadence code!
See if you can follow the instructions in the comments of the contract
to write your own approval voting contract.
Instructions for transactions are also included in the sample transactions.
Once you're done, share your project with the Flow community in the Flow discord! :)

## Deploy the Contract[​](#deploy-the-contract "Direct link to Deploy the Contract")

Action

1. In the bottom right deployment modal, press the arrow to expand and make sure account `0x06` is selected as the signer.
2. Click the Deploy button to deploy it to account `0x06`
## Perform Voting[​](#perform-voting "Direct link to Perform Voting")

Performing the common actions in this voting contract only takes three types of transactions.

1. Initialize Proposals
2. Send `Ballot` to a voter
3. Cast Vote

We have a transaction for each step that we provide a skeleton of for you.
With the `ApprovalVoting` contract deployed to account `0x06`:

Action

1. Open Transaction 1 which should have `Create Proposals`
2. Submit the transaction with account `0x06` selected as the only signer.

CreateProposals.cdc `_26import ApprovalVoting from 0x06_26_26// This transaction allows the administrator of the Voting contract_26// to create new proposals for voting and save them to the smart contract_26_26transaction {_26 // Fill in auth() with the correct entitlements you need!_26 prepare(admin: auth()) {_26_26 // borrow a reference to the admin Resource_26 // remember to use descriptive error messages!_26_26 // Call the initializeProposals function_26 // to create the proposals array as an array of strings_26 // Maybe we could create two proposals for the local basketball league:_26 // ["Longer Shot Clock", "Trampolines instead of hardwood floors"]_26_26 // Issue and public a public capability to the Administrator resource_26 // so that voters can get their ballots!_26 }_26_26 post {_26 // Verify that the proposals were initialized properly_26 }_26_26}`

This transaction allows the `Administrator` of the contract to create new proposals for voting and save them to the smart contract. They do this by calling the `initializeProposals` function on their stored `Administrator` resource, giving it two new proposals to vote on.
We use the `post` block to ensure that there were two proposals created, like we wished for.

Next, the `Administrator` needs to hand out `Ballot`s to the voters. There isn't an easy `deposit` function this time for them to send a `Ballot` to another account, so how would they do it?

## Putting Resource Creation in public capabilities[​](#putting-resource-creation-in-public-capabilities "Direct link to Putting Resource Creation in public capabilities")

Unlike our other tutorial contracts, the Approval Voting contract
puts its Ballot creation function in a resource instead of as a public function in a contract.
This way, the admin can control who can and cannot create a Ballot resource.
There are also ways to consolidate all of the voting logic into the Admin resource
so that there can be multiple sets of proposals being voted on at the same time
without having to deploy a new contract for each one!

Here, we're just exposing the create ballot function through a public capability
for simplicity, so lets use the transaction for a voter to create a ballot.

Action

1. Open the `Create Ballot` transaction.
2. Select account `0x07` as a signer.
3. Submit the transaction by clicking the `Send` button

CreateBallot.cdc `_21_21import ApprovalVoting from 0x06_21_21// This transaction allows a user_21// to create a new ballot and store it in their account_21// by calling the public function on the Admin resource_21// through its public capability_21_21transaction {_21 // fill in the correct entitlements!_21 prepare(voter: auth() &Account) {_21_21 // Get the administrator's public account object_21 // and borrow a reference to their Administrator resource_21_21 // create a new Ballot by calling the issueBallot_21 // function of the admin Reference_21_21 // store that ballot in the voter's account storage_21 }_21}`

After this transaction, account `0x07` should now have a `Ballot` resource
object in its account storage. You can confirm this by selecting `0x07`
from the lower-left sidebar and seeing `Ballot` resource listed under the `Storage` field.

## Casting a Vote[​](#casting-a-vote "Direct link to Casting a Vote")

Now that account `0x07` has a `Ballot` in their storage, they can cast their vote.
To do this, they will call the `vote` method on their stored resource,
then cast that `Ballot` by passing it to the `cast` function in the main smart contract.

Action

1. Open the `Cast Ballot` transaction.
2. Select account `0x07` as the only transaction signer.
3. Click the `send` button to submit the transaction.

CastBallot.cdc `_23import ApprovalVoting from 0x06_23_23// This transaction allows a voter to select the votes they would like to make_23// and cast that vote by using the cast vote function_23// of the ApprovalVoting smart contract_23_23transaction {_23 // fill in the correct entitlements!_23 prepare(voter: auth() &Account) {_23_23 // Borrow a reference to the Ballot resource in the Voter's storage_23 _23 // Vote on the proposal_23_23 // Issue a capability to the Ballot resource in the voter's storage_23_23 // Cast the vote by submitting it to the smart contract_23 }_23_23 post {_23 // verify that the votes were cast properly_23 }_23}`

In this transaction, the user votes for one of the proposals by submitting
their votes on their own ballot and then sending the capability.

## Reading the result of the vote[​](#reading-the-result-of-the-vote "Direct link to Reading the result of the vote")

At any time, anyone could read the current tally of votes by directly reading the fields of the contract. You can use a script to do that, since it does not need to modify storage.

Action

1. Open the `Get Votes` script.
2. Click the `execute` button to run the script.

GetVotes.cdc `_16import ApprovalVoting from 0x06_16_16// This script allows anyone to read the tallied votes for each proposal_16//_16_16// Fill in a return type that can properly represent the number of votes_16// for each proposal_16// This might need a custom struct to represent the data_16access(all) fun main(): {_16_16 // Access the public fields of the contract to get_16 // the proposal names and vote counts_16_16 // return them to the calling context_16_16}`

The return type should reflect the number of votes that were cast for each proposal
with the `Cast Vote` transaction.

## Other Voting possibilities[​](#other-voting-possibilities "Direct link to Other Voting possibilities")

This contract was a very simple example of voting in Cadence.
It clearly couldn't be used for a real-world voting situation,
but hopefully you can see what kind of features could be added to it to ensure practicality and security.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/09-voting.md)[Previous8. Marketplace](/docs/tutorial/marketplace-compose)[Next10. Composable Resources](/docs/tutorial/resources-compose)
###### Rate this page

😞😐😊

* [A Voting Contract in Cadence](#a-voting-contract-in-cadence)
* [Write the Contract](#write-the-contract)
* [Deploy the Contract](#deploy-the-contract)
* [Perform Voting](#perform-voting)
* [Putting Resource Creation in public capabilities](#putting-resource-creation-in-public-capabilities)
* [Casting a Vote](#casting-a-vote)
* [Reading the result of the vote](#reading-the-result-of-the-vote)
* [Other Voting possibilities](#other-voting-possibilities)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

