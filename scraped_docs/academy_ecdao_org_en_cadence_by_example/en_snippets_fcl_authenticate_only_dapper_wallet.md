# Source: https://academy.ecdao.org/en/snippets/fcl-authenticate-only-dapper-wallet


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Dapper Wallet-Only Authentication using FCL

# Dapper Wallet-Only Authentication using FCL


Snippet



You can change how the Dapper Wallet login appears using the `discovery.wallet.method` field in your config. See comments below.

javascript
```
		
			import { config, authenticate, unauthenticate, currentUser } from "@onflow/fcl";
import { useEffect, useState } from "react";

// For mainnet:
config({
  "accessNode.api": "https://rest-mainnet.onflow.org",
  "discovery.wallet": "https://accounts.meetdapper.com/fcl/authn-restricted",
  "flow.network": "mainnet",
  // options for method:
  // POP/RPC: popup within the browser
  // TAB/RPC: separate tab
  // IFRAME/RPC: iframe within the tab
  "discovery.wallet.method": "TAB/RPC"
});

// For testnet:
// config({
//   "accessNode.api": "https://rest-testnet.onflow.org",
//   "discovery.wallet": "https://staging.accounts.meetdapper.com/fcl/authn-restricted",
//   "flow.network": "testnet",
//   "discovery.wallet.method": "TAB/RPC"
// });

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




[Run Code](https://codesandbox.io/s/fcl-authenticate-only-dapper-wallet-5c27py?file=/src/App.js)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-authenticate-only-dapper-wallet/readme.md)


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



