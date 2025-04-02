# Source: https://academy.ecdao.org/en/snippets/fcl-create-account

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Create an Account with FCL

# Create an Account with FCL

Snippet

javascript

```
		
			import { mutate, config, tx, unauthenticate } from '@onflow/fcl';

config({
	'accessNode.api': 'https://rest-testnet.onflow.org',
	'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn'
});

async function createAccount() {
	// replace with your public key
	const publicKey =
		'fc1701c73cab29991b8f3c902672a22c13dbfbfc99054cfe47e0de64afc521bfd7b4250e20cae6e296819539712b32166f46c1e6d74427ff1c08422b0f600e98';
	const txHash = await mutate({
		cadence: `
    transaction (publicKey: String) {
    prepare(signer: auth(BorrowValue) &Account) {
      let key = PublicKey(
        publicKey: publicKey.decodeHex(),
        signatureAlgorithm: SignatureAlgorithm.ECDSA_P256
      )

      let account = Account(payer: signer)

      account.keys.add(
        publicKey: key,
        hashAlgorithm: HashAlgorithm.SHA3_256,
        weight: 1000.0
      )
    }
  }
    `,
		args: (arg, t) => [arg(publicKey, t.String)],
		limit: 1000
	});

	console.log({ txHash });
	const txResult = await tx(txHash).onceExecuted();
	console.log({ txResult });
	const { events } = txResult;

	// we need to find system event `flow.AccountCreated` in list of events
	const event = events.find((event) => event.type.includes('AccountCreated'));
	// then we can extract address from it
	const accountAddress = event.data.address;
	console.log({ accountAddress });
}
		 
	
```

![User avatar](https://pbs.twimg.com/profile_images/1476344533172510722/5Bka7etN_400x400.jpg)

Author

[Max Starka](https://twitter.com/MaxStalker)

[Run Code](https://codesandbox.io/s/fcl-create-account-2y4w7z?file=/src/index.js:0-1396)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/fcl-create-account/readme.md)



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