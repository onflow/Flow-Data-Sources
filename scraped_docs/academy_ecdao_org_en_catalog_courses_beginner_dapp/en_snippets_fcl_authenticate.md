# Source: https://academy.ecdao.org/en/snippets/fcl-authenticate

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Authenticate using FCL

# Authenticate using FCL

Snippet

javascript

```
		
			import { config, authenticate, unauthenticate, currentUser } from "@onflow/fcl";
import { useEffect, useState } from "react";

const fclConfigInfo = {
	emulator: {
		accessNode: 'http://127.0.0.1:8888',
		discoveryWallet: 'http://localhost:8701/fcl/authn',
		discoveryAuthInclude: []
	},
	testnet: {
		accessNode: 'https://rest-testnet.onflow.org',
    discoveryWallet: 'https://fcl-discovery.onflow.org/testnet/authn',
    discoveryAuthnEndpoint: 'https://fcl-discovery.onflow.org/api/testnet/authn',
    // Adds in Dapper + Ledger
		discoveryAuthInclude: ["0x82ec283f88a62e65", "0x9d2e44203cb13051"]
	},
	mainnet: {
		accessNode: 'https://rest-mainnet.onflow.org',
    discoveryWallet: 'https://fcl-discovery.onflow.org/authn',
    discoveryAuthnEndpoint: 'https://fcl-discovery.onflow.org/api/authn',
    // Adds in Dapper + Ledger
		discoveryAuthInclude: ["0xead892083b3e2c6c", "0xe5cd26afebe62781"]
	}
};

const network = 'mainnet';

config({
  "app.detail.title": "Emerald Academy", // the name of your DApp
  "app.detail.icon": "https://academy.ecdao.org/favicon.png", // your DApps icon
  "flow.network": network,
  "accessNode.api": fclConfigInfo[network].accessNode,
  "discovery.wallet": fclConfigInfo[network].discoveryWallet,
  "discovery.authn.endpoint": fclConfigInfo[network].discoveryAuthnEndpoint,
  // adds in opt-in wallets like Dapper and Ledger
  "discovery.authn.include": fclConfigInfo[network].discoveryAuthInclude
});

export default function App() {
  const [user, setUser] = useState({ loggedIn: false, addr: "" });

  // So that the user stays logged in
  // even if the page refreshes
  useEffect(() => {
    currentUser.subscribe(setUser);
  }, []);

  return (
    <div className="App">
      <button onClick={authenticate}>Log In</button>
      <button onClick={unauthenticate}>Log Out</button>
      <p>{user.loggedIn ? `Welcome, ${user.addr}!` : "Please log in."}</p>
    </div>
  );
}
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://codesandbox.io/s/fcl-authenticate-gxr8mg)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-authenticate/readme.md)



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