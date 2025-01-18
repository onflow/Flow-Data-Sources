# Source: https://academy.ecdao.org/en/snippets/find-historical-blocks


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Fetch Historical Blocks

# Fetch Historical Blocks


Snippet



Returns a specific block at block height and the 9 previous blocks.

javascript
```
		
			async function getBlocks() {
  try {
    const height = "63253147";

    const response = await fetch(
      `https://api.findlabs.io/historical/api/rest/blocks?height=${height}`
    );
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
}

getBlocks();
		 
	
```


![User avatar](/avatars/find-labs.jpg)

Author

[Find Labs](https://twitter.com/findlabs)


[Run Code](https://codesandbox.io/s/find-historical-blocks-ky689v?file=/src/index.js:0-333)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/find-historical-blocks/readme.md)


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



