# Source: https://academy.ecdao.org/en/snippets/cadence-deploy-contract


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Deploy a Contract in Cadence

# Deploy a Contract in Cadence


Snippet



cadence
```
		
			transaction(
  contractCode: String, // must be a hex string of your contract code
  contractName: String // must match the name of the contract you're deploying
) {
  prepare(signer: auth(AddContract) &Account) {
      signer.contracts.add(
          name: contractName,
          code: contractCode.decodeHex()
      )
  }
}
		 
	
```


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Run Code](https://run.ecdao.org?code=dHJhbnNhY3Rpb24oCiAgY29udHJhY3RDb2RlOiBTdHJpbmcsIC8vIG11c3QgYmUgYSBoZXggc3RyaW5nIG9mIHlvdXIgY29udHJhY3QgY29kZQogIGNvbnRyYWN0TmFtZTogU3RyaW5nIC8vIG11c3QgbWF0Y2ggdGhlIG5hbWUgb2YgdGhlIGNvbnRyYWN0IHlvdSdyZSBkZXBsb3lpbmcKKSB7CiAgcHJlcGFyZShzaWduZXI6IEF1dGhBY2NvdW50KSB7CiAgICAgIHNpZ25lci5jb250cmFjdHMuYWRkKAogICAgICAgICAgbmFtZTogY29udHJhY3ROYW1lLAogICAgICAgICAgY29kZTogY29udHJhY3RDb2RlLmRlY29kZUhleCgpCiAgICAgICkKICB9Cn0%3D&network=testnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-deploy-contract/readme.md)


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



