# Source: https://academy.ecdao.org/en/snippets/fcl-passing-dictionary-arg

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Pass a Dictionary Arg to Cadence in FCL

# Pass a Dictionary Arg to Cadence in FCL

Snippet

javascript

```
		
			import { config, query } from '@onflow/fcl';

config({
	'accessNode.api': 'https://rest-testnet.onflow.org'
});

async function executeScript() {
	const result = await query({
		cadence: `
    access(all) fun main(test: {String: UFix64}): {String: UFix64} {
      return test
    }
    `,
		args: (arg, t) => [
			arg(
				[
					{ key: 'Jacob', value: '10.5' },
					{ key: 'Bjartek', value: '3.1' },
					{ key: 'Austin', value: '0.17' }
				],
				t.Dictionary({ key: t.String, value: t.UFix64 })
			)
		]
	});

	console.log({ result });
}

executeScript();
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://codesandbox.io/s/fcl-dictionary-arg-zd789r?file=/src/index.js:0-596)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-passing-dictionary-arg/readme.md)



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