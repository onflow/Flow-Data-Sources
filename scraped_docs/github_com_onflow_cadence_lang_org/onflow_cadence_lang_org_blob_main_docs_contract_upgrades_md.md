# Source: https://github.com/onflow/cadence-lang.org/blob/main/docs/contract-upgrades.md

---
title: Contract Upgrades with Incompatible Changes
---

### Problem

I have an incompatible upgrade for a contract. How can I deploy this?

### Solution

Please don't perform incompatible upgrades between contract versions in the same account.
There is too much that can go wrong.

You can make [compatible upgrades](./language/contract-updatability.md) and then run a post-upgrade function on the new contract code if needed.

If you must replace your contract rather than update it,
the simplest solution is to add or increase a suffix on any named paths in the contract code
(e.g. `/public/MyProjectVault` becomes `/public/MyProjectVault002`) in addition to making the incompatible changes,
then create a new account and deploy the updated contract there.

⚠️ Flow identifies types relative to addresses, so you will also need to provide _upgrade transactions_ to exchange the old contract's resources for the new contract's ones. Make sure to inform users as soon as possible when and how they will need to perform this task.

If you absolutely must keep the old address when making an incompatible upgrade, then you do so at your own risk. Make sure you perform the following actions in this exact order:

1. Delete any resources used in the contract account, e.g. an Admin resource.
2. Delete the contract from the account.
3. Deploy the new contract to the account.

⚠️ Note that if any user accounts contain `structs` or `resources` from the _old_ version of the contract that have been replaced with incompatible versions in the new one, **they will not load and will cause transactions that attempt to access them to crash**. For this reason, once any users have received `structs` or `resources` from the contract, this method of making an incompatible upgrade should not be attempted!
