# Source: https://academy.ecdao.org/en/cadence-by-example/12-optional-binding

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Optional Binding

# Optional Binding

You can use `if let` to automatically unwrap an optional type.

If the optional contains a value, the `if` branch is executed and a temporary constant or variable is set to the value contained in the optional; otherwise, the `else` branch (not required) is executed.

cadence

```
		
			access(all) fun main(profileAddress: Address) {

   let profiles: {Address: String} = {
      0x01: "Jacob",
      0x03: "Sarah"
   }

   if let profile: String = profiles[profileAddress] {
      // profile is now able to be used as a 
      // variable and it has `String` type
   } else {
      // the profile with `profileAddress`
      // did not exist, because `profiles[profileAddress]` was nil
   }
}
		 
	
```

[Optionals](/en/cadence-by-example/11-optionals)
[Structs](/en/cadence-by-example/13-structs)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/12-optional-binding.md)



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