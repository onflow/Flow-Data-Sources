# Source: https://academy.ecdao.org/en/cadence-by-example/21-capability-controllers

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Capability Controllers

# Capability Controllers

When we store data to an account at a storage path, that data is only accessible by the account owner.

To make data stored at a storage path available to a public path, we can issue (create) a new capability and publish it. That capability can then be fetched by anyone and gives them access to that public data.

We can restrict capabilities by restricting certain access, so we only share certain data / functions we want the accessor of our capability to have.

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

   access(all) fun createNFT(name: String): @NFT {
      let nft <- create NFT(name: name)
      return <- nft
   }

}
		 
	
```

cadence

```
		
			// Transaction file: store_nft.cdc
import Test from 0x01

transaction(name: String) {

   prepare(signer: auth(SaveValue, Capabilities) &Account) {
      let nft <- Test.createNFT(name: name)
      // moves the NFT resource into storage at `/storage/MyNFT`
      signer.storage.save(<- nft, to: /storage/MyNFT)

      // Creates a capability at `/public/MyPublicNFT` for anyone to borrow.
      // 
      // Notice we link the type: `&Test.NFT`, which is not authorized to call `changeName`.
      // We don't want other people changing our NFT's name! :)
      let cap = signer.capabilities.issue<&Test.NFT>(/storage/MyNFT)
      signer.capabilities.publish(cap, /public/MyPublicNFT)
   }

   execute {}
}
		 
	
```

cadence

```
		
			// Script file: read_nft.cdc
import Test from 0x01

access(all) fun main(owner: Address): NFTData {
   // use the built-in `getAccount` function to get 
   // the owner's `&Account`
   let ownerAccount: &Account = getAccount(owner)

   let nftCap: Capability<&Test.NFT> = ownerAccount
                                          .capabilities
                                          .get<&Test.NFT>(/public/MyPublicNFT) 
                                          ?? panic("Not a valid NFT capability.")
   let nftRef: &Test.NFT = nftCap.borrow() ?? panic("Not a valid NFT reference.")

   /*
      NOTE: Instead of getting the capability and borrowing it, we can reduce this
      to 1 line by using `capabilities.borrow` directly:

      let nftRef: &Test.NFT = ownerAccount
                              .capabilities
                              .borrow<&Test.NFT>(/public/MyPublicNFT) 
                              ?? panic("Not a valid NFT reference.")
   */

   return NFTData(nftRef.id, nftRef.name)
}

access(all) struct NFTData {
   access(all) let id: UInt64
   access(all) let name: String

   init(_ i: UInt64, _ n: String) {
      self.id = i
      self.name = n
   }
}
		 
	
```

[Entitlements](/en/cadence-by-example/20-entitlements)
[Random](/en/cadence-by-example/22-random)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/21-capability-controllers.md)



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