# Source: https://academy.ecdao.org/en/catalog/tutorials/user-profile

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Catalog](/en/catalog)
Create a User Profile using Cadence

# Create a User Profile using Cadence

Tutorial

Beginner

10 mins

# Tutorial - Making a User Profile using Cadence

GM! Welcome, everyone, to this session on developing our very first User Profile using Cadence. I am Memxor, your neighborhoodâs average nerdy developer, and Iâm excited to guide you through this process.

To get started, we will be utilizing the powerful [Flow Playground](https://play.flow.com/) tool for developing our smart contract. It provides us with a convenient environment to write and test our Cadence code effectively.

Without further ado, letâs jump right into the action!

## Some basics about Cadence

Before we dive into writing our User Profile smart contract, itâs essential to understand the access types in Cadence and how they relate to access modifiers in other programming languages, such as public, private, and protected.

In Cadence, access types control how resources and functions can be accessed within a contract. Letâs explore the different access types and their similarities to access modifiers in other languages:

### Access(all):

This access type is similar to the public access modifier in other languages. It means that the resource or function can be accessed from any account, including both within and outside the contract.

### Access(contract):

This access type is similar to the private access modifier in other languages. It means that the resource or function can only be accessed from within the same contract. Other contracts or accounts cannot directly access these resources or invoke these functions.

### Access(self):

This access type is unique to Cadence and provides access within the same function. It is similar to the private access modifier, but with the distinction that it limits access to the function rather than the whole contract. Resources or functions marked with access(self) can only be accessed within the same function or contract, not by other accounts or contracts.

Understanding these access types will help us define the appropriate access modifiers for our User Profile smart contract. It ensures that our contractâs resources and functions are accessible in a controlled and secure manner.

That being said, Cadence also supports `pub` and `priv`. But we will continue with access().

## Step 1 - Making the User Profile Contract

In this step, we will focus on writing the Cadence smart contract responsible for managing user profiles. The user profile will contain information about individuals in our application.

Letâs start by defining the structure of the contract and we will learn what itâs doing along the way.

cadence

```
		
			access(all) contract Profile
{
    access(contract) var totalUsersCount: UInt64;

    access(all) var publicProfileStoragePath: PublicPath;
    access(all) var storageProfileStoragePath: StoragePath;

    init()
    {
        self.totalUsersCount = 0;

        self.publicProfileStoragePath = /public/userProfile;
        self.storageProfileStoragePath = /storage/userProfile;
    }
}
		 
	
```

1. `access(all) contract Profile`: This line declares a contract named `Profile` with the `access(all)` access type. It means that this contract can be accessed from any account, both within and outside the contract.
2. `access(contract) var totalUsersCount: UInt64;`: This line declares a variable named `totalUsersCount` of type `UInt64` (an unsigned 64-bit integer). The variable has the `access(contract)` access type, which means it can only be accessed within the same contract.
3. `access(all) var publicProfileStoragePath: PublicPath;` and `access(all) var storageProfileStoragePath: StoragePath;`: These lines declare two variables, `publicProfileStoragePath` and `storageProfileStoragePath`. Both variables have the `access(all)` access type. These are the storage paths, if youâre not sure what they are please refer to the [Beginner Candence Course](https://academy.ecdao.org/en/catalog/courses/beginner-cadence/chapter4/lesson1).
4. `init()`: This is the initialization function for the contract. It is called when the contract is created. In this function, the following actions are performed:

   * `self.totalUsersCount = 0;`: Sets the initial value of `totalUsersCount` to 0. This variable will be used to keep track of the total number of users.
   * `self.publicProfileStoragePath = /public/userProfile;` and `self.storageProfileStoragePath = /storage/userProfile;`: Assigns the paths to the `publicProfileStoragePath` and `storageProfileStoragePath` variables. These paths represent the storage locations where user profile information will be stored.

Feel free to copy and paste the code snippet and modify to your needs.

Now letâs go ahead abit and define the `UserProfileInfo` struct that will be returned by `getUserProfileInfo()` in our next step.

cadence

```
		
			    access(all) struct UserProfileInfo
    {
        access(all) let id: UInt64;
        access(all) let name: String;
        access(all) let address: String;

        init(_ id: UInt64, _ name: String, _ address: String)
        {
            self.id = id;
            self.name = name;
            self.address = address;
        }
    }
		 
	
```

1. `access(all) struct UserProfileInfo`: This line declares a struct named `UserProfileInfo` with the `access(all)` access type. A struct in Cadence is a composite data type that can contain multiple fields.
2. `access(all) let id: UInt64;`, `access(all) let name: String;`, `access(all) let address: String;`: These lines declare three properties of the `UserProfileInfo` struct: `id`, `name`, and `address`.
3. `init(_ id: UInt64, _ name: String, _ address: String)`: This is the initialization function for the `UserProfileInfo` struct. It takes three parameters: `id` of type `UInt64`, `name` of type `String`, and `address` of type `String`. The function initializes the `id`, `name`, and `address` properties of the `UserProfileInfo` struct with the provided parameter values.

Now, we will add our `UserProfile` resource. If youâre not sure what resources are please refer to the [Beginner Cadence Course](https://academy.ecdao.org/en/catalog/courses/beginner-cadence/chapter3/lesson1).

cadence

```
		
			    access(all) resource UserProfile : IUserProfilePublic
    {
        access(all) let id: UInt64;
        access(all) let address: String;
        access(all) var name: String;

        access(all) fun getUserProfileInfo(): UserProfileInfo
        {
            return UserProfileInfo(self.id, self.name, self.address);
        }

        access(all) fun updateUserName(_ name: String)
        {
            self.name = name;
        }

        init(_ id: UInt64, _ name: String, _ address: String)
        {
            self.id = id;
            self.name = name;
            self.address = address;
        }
    }
		 
	
```

1. `access(all) resource UserProfile : IUserProfilePublic`: This line declares a resource named `UserProfile` with the `access(all)` access type. A resource in Cadence is a type of object that is owned by a single account and can be moved or consumed during transactions. It also implements the `IUserProfilePublic` interface, which we will look at next, and why do we use it.
2. `access(all) let id: UInt64;`, `access(all) let address: String;`, `access(all) var name: String;`: These lines declare three properties of the `UserProfile` resource: `id`, `address`, and `name`. All three properties have the `access(all)` access type.
3. `access(all) fun getUserProfileInfo(): UserProfileInfo`: This line declares a function named `getUserProfileInfo`. The function returns a value of type `UserProfileInfo`, which we defined in the previous step.
4. `access(all) fun updateUserName(_ name: String)`: This line declares a function named `updateUserName` that takes a parameter `name` of type `String`. The function has the `access(all)` access type, making it accessible from any account. The function updates the `name` property of the `UserProfile` resource with the provided `name` parameter value.
5. `init(_ id: UInt64, _ name: String, _ address: String)`: This is the initialization function for the `UserProfile` resource. It takes three parameters: `id` of type `UInt64`, `name` of type `String`, and `address` of type `String`. The function initializes the `id`, `name`, and `address` properties of the `UserProfile` resource with the provided parameter values.

Feel free to copy and paste the code snippet and modify to your needs.

Going ahead we will define the `IUserProfilePublic` interface first, then we will talk about why we need it! If youâre not sure what interfaces are please chec out the [Beginner Cadence Course](https://academy.ecdao.org/en/catalog/courses/beginner-cadence/chapter5/lesson2)

cadence

```
		
			    access(all) resource interface IUserProfilePublic
    {
        access(all) let id: UInt64;
        access(all) let address: String;
        access(all) var name: String;
        
        access(all) fun getUserProfileInfo(): UserProfileInfo;
    }
		 
	
```

1. `access(all) resource interface IUserProfilePublic`: This line declares a resource interface named `IUserProfilePublic` with the `access(all)` access type. A resource interface in Cadence defines a set of properties and functions that can be implemented by a resource types.
2. `access(all) let id: UInt64;`, `access(all) let address: String;`, `access(all) var name: String;`: These lines declare three properties within the `IUserProfilePublic` interface: `id`, `address`, and `name`. Which is exactly same as what we defined in the resource.
3. `access(all) fun getUserProfileInfo(): UserProfileInfo;`: This line declares a function within the `IUserProfilePublic` interface named `getUserProfileInfo`. Which is again same as we defined in the resource.

Youâll notice that the fuction has no boby, thatâs because the interface only defines it, and it must be implemented by the resource itself. Same goes with the variables we just define them in the interface and then initialize them in the resource.

Another thing youâll notice is that the interface doesnât contain the `updateUserName` function. Which bring us to, why do we even need the interface? If you know a few things about Cadence youâll also know that you can borrow a resource and do things with it, now imagine if someone had the full access to our resource including the `updateUserName` function. Anyone would be able to borrow anyoneâs resource and change its name, which is not ideal. So we make an interface that doesnât have the `updateUserName` function, and then give everyone the access to this interface. Which means anyone will be able to see our name, id and address. But only the owner will be able to change it. Isnât that cool?

And finally, we will define a function in the contract that we will be able to call from outside the contract from a trasaction, that will help us to create a user profile.

cadence

```
		
			    access(all) fun createUserProfile(_ name: String, _ address: String): @UserProfile
    {
        let newUserProfile <- create UserProfile(self.totalUsersCount, name, address);
        self.totalUsersCount = self.totalUsersCount + 1;
        return <- newUserProfile;
    }
		 
	
```

1. `access(all) fun createUserProfile(_ name: String, _ address: String): @UserProfile`: This line declares a function named `createUserProfile`. It takes two parameters: `name` of type `String` and `address` of type `String`. The function returns a reference to a resource of type `UserProfile` using the `@UserProfile` syntax. `@` in Cadence means a type, in C# it may look like `typeof(UserProfile)`.
2. `let newUserProfile <- create UserProfile(self.totalUsersCount, name, address);`: This line creates a new instance of the `UserProfile` resource using the `create` keyword. It initializes the `newUserProfile` variable with the newly created resource. The `self.totalUsersCount` parameter passed to the `UserProfile` constructor represents the ID for the new user profile, which is obtained from the `totalUsersCount` property of the current contract.
3. `self.totalUsersCount = self.totalUsersCount + 1;`: This line increments the `totalUsersCount` property of the current contract by 1. This ensures that each newly created user profile receives a unique ID.
4. `return <- newUserProfile;`: This line returns the newly created user profile resource using the `<-` arrow syntax. The caller of the `createUserProfile` function will receive a reference to the created `UserProfile` resource.

All right! Thatâs our whole contract. Wasnât that easy? I hope it was.

The whole contract in action might look something like this

cadence

```
		
			access(all) contract Profile
{
    access(contract) var totalUsersCount: UInt64;

    access(all) var publicProfileStoragePath: PublicPath;
    access(all) var storageProfileStoragePath: StoragePath;

    access(all) resource interface IUserProfilePublic
    {
        access(all) let id: UInt64;
        access(all) let address: String;
        access(all) var name: String;
        
        access(all) fun getUserProfileInfo(): UserProfileInfo;
    }

    access(all) resource UserProfile : IUserProfilePublic
    {
        access(all) let id: UInt64;
        access(all) let address: String;
        access(all) var name: String;

        access(all) fun getUserProfileInfo(): UserProfileInfo
        {
            return UserProfileInfo(self.id, self.name, self.address);
        }

        access(all) fun updateUserName(_ name: String)
        {
            self.name = name;
        }

        init(_ id: UInt64, _ name: String, _ address: String)
        {
            self.id = id;
            self.name = name;
            self.address = address;
        }
    }

    access(all) fun createUserProfile(_ name: String, _ address: String): @UserProfile
    {
        let newUserProfile <- create UserProfile(self.totalUsersCount, name, address);
        self.totalUsersCount = self.totalUsersCount + 1;
        return <- newUserProfile;
    }

    access(all) struct UserProfileInfo
    {
        access(all) let id: UInt64;
        access(all) let name: String;
        access(all) let address: String;

        init(_ id: UInt64, _ name: String, _ address: String)
        {
            self.id = id;
            self.name = name;
            self.address = address;
        }
    }

    init()
    {
        self.totalUsersCount = 0;

        self.publicProfileStoragePath = /public/userProfile;
        self.storageProfileStoragePath = /storage/userProfile;
    }
}
		 
	
```

Now, Letâs go ahead and deploy it to `0x01` account. Select `0x01` and then click on deploy. As shown in the image below!

![Deployment Example](https://i.imgur.com/uG7Ag6B.png)

## Step 2 - Making our transactions

We will write 2 transactions, 1 for creating a userProfile and 1 for updating the name in a userProfile.

### Creating a User Profile

cadence

```
		
			import Profile from 0x01;

transaction(name: String)
{
  prepare(acct: AuthAccount) 
  {
    let newUserProfile <- Profile.createUserProfile(name, acct.address.toString());
    acct.save(<- newUserProfile, to: Profile.storageProfileStoragePath);
    acct.link<&Profile.UserProfile{Profile.IUserProfilePublic}>(Profile.publicProfileStoragePath, target: Profile.storageProfileStoragePath);
  }
}
		 
	
```

1. `import Profile from 0x01;`: This line imports the contract named `Profile` from the address `0x01`. It allows the transaction to use the functions and resources defined in the `Profile` contract.
2. `transaction(name: String)`: This line declares a transaction that takes a parameter `name` of type `String`. A transaction in Cadence represents a sequence of operations that can modify the state of the blockchain.
3. `prepare(acct: AuthAccount)`: This line defines the `prepare` block of the transaction. It takes an `AuthAccount` argument named `acct`, which represents the authenticated account initiating the transaction.
4. `let newUserProfile <- Profile.createUserProfile(name, acct.address.toString());`: This line creates a new user profile by calling the `createUserProfile` function from the imported `Profile` contract. It passes the `name` parameter and the string representation of the accountâs address (`acct.address.toString()`) as arguments. Then we use the `<-` syntax to move the newly created resource into the variable.
5. `acct.save(<- newUserProfile, to: Profile.storageProfileStoragePath);`: This line saves the newly created user profile resource to the storage path specified by `Profile.storageProfileStoragePath`. The `<-` syntax is used again to move the resource from the variable to storage.
6. `acct.link<&Profile.UserProfile{Profile.IUserProfilePublic}>(Profile.publicProfileStoragePath, target: Profile.storageProfileStoragePath);`: This line establishes a link between the public storage path `Profile.publicProfileStoragePath` and the storage path where the user profile resource is stored `Profile.storageProfileStoragePath`. The `link` function is called on the `acct` account object, specifying the type `&Profile.UserProfile{Profile.IUserProfilePublic}` to indicate the resource interface type being linked. By doing this, we will be able to read the state of any User Profile from any Script.

Wanna give it a spin? Type you name in the box below and hit Send. As shown in the image below!

![Trasaction of User Profile Creation Example](https://i.imgur.com/JPtQrtq.png)

### Updating the name in a User Profile

cadence

```
		
			import Profile from 0x01;

transaction(name: String)
{
  prepare(acct: AuthAccount) 
  {
    let userInfo = acct.borrow<&Profile.UserProfile>(from: Profile.storageProfileStoragePath) ?? panic("Can't borrow the file from storage!");
    userInfo.updateUserName(name);
  }
}
		 
	
```

1. `import Profile from 0x01;`: This line imports the contract named `Profile` from the address `0x01`. It allows the transaction to use the functions and resources defined in the `Profile` contract.
2. `transaction(name: String)`: This line declares a transaction that takes a parameter `name` of type `String`.
3. `prepare(acct: AuthAccount)`: This line defines the `prepare` block of the transaction. It takes an `AuthAccount` argument named `acct`, which represents the authenticated account initiating the transaction.
4. `let userInfo = acct.borrow<&Profile.UserProfile>(from: Profile.storageProfileStoragePath) ?? panic("Can't borrow the file from storage!");`: This line borrows a reference to the user profile resource from storage. It uses the `borrow` function on the `acct` account object to borrow a reference to the `UserProfile` resource. The `&Profile.UserProfile` type parameter specifies the type of the resource being borrowed. The `from` keyword is used to indicate the storage path from which the resource is being borrowed. If the borrowing operation fails (i.e., the resource is not found), the `??` operator is used for error handling, and the program panics with the error message âCanât borrow the file from storage!â.
5. `userInfo.updateUserName(name);`: This line calls the `updateUserName` function on the borrowed reference `userInfo` to update the userâs name with the provided `name` parameter.

Exited? Letâs spin it!

Type the new name, and hit Send. As shown in the example below!

![Remaing Example](https://i.imgur.com/WhGKu3r.png)

## Step 3 - Making our Scripts

We are in the final stretch now! We will make a script that will be able to read from the storage and show us information stored there.

cadence

```
		
			import Profile from 0x01;

pub fun main(add: Address): Profile.UserProfileInfo
{
  let publicCap = getAccount(add).getCapability(Profile.publicProfileStoragePath).borrow<&Profile.UserProfile{Profile.IUserProfilePublic}>() ?? panic("Can't find public path!");
  return publicCap.getUserProfileInfo();
}
		 
	
```

1. `import Profile from 0x01;`: This line imports the contract named `Profile` from the address `0x01`.
2. `pub fun main(add: Address): Profile.UserProfileInfo`: This line declares a public function named `main`. The function takes an `add` parameter of type `Address` and returns a value of type `Profile.UserProfileInfo`.
3. `let publicCap = getAccount(add).getCapability(Profile.publicProfileStoragePath)`
   `.borrow<&Profile.UserProfile{Profile.IUserProfilePublic}>()`
   `?? panic("Can't find public path!");`: This line retrieves the capability for accessing the public storage path of the user profile. It first calls `getAccount(add)` to get the account object associated with the provided address. Then, it calls `getCapability(Profile.publicProfileStoragePath)` on that account object to obtain the capability for the specified public storage path. The `borrow` function is used to borrow a reference to the `UserProfile` resource from the capability. The `&Profile.UserProfile{Profile.IUserProfilePublic}` type parameter specifies that the borrowed reference should conform to the `IUserProfilePublic` interface defined within the `UserProfile` resource. If the borrowing operation fails (i.e., the resource is not found or does not conform to the interface), the `??` operator is used for error handling, and the program panics with the error message âCanât find public path!â.
4. `return publicCap.getUserProfileInfo();`: This line calls the `getUserProfileInfo` function on the borrowed reference `publicCap` to retrieve the user profile information. The function returns this information as the result of the `main` function.

Fire it up! Put in the account address as `0x01` in the box and hit Execute. And you should be able to see the logs in the logs tab. As shown in the image below.

![Getting Info from Scripts example](https://i.imgur.com/Bholhx9.png)

WOW! You did it! Congratulations! Give yourself a pat in the back and buy ourself something nice to eat (please stop with those Doritos)!

![User avatar](https://i.imgur.com/Nfww3sn.png)

Author

[Memxor](https://twitter.com/memxor_)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/tutorials/user-profile/en/readme.md)



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