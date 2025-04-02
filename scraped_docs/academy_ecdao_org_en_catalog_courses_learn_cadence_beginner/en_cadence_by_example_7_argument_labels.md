# Source: https://academy.ecdao.org/en/cadence-by-example/7-argument-labels

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Argument Labels

# Argument Labels

Function parameters must have a name and a type.

When calling functions, you must provide âargument labelsâ unless the function parameter is defined with a `_`  in front of it.

cadence

```
		
			// Contract file: Test.cdc
// Deployed to 0x01
access(all) contract Test {
   
  access(all) fun add1(x: Int, y: Int): Int {
    return x + y
  }

  access(all) fun add2(_ x: Int, y: Int): Int {
    return x + y
  }

  access(all) fun add3(_ x: Int, _ y: Int): Int {
    return x + y
  }

}
		 
	
```

cadence

```
		
			// Script file: add.cdc
import Test from 0x01

access(all) fun main() {
  // must provide x and y argument labels
  let test1 = Test.add1(x: 10, y: 5)

  // only the y argument label is needed
  let test2 = Test.add2(10, y: 5)

  let test3 = Test.add3(10, 5)
}
		 
	
```

[Scripts](/en/cadence-by-example/6-scripts)
[If-Else](/en/cadence-by-example/8-if-else)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/7-argument-labels.md)



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