# Source: https://academy.ecdao.org/en/snippets/flow-unitysdk-scripts

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Execute Scripts using Unity SDK

# Execute Scripts using Unity SDK

Snippet

cs

```
		
			using UnityEngine;
using DapperLabs.Flow.Sdk;
using DapperLabs.Flow.Sdk.Unity;
using DapperLabs.Flow.Sdk.Crypto;
using DapperLabs.Flow.Sdk.WalletConnect;
using System.Threading.Tasks;
using DapperLabs.Flow.Sdk.DataObjects;
using System.Collections.Generic;

public class Scripts()
{
  private void Start()
  {
    StartCoroutine(ExecuteScripts());
  }

  private IEnumerator ExecuteScripts()
  {
    var scpRespone = scriptsExecutionAccount.ExecuteScript  //We assigned the scriptsExecutionAccount while setting up Flow in Unity.
    (                                                       //To learn how checkout the Setup and Authentication Snippet.
      Cadence.Instance.yourScriptAssetName.text,  //Cadence.Instance is a Singleton Script, to learn more check out Cadence Setup using UnitySDK Snippet.
      //Parameters to the script exmaple
      Convert.ToCadence((string)USER_WALLET_ADDRESS, "Address"), //Address Example
      Convert.ToCadence((System.UInt64)YOUR_NUMBER, "UInt64"), //UInt64 Example 
      Convert.ToCadence((decimal)YOUR_NUMBER, "UFix64"), //UFix64 Example 
    );

    yield return new WaitUntil(() => scpRespone.IsCompleted);
    var scpResult = scpRespone.Result;

    if (scpResult.Error != null)
    {
      //Handle Failure Here
      yield break;
    }
    else
    {
      //Handle Success Here
      yield break;
    }
  }
}
		 
	
```

![User avatar](https://i.imgur.com/Nfww3sn.png)

Author

[Memxor](https://twitter.com/memxor_)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/flow-unitysdk-scripts/readme.md)



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