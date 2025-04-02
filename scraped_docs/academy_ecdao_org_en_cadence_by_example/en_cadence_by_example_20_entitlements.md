# Source: https://academy.ecdao.org/en/cadence-by-example/20-entitlements

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Entitlements

# Entitlements

Entitlements are how we handle access control.

By creating an âauthorized referenceâ (looks like `auth(...)`), you can specify certain variables/functions are only accessible if you have a certain entitlement.

You can only create authorizied references if you own the resource (have the resource itself).

cadence

```
		
			// Contract file: Test.cdc
// Deployed to 0x01
access(all) contract Test {

   access(all) entitlement NameChange

   access(all) resource NFT {
      access(all) let id: UInt64
      access(all) var name: String

      access(NameChange) fun changeName(newName: String) {
         self.name = newName
      }
      
      init(name: String) {
         self.id = self.uuid
         self.name = name
      }
   }

   access(all) fun test(name: String) {
      let nft: @NFT <- create NFT(name: name)
      
      let publicRef = &nft as &NFT
      log(publicRef.name) // good
      /*
         compile-error: cannot access `changeName`: function requires `NameChange` authorization, but reference is unauthorized.

         publicRef.changeName(newName: "Bob")
      */

      let entitledRef = &nft as auth(NameChange) &NFT
      log(entitledRef.name) // good
      entitledRef.changeName(newName: "Bob") // good because we have the NameChange entitlement
   }

}
		 
	
```

[Account Storage](/en/cadence-by-example/19-account-storage)
[Capability Controllers](/en/cadence-by-example/21-capability-controllers)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/20-entitlements.md)



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