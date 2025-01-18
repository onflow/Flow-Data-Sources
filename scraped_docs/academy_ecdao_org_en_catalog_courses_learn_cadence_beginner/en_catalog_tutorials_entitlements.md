# Source: https://academy.ecdao.org/en/catalog/tutorials/entitlements




















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Catalog](/en/catalog)
Entitlements (new access control system)

# Entitlements (new access control system)


Tutorial

Beginner

10 minutes



The old way of determining access control based on an objectâs type is going away. This tutorial will walk through the new mechanism: **Entitlements**.

If you would like to learn by video, check this out. Otherwise, the written content below is exactly the same.

  

Follow along in a video format.
# Example Overview

In order to showcase the new Entitlements system, letâs create an example contract so we can compare how you would access an objectâs fields & functions in the old vs. new way side by side. We will have to define 2 different contracts - one in old Cadence, and one using Cadence 1.0 to properly show examples.

Old Cadence Contract:

cadence
```
		
			pub contract HelloWorld {

    pub resource interface IGreeting {
        pub var greeting: String
    }

    pub resource Greeting: IGreeting {
        pub var greeting: String

        pub fun changeGreeting(newGreeting: String) {
            self.greeting = newGreeting
        }

        init(greeting: String) {
            self.greeting = greeting
        }
    }

    pub fun createGreeting(greeting: String): @Greeting {
        return <- create Greeting(greeting: greeting)
    }

}
		 
	
```

Cadence 1.0 Contract:

cadence
```
		
			access(all) contract HelloWorld {

    access(all) entitlement ChangeGreeting

    access(all) resource Greeting {
        access(all) var greeting: String

        access(ChangeGreeting) fun changeGreeting(newGreeting: String) {
            self.greeting = newGreeting
        }

        init(greeting: String) {
            self.greeting = greeting
        }
    }

    access(all) fun createGreeting(greeting: String): @Greeting {
        return <- create Greeting(greeting: greeting)
    }

}
		 
	
```

In each case, the idea is that we have a `Greeting` resource. We want the public to be able to read the `greeting` variable, but only the owner of the resource should be able to call the `changeGreeting` function.

## Old vs. New: Restricting Access

In the old way of determining access control, you would limit an objectâs access by restricting it with an interface.

Here is how you would have done that:

cadence
```
		
			import HelloWorld from 0x01

access(all) fun main(greeting: String) {
   let g: @HelloWorld.Greeting <- HelloWorld.createGreeting(greeting: greeting)

   // full access
   let gRef: &HelloWorld.Greeting = &g as &HelloWorld.Greeting
   log(gRef.greeting) // ok
   gRef.changeGreeting(newGreeting: "Test") // ok

   // restricted access based on the `IGreeting` interface
   let restrictedRef: &HelloWorld.Greeting{HelloWorld.IGreeting} = &g as &HelloWorld.Greeting{HelloWorld.IGreeting}
   log(restrictedRef.greeting) // ok
   /*
        ERROR: `changeGreeting` not accessible

        restrictedRef.changeGreeting(newGreeting: "Test")
   */

   destroy g
}
		 
	
```

In the new way of determining access control, **access is not determined by the type. It is determined by its entitlement.**

Here is the new way of doing the above (using the new Cadence 1.0 contract):

cadence
```
		
			import HelloWorld from 0x01

access(all) fun main(greeting: String) {
   let g: @HelloWorld.Greeting <- HelloWorld.createGreeting(greeting: greeting)

   // full access
   let gRef: auth(HelloWorld.ChangeGreeting) &HelloWorld.Greeting = &g
   log(gRef.greeting) // ok
   gRef.changeGreeting(newGreeting: "Test") // ok

   // restricted access based on not having the `ChangeGreeting` entitlement
   let restrictedRef: &HelloWorld.Greeting = &g
   log(restrictedRef.greeting) // ok
   /*
        ERROR: `changeGreeting` not accessible

        restrictedRef.changeGreeting(newGreeting: "Test")
   */

   destroy g
}
		 
	
```

We don't need the `as` cast anymore for references if we specify the type.

As you can see, instead of declaring an interface and restricting a type to the fields/functions available in the interface, you have to create a new entitlement and declare that entitlement as the access for a field/function, which will only be accessible if you have that specific entitled (âauthorizedâ) reference to it.

## Conclusion

There are other new features included in the new Entitlements system, but I wanted to make it easy to digest. I will continually update this tutorial with more complicated features. I hope this helped!

Also, if youâd like to view the official changes for Entitlements, go [here](https://forum.flow.com/t/update-on-cadence-1-0/5197#entitlements-and-safe-down-casting-40).

Till next time ~ Jacob Tucker


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Video lesson](#)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/tutorials/entitlements/en/readme.md)


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



