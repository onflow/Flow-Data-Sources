# Source: https://academy.ecdao.org/en/snippets/cadence-random

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Random Number in Cadence

# Random Number in Cadence

Snippet

Note that while the `revertibleRandom` function is secure & unpredictable (you can read more about it [here](https://developers.flow.com/cadence/language/built-in-functions#revertiblerandom)), you must be cautious about how you use this.

Users who authorize/sign transactions can always abort transactions if they do not like the outcome. For example, a coin flip game where a user signs a transaction to flip a coin and win $. They can simply abort the transaction if the end result is a loss.

Thus, this function should be used where aborting a transaction is not a concern (ex. an Admin running an on-chain raffle).

cadence

```
		
			// gets a number between min & max
access(all) fun main(min: UInt64, max: UInt64): UInt64 {
  let randomNumber: UInt64 = revertibleRandom<UInt64>()
  return (randomNumber % (max + 1 - min)) + min
}
		 
	
```

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Run Code](https://run.ecdao.org?code=cHViIGZ1biBtYWluKG1pbjogVUludDY0LCBtYXg6IFVJbnQ2NCk6IFVJbnQ2NCB7CiAgbGV0IHJhbmRvbU51bWJlcjogVUludDY0ID0gcmV2ZXJ0aWJsZVJhbmRvbSgpCiAgcmV0dXJuIChyYW5kb21OdW1iZXIgJSAobWF4ICsgMSAtIG1pbikpICsgbWluCn0%3D&network=mainnet&args=eyJtaW4iOjUsIm1heCI6MTB9)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-random/readme.md)



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