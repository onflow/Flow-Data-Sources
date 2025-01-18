# Source: https://academy.ecdao.org/en/snippets/flow-unitysdk-cadence-setup


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Cadence Setup using Unity SDK

# Cadence Setup using Unity SDK


Snippet



Before you get to this step, make sure youâve downloaded Flow UnitySDK from the Unity Asset Store and installed it from the package manager.
Then put your .cdc files in a folder, we will soon assign them.

cs
```
		
			public class Cadence()
{
  public static Cadence Instance { get; private set; }

  [Header("Contracts")]
  public CadenceContractAsset yourContractOneName; //Assign it from the inspector
  public CadenceContractAsset yourContractTwoName; //Assign it from the inspector

  [Header("Transactions")]
  public CadenceTransactionAsset yourTransactionOneName; //Assign it from the inspector
  public CadenceTransactionAsset yourTransactionTwoName; //Assign it from the inspector

  [Header("Scripts")]
  public CadenceScriptAsset yourScriptOneName; //Assign it from the inspector
  public CadenceScriptAsset yourScriptTwoName; //Assign it from the inspector

  void Awake()
  {
    if (Instance != null && Instance != this) Destroy(this);
    else Instance = this;
  }
}
		 
	
```


![User avatar](https://i.imgur.com/Nfww3sn.png)

Author

[Memxor](https://twitter.com/memxor_)




[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/flow-unitysdk-cadence-setup/readme.md)


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



