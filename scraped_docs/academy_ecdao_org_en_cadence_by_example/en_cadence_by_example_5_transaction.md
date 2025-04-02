# Source: https://academy.ecdao.org/en/cadence-by-example/5-transaction

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Transactions

# Transactions

In order to change data in a contract, you need to send a transaction.

In Cadence, transactions (and scripts) are separate from the contract layer, and are written in different files.

Transactions can import any number of deployed contracts, so you can combine many different actions (across contracts) into 1 transcation.

Transactions always look like:

cadence

```
		
			transaction() {
   prepare(signer: &Account) {

   }
   execute {

   }
}
		 
	
```

Transactions have 2 main stages:

1. **prepare** - to access/manipulate data inside the `signer`âs account (to come laterâ¦)
2. **execute** - to execute actions

# Example Contract & Transaction

cadence

```
		
			// Contract file: Counter.cdc
// Deployed to 0x01
access(all) contract Counter {
   access(all) var count: Int

   access(all) fun increment() {
      self.count = self.count + 1
   }

   init() {
      self.count = 0
   }
}
		 
	
```

cadence

```
		
			// Transaction file: increment.cdc
import Counter from 0x01

transaction() {

   prepare(signer: &Account) {
      // we don't need to do anything 
      // with the signer's data

      // we will learn more about this later
   }

   execute {
      Counter.increment()
   }
}
		 
	
```

[Variables](/en/cadence-by-example/4-variables)
[Scripts](/en/cadence-by-example/6-scripts)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/5-transaction.md)



[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow

##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)


##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)


##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)

[Join the community](https://discord.gg/emerald-city-906264258189332541)