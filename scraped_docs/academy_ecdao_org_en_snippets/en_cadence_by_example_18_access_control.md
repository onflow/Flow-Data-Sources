# Source: https://academy.ecdao.org/en/cadence-by-example/18-access-control

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Access Control

# Access Control

We use âaccess modifiersâ to determine who can read/write variables or call functions.

We will cover Entitlements in the next lesson.

![](/tutorials/access-control.png)

cadence

```
		
			access(all) contract SomeContract {

   access(all) struct SomeStruct {

      //
      // 4 Variables
      //

      access(all) var a: String

      access(account) var b: String

      access(contract) var c: String

      access(self) var d: String

      //
      // 3 Functions
      //

      access(all) fun publicFunc() {}

      access(account) fun accountFunc() {}

      access(contract) fun contractFunc() {}

      access(self) fun privateFunc() {}


      access(all) fun structFunc() {
         /**************/
         /*** AREA 1 ***/
         /**************/

         // Readable: a, b, c, d
         // Writable: a, b, c, d
         // Callable: publicFunc, accountFunc, contractFunc, privateFunc
      }

      init() {
         self.a = "a"
         self.b = "b"
         self.c = "c"
         self.d = "d"
      }
   }

   access(all) resource SomeResource {
      access(all) var e: Int

      access(all) fun resourceFunc() {
         /**************/
         /*** AREA 2 ***/
         /**************/

         // Readable: a, b, c
         // Writable: None
         // Callable: publicFunc, accountFunc, contractFunc
      }

      init() {
         self.e = 17
      }
   }

   access(all) fun questsAreFun() {
      /**************/
      /*** AREA 3 ***/
      /**************/

      // Readable: a, b, c
      // Writable: None
      // Callable: publicFunc, accountFunc, contractFunc
   }

   init() {
      self.testStruct = SomeStruct()
   }
}
		 
	
```

This is a script that imports the contract above:

cadence

```
		
			import SomeContract from 0x01

access(all) fun main() {
  /**************/
  /*** AREA 4 ***/
  /**************/

  // Readable: a
  // Writable: None
  // Callable: publicFunc
}
		 
	
```

This is a contract deployed to the same account as `SomeContract` (0x01):

cadence

```
		
			import SomeContract from 0x01
access(all) contract AnotherContract {
   /**************/
   /*** AREA 5 ***/
   /**************/

   // Readable: a, b
   // Writable: None
   // Callable: publicFunc, accountFunc
}
		 
	
```

[References](/en/cadence-by-example/17-references)
[Account Storage](/en/cadence-by-example/19-account-storage)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/18-access-control.md)



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