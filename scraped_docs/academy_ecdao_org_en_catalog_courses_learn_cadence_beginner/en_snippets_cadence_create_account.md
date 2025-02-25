# Source: https://academy.ecdao.org/en/snippets/cadence-create-account

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Create an Account in Cadence

# Create an Account in Cadence

Snippet

cadence

```
		
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
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://run.ecdao.org?code=dHJhbnNhY3Rpb24ocHVibGljS2V5OiBTdHJpbmcpIHsKICAgIHByZXBhcmUoc2lnbmVyOiBBdXRoQWNjb3VudCkgewogICAgICAgIGxldCBrZXkgPSBQdWJsaWNLZXkoCiAgICAgICAgICAgIHB1YmxpY0tleTogcHVibGljS2V5LmRlY29kZUhleCgpLAogICAgICAgICAgICBzaWduYXR1cmVBbGdvcml0aG06IFNpZ25hdHVyZUFsZ29yaXRobS5FQ0RTQV9QMjU2CiAgICAgICAgKQoKICAgICAgICBsZXQgYWNjb3VudCA9IEF1dGhBY2NvdW50KHBheWVyOiBzaWduZXIpCgogICAgICAgIGFjY291bnQua2V5cy5hZGQoCiAgICAgICAgICAgIHB1YmxpY0tleToga2V5LAogICAgICAgICAgICBoYXNoQWxnb3JpdGhtOiBIYXNoQWxnb3JpdGhtLlNIQTNfMjU2LAogICAgICAgICAgICB3ZWlnaHQ6IDEwMDAuMAogICAgICAgICkKICAgIH0KfQ%3D%3D&network=testnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-create-account/readme.md)



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