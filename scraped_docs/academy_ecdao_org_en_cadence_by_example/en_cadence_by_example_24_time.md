# Source: https://academy.ecdao.org/en/cadence-by-example/24-time
















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Time

# Time

cadence
```
		
			access(all) fun main() {
   // time is represented as a unix timestamp in seconds
   let currentTime: UFix64 = getCurrentBlock().timestamp

   // 1 minute from now
   log(currentTime + 60.0)

   // 1 hour from now
   log(currentTime + (60.0 * 60.0))

   // 1 day from now
   log(currentTime + (60.0 * 60.0 * 24.0))

   // 1 week from now
   log(currentTime + (60.0 * 60.0 * 24.0 * 7.0))

   // 1 year from now
   log(currentTime + (60.0 * 60.0 * 24.0 * 365.0))
}
		 
	
```


[Transaction Architecture](/en/cadence-by-example/23-transaction-architecture)
[Admin Access](/en/cadence-by-example/25-admin-access)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/24-time.md)

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



