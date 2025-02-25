# Source: https://academy.ecdao.org/en/snippets/flow-unitysdk-setup-and-authenticate

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Setup and Authenticate using Unity SDK

# Setup and Authenticate using Unity SDK

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

public class WalletManager()
{
  public GameObject qrCodeCustomPrefab;
  public GameObject walletSelectCustomPrefab;
  public FlowControl.Account scriptsExecutionAccount;

  private async void Start()
  {
    FlowConfig flowConfig = new()
    {
      NetworkUrl = FlowConfig.TESTNETURL,
      Protocol = FlowConfig.NetworkProtocol.HTTP
    };

    FlowSDK.Init(flowConfig);
    IWallet walletProvider = new WalletConnectProvider();

    walletProvider.Init(new WalletConnectConfig
    {
      ProjectId = "YOUR_WALLETCONNECT_ID",
      ProjectName = "YOUR_PROJECT_NAME",
      ProjectDescription = "YOUR_PROJECT_DESCRIPTION",
      ProjectIconUrl = "YOUR_PROJECT_ICON_URL",
      ProjectUrl = "YOUR_PROJECT_URL",
      QrCodeDialogPrefab = qrCodeCustomPrefab,
      WalletSelectDialogPrefab = walletSelectCustomPrefab
    });

    FlowSDK.RegisterWalletProvider(walletProvider);

    scriptsExecutionAccount = new()
    {
      GatewayName = "Flow Testnet"
    };

    await AuthenticateWithWallet();
  }

  private async Task AuthenticateWithWallet()
  {
    await FlowSDK.GetWalletProvider().Authenticate("", (string flowAddress) =>
    {
      //Handle your success here
    }, () =>
    {
      //Handle your failure here
      Debug.LogError("Authentication failed.");
    });
  }
}
		 
	
```

![User avatar](https://i.imgur.com/Nfww3sn.png)

Author

[Memxor](https://twitter.com/memxor_)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/flow-unitysdk-setup-and-authenticate/readme.md)



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