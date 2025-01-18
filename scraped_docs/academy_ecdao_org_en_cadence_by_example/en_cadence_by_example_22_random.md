# Source: https://academy.ecdao.org/en/cadence-by-example/22-random
















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Random

# Random

While Cadence has a built-in random function, beware that users can always abort their own transactions if the result is not favorable.

cadence
```
		
			// gets a number [min, max]
access(all) fun getRandom(min: UInt64, max: UInt64): UInt64 {
    // revertibleRandom is a built-in random function to Cadence!
    let randomNumber: UInt64 = revertibleRandom<UInt64>()
    return (randomNumber % (max + 1 - min)) + min
}
		 
	
```


[Capability Controllers](/en/cadence-by-example/21-capability-controllers)
[Transaction Architecture](/en/cadence-by-example/23-transaction-architecture)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/22-random.md)

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



