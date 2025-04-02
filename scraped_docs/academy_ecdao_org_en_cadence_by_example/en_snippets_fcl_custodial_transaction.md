# Source: https://academy.ecdao.org/en/snippets/fcl-custodial-transaction

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Execute a Transaction w/ FCL (Custodial Wallet)

# Execute a Transaction w/ FCL (Custodial Wallet)

Snippet

javascript

```
		
			import { config, mutate, authz } from '@onflow/fcl';

// NOTE: `authz` is automatically configured
// to be the signed in user through FCL discovery (blocto, lilico, etc)
//
// this is NOT for sending a tx using a non-custodial
// account (private key)

config({
	'accessNode.api': 'https://rest-testnet.onflow.org',
	'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn'
});

async function sendTransaction(x, y) {
	const transactionId = await mutate({
		cadence: `
    transaction(x: Int, y: Int) {
      prepare(signer: &Account) {

      }

      execute {
        // do nothing
      }
    }
    `,
		args: (arg, t) => [arg(x, t.Int), arg(y, t.Int)],
		// the person paying for the tx
		payer: authz,
		// the person proposing the tx (uses their public key to send the tx)
		proposer: authz,
		// the person authorizing the tx (gets put as the `signer` in prepare phase)
		authorizations: [authz]
	});

	console.log({ transactionId });
}

sendTransaction('3', '5');
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://codesandbox.io/s/fcl-custodial-transaction-f862wz)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-custodial-transaction/readme.md)



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