# Source: https://academy.ecdao.org/en/cadence-by-example/10-dictionaries

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Dictionaries

# Dictionaries

When retrieving a value from a dictionary, an optional type is returned. More on that next.

cadence

```
		
			access(all) contract Dictionaries {
   access(all) let map: {Address: Int}

   access(all) fun add(address: Address, number: Int) {
      self.map[address] = number
   }

   access(all) fun remove(address: Address) {
      self.map.remove(key: address)
   }

   access(all) fun get(address: Address): Int? {
      return self.map[address]
   }

   init() {
      self.map = {
         0x01: 1,
         0x02: 2,
         0x03: 3
      }
   }
}
		 
	
```

[Arrays](/en/cadence-by-example/9-arrays)
[Optionals](/en/cadence-by-example/11-optionals)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/10-dictionaries.md)



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