# Source: https://cadence-lang.org/docs/contract-upgrades




Contract Upgrades with Incompatible Changes | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
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


* Contract Upgrades with Incompatible Changes
On this page
# Contract Upgrades with Incompatible Changes

### Problem[​](#problem "Direct link to Problem")

I have an incompatible upgrade for a contract. How can I deploy this?

### Solution[​](#solution "Direct link to Solution")

Please don't perform incompatible upgrades between contract versions in the same account.
There is too much that can go wrong.

You can make [compatible upgrades](/docs/language/contract-updatability) and then run a post-upgrade function on the new contract code if needed.

If you must replace your contract rather than update it,
the simplest solution is to add or increase a suffix on any named paths in the contract code
(e.g. `/public/MyProjectVault` becomes `/public/MyProjectVault002`) in addition to making the incompatible changes,
then create a new account and deploy the updated contract there.

⚠️ Flow identifies types relative to addresses, so you will also need to provide *upgrade transactions* to exchange the old contract's resources for the new contract's ones. Make sure to inform users as soon as possible when and how they will need to perform this task.

If you absolutely must keep the old address when making an incompatible upgrade, then you do so at your own risk. Make sure you perform the following actions in this exact order:

1. Delete any resources used in the contract account, e.g. an Admin resource.
2. Delete the contract from the account.
3. Deploy the new contract to the account.

⚠️ Note that if any user accounts contain `structs` or `resources` from the *old* version of the contract that have been replaced with incompatible versions in the new one, **they will not load and will cause transactions that attempt to access them to crash**. For this reason, once any users have received `structs` or `resources` from the contract, this method of making an incompatible upgrade should not be attempted!

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/contract-upgrades.md)[PreviousGuide for Solidity Developers](/docs/solidity-to-cadence)[NextJSON-Cadence format](/docs/json-cadence-spec)
###### Rate this page

😞😐😊

* [Problem](#problem)
* [Solution](#solution)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

