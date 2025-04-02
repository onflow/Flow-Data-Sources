# Source: https://academy.ecdao.org/en/cadence-by-example/11-optionals

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Optionals

# Optionals

An optional type means: âThis value is either the type, or `nil`.â

For example, `Int?` means: âThis value is either `Int`, or `nil`.â

`nil` simply means nothing, or `null` in other languages.

cadence

```
		
			access(all) fun main() {
   let test_one: Int? = 3 // valid
   
   let test_two: Int? = nil // valid

   /*
    compile error: a string is not an integer or nil
   
    let test_three: Int? = "gg"
   */

   /*
    compile error: nil is not an integer

    let test_four: Int = nil
   */
}
		 
	
```

# Optionals with Dictionaries

When indexing into dictionaries, we get optional types back.

To get rid of the optional type (âunwrap itâ), we can use the force-unwrap operator `!`, or `panic` (recommended) if we want to provide an explanation for why the value is `nil`.

cadence

```
		
			access(all) fun main() {
   let map: {Address: Int} = {
      0x01: 1,
      0x02: 2
   }

   let test_one: Int? = map[0x01] // 1
   
   let test_two: Int? = map[0x05] // nil (because nothing was there)

   /*
    compile error: we get an optional back, but trying to cast to Int
   
    let test_three: Int = map[0x01]
   */

   // use the force-unwrap operator `!` to get rid of the optional
   let test_four: Int = map[0x01]! // 1

   /*
    run-time error: cannot cast nil to Int
   
    let test_five: Int = map[0x05]!
   */

   let test_six: Int = map[0x01] ?? panic("Address 0x01 does not exist in the dictionary.")

   /*
    run-time error: Address 0x05 does not exist in the dictionary.
    
    let test_seven: Int = map[0x05] ?? panic("Address 0x05 does not exist in the dictionary.")
   */
}
		 
	
```

[Dictionaries](/en/cadence-by-example/10-dictionaries)
[Optional Binding](/en/cadence-by-example/12-optional-binding)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/11-optionals.md)



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