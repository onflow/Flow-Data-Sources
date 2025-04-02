# Source: https://academy.ecdao.org/en/cadence-by-example/23-transaction-architecture

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Transaction Architecture

# Transaction Architecture

Transactions have 2 main stages:

1. **prepare** - to access/manipulate data inside the `signer`âs account
2. **execute** - to execute actions

To be proper, you should use the `prepare` phase to play with storage and capabilities, and leave all other actions to `execute`.

cadence

```
		
			// Transaction file: change_nft_name.cdc
import Test from 0x01

transaction(newName: String) {

   // create a local variable
   let nft: &Test.NFT

   prepare(signer: auth(BorrowValue) &Account) {
      // access account storage and set the local variable in prepare phase
      self.nft = signer.storage.borrow<&Test.NFT>(from: /storage/MyNFT) 
                           ?? panic("Signer does not have an NFT.")
   }

   execute {
      // perform all other actions in the execute phase,
      self.nft.changeName(newName: newName)
   }
}
		 
	
```

[Random](/en/cadence-by-example/22-random)
[Time](/en/cadence-by-example/24-time)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/23-transaction-architecture.md)



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