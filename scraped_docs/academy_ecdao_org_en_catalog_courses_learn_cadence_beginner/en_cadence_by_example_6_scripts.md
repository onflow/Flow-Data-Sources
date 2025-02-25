# Source: https://academy.ecdao.org/en/cadence-by-example/6-scripts

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Scripts

# Scripts

In order to read data from a contract, you need to execute a script.

Like transactions, scripts are separate from the contract layer, and are written in different files.

Scripts always look like:

cadence

```
		
			access(all) fun main() {
  
}
		 
	
```

# Example Contract & Script

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
		
			// Script file: get_count.cdc
import Counter from 0x01

access(all) fun main(): Int {
   return Counter.count
}
		 
	
```

[Transactions](/en/cadence-by-example/5-transaction)
[Argument Labels](/en/cadence-by-example/7-argument-labels)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/6-scripts.md)



[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow

##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)


##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)


##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)

[Join the community](https://discord.gg/emerald-city-906264258189332541)