# Source: https://academy.ecdao.org/en/snippets/fcl-account-proof


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Proving Authentication with FCL (Account Proof)

# Proving Authentication with FCL (Account Proof)


Snippet



javascript
```
		
			import {
  config,
  authenticate,
  unauthenticate,
  currentUser,
  AppUtils
} from "@onflow/fcl";
import { useEffect, useState } from "react";

// your own app identifier
const appIdentifier = "Emerald Academy";

// need a resolver function for account proofing
const resolver = async () => {
  // minimum 32-byte random nonce as hex string
  const nonce =
    "cdcdfb6611e25cb207c47f6b7e2b99c1afa28c2bb2f7f582c9df935ba90c8df2";
  return {
    appIdentifier,
    nonce
  };
};

const fclConfigInfo = {
  emulator: {
    accessNode: "http://127.0.0.1:8888",
    discoveryWallet: "http://localhost:8701/fcl/authn"
  },
  testnet: {
    accessNode: "https://rest-testnet.onflow.org",
    discoveryWallet: "https://fcl-discovery.onflow.org/testnet/authn",
    BLOCTO_FCLCRYPTO_CONTRACT_ADDRESS: "0x5b250a8a85b44a67"
  },
  mainnet: {
    accessNode: "https://rest-mainnet.onflow.org",
    discoveryWallet: "https://fcl-discovery.onflow.org/authn",
    BLOCTO_FCLCRYPTO_CONTRACT_ADDRESS: "0xdb6b70764af4ff68"
  }
};

/* TODO: Change based on your network */
const network = "mainnet"; // mainnet
/* TODO: Change based on your wallet */
// If you are verifying a Blocto wallet, you must use the
// provided `BLOCTO_FCLCRYPTO_CONTRACT_ADDRESS`.
// Otherwise, `fclCryptoContract` can be `null`.
const fclCryptoContract = null; // fclConfigInfo[network].BLOCTO_FCLCRYPTO_CONTRACT_ADDRESS;

config({
  "accessNode.api": fclConfigInfo[network].accessNode,
  "discovery.wallet": fclConfigInfo[network].discoveryWallet,
  "flow.network": network,
  // add resolver function to your config
  "fcl.accountProof.resolver": resolver
});

export default function App() {
  const [user, setUser] = useState({ loggedIn: false, addr: "" });

  // So that the user stays logged in
  // even if the page refreshes
  useEffect(() => {
    currentUser.subscribe(setUser);
  }, []);

  const verifyAccountOwnership = async () => {
    if (!user.loggedIn) {
      return;
    }
    const accountProofService = user.services.find(
      (services) => services.type === "account-proof"
    );
    console.log(accountProofService);
    const verified = await AppUtils.verifyAccountProof(
      appIdentifier,
      accountProofService.data,
      {
        fclCryptoContract
      }
    );
    console.log({ verified });
  };

  return (
    <div className="App">
      <button onClick={authenticate}>Log In</button>
      <button onClick={unauthenticate}>Log Out</button>

      {user.loggedIn ? (
        <button onClick={verifyAccountOwnership}>Verify</button>
      ) : null}

      <p>{user.loggedIn ? `Welcome, ${user.addr}!` : "Please log in."}</p>
    </div>
  );
}
		 
	
```


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Run Code](https://codesandbox.io/s/fcl-account-proof-2dmv2m?file=/src/App.js)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-account-proof/readme.md)


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



