# Source: https://academy.ecdao.org/en/snippets/fcl-passing-struct-arg


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Pass a Struct Arg to Cadence in FCL

# Pass a Struct Arg to Cadence in FCL


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
    import BasicBeastsNFTStakingRewards from 0x4c74cb420f4eaa84
    
    access(all) fun main(rewardItem: BasicBeastsNFTStakingRewards.RewardItem): BasicBeastsNFTStakingRewards.RewardItem {
      return rewardItem
    }
    `,
		args: (arg, t) => [
			arg(
				{
					fields: [
						{ name: 'id', value: '10' },
						{ name: 'rewardItemTemplateID', value: '20' },
						{ name: 'timestamp', value: '10.0' },
						{ name: 'revealed', value: true }
					]
				},
				// `A.${contract address without the 0x}.${contract name}.${struct name}`
				t.Struct(`A.4c74cb420f4eaa84.BasicBeastsNFTStakingRewards.RewardItem`, [
					{ name: 'id', value: t.UInt32 },
					{ name: 'rewardItemTemplateID', value: t.UInt32 },
					{ name: 'timestamp', value: t.UFix64 },
					{ name: 'revealed', value: t.Bool }
				])
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




[Run Code](https://codesandbox.io/s/fcl-struct-arg-lp6yqq?file=/src/index.js:283-311)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-passing-struct-arg/readme.md)


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



