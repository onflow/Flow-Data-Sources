# Source: https://academy.ecdao.org/en/snippets/find-historical-tx-data


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Fetch Historical Transaction Data

# Fetch Historical Transaction Data


Snippet



javascript
```
		
			async function getTransactionData() {
  try {
    const transactionId =
      "752db233c432285125c966ac39536d14d016211a82f01eef76be4f732ed0bfb5";
    const response = await fetch(
      `https://api.findlabs.io/historical/api/rest/transaction?id=${transactionId}`
    );
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
}

getTransactionData();
		 
	
```


![User avatar](/avatars/find-labs.jpg)

Author

[Find Labs](https://twitter.com/findlabs)


[Run Code](https://codesandbox.io/s/find-historical-tx-data-qh2vk3)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/find-historical-tx-data/readme.md)


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



