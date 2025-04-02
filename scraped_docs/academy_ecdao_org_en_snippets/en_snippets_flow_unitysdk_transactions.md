# Source: https://academy.ecdao.org/en/snippets/flow-unitysdk-transactions

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Send Transactions using Unity SDK

# Send Transactions using Unity SDK

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

public class Transaction()
{
  private void Start()
  {
    StartCoroutine(CallTransaction());
  }

  private IEnumerator CallTransaction()
  {
    var txResponse = Transactions.SubmitAndWaitUntilSealed
    (
      Cadence.Instance.yourTransactionAssetName.text, //Cadence.Instance is a Singleton Script, to learn more check out Cadence Setup using UnitySDK Snippet.
      //Parameters to the transaction example
      Convert.ToCadence((string)USER_WALLET_ADDRESS, "Address"), //Address Example
      Convert.ToCadence((System.UInt64)YOUR_NUMBER, "UInt64"), //UInt64 Example 
      Convert.ToCadence((decimal)YOUR_NUMBER, "UFix64"), //UFix64 Example 
    );

    yield return new WaitUntil(() => txResponse.IsCompleted);
    var txResult = txResponse.Result;

    if (txResult.Error != null)
    {
      //Handle Errors Here
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

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/flow-unitysdk-transactions/readme.md)



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