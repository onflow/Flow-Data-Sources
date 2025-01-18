# Source: https://academy.ecdao.org/en/snippets/dynamic-import-contract


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Dynamically Import a Contract

# Dynamically Import a Contract


Snippet



Your contract must implement a contract interface in order to be imported. In this case, weâre borrowing a contract that implements the `NonFungibleToken` contract interface.

You can only access fields/functions present in the contract interface.

cadence
```
		
			import NonFungibleToken from 0x1d7e57aa55817448

access(all) fun main(contractAddress: Address, contractName: String) {
  let importedContract = getAccount(contractAddress).contracts.borrow<&{NonFungibleToken}>(name: contractName)
                    ?? panic("This contract does not exist in this account.")

  // this part isn't important, but just shows how you can then use it
  let emptyCollection <- importedContract.createEmptyCollection(nftType: Type<@{NonFungibleToken.NFT}>())
  destroy emptyCollection
}
		 
	
```


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Run Code](https://run.ecdao.org?code=aW1wb3J0IE5vbkZ1bmdpYmxlVG9rZW4gZnJvbSAweDFkN2U1N2FhNTU4MTc0NDgKCnB1YiBmdW4gbWFpbihjb250cmFjdEFkZHJlc3M6IEFkZHJlc3MsIGNvbnRyYWN0TmFtZTogU3RyaW5nKTogVUludDY0IHsKICBsZXQgY29udHJhY3QgPSBnZXRBY2NvdW50KGNvbnRyYWN0QWRkcmVzcykuY29udHJhY3RzLmJvcnJvdzwmTm9uRnVuZ2libGVUb2tlbj4obmFtZTogY29udHJhY3ROYW1lKQogICAgICAgICAgICAgICAgICAgID8%2FIHBhbmljKCJUaGlzIGNvbnRyYWN0IGRvZXMgbm90IGV4aXN0IGluIHRoaXMgYWNjb3VudC4iKQoKICByZXR1cm4gY29udHJhY3QudG90YWxTdXBwbHkKfQ%3D%3D&network=mainnet&args=eyJjb250cmFjdEFkZHJlc3MiOiIweDJkNGMzY2FmZmJlYWI4NDUiLCJjb250cmFjdE5hbWUiOiJGTE9BVCJ9)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/dynamic-import-contract/readme.md)


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



