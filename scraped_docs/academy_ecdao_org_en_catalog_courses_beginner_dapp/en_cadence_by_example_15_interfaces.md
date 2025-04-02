# Source: https://academy.ecdao.org/en/cadence-by-example/15-interfaces

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Interfaces

# Struct/Resource Interfaces

We can define and implement interfaces on structs or resources.

cadence

```
		
			access(all) contract Test {

   access(all) resource interface IWeapon {
      access(all) let rarity: String
      paccess(all)ub fun getStats(): String
   }

   // implement the interface with `: IWeapon`
   access(all) resource Sword: IWeapon {
      access(all) let rarity: String
      access(all) let sharpness: Int

      access(all) fun getStats(): String {
         return self.rarity
                  .concat(" sword with sharpness level ")
                  .concat(self.sharpness.toString())
      }

      init(rarity: String, sharpness: Int) {
         self.rarity = rarity
         self.sharpness = sharpness
      }
   }

   access(all) resource Bow: IWeapon {
      access(all) let rarity: String
      access(all) let power: Int

      access(all) fun getStats(): String {
         return self.rarity
                  .concat(" bow with power level ")
                  .concat(self.power.toString())
      }

      init(rarity: String, power: Int) {
         self.rarity = rarity
         self.power = power
      }
   }

   // notice how the interface types are written
   // (we add @ in front only because it's a resource)
   access(all) fun logAndDestroyWeapon(weapon: @{IWeapon}) {
      log(weapon.getStats())
      destroy weapon
   }

   // ... more stuff here
}
		 
	
```

Contracts can also implement interfaces defined in other contracts.

cadence

```
		
			import Test from "./Test.cdc"

access(all) contract AddedTest {
   access(all) resource Shield: Test.IWeapon {
      access(all) let rarity: String
      access(all) let endurance: Int

      access(all) fun getStats(): String {
         return self.rarity
                  .concat(" shield with endurance level ")
                  .concat(self.endurance.toString())
      }

      init(rarity: String, endurance: Int) {
         self.rarity = rarity
         self.endurance = endurance
      }
   }

   // ... more stuff here
}
		 
	
```

[Resources](/en/cadence-by-example/14-resources)
[Storing Resources](/en/cadence-by-example/16-storing-resources)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/15-interfaces.md)



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