# Source: https://academy.ecdao.org/en/catalog/courses/niftory/chapter1/lesson4

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Course Overview](/en/catalog/courses/niftory)

1. Niftory Concepts

[1.1 Why Niftory?](/en/catalog/courses/niftory/chapter1/lesson1)[1.2 Admin Portal](/en/catalog/courses/niftory/chapter1/lesson2)[1.3 Basic Niftory App](/en/catalog/courses/niftory/chapter1/lesson3)[1.4 Authentication](/en/catalog/courses/niftory/chapter1/lesson4)

Course Overview

[Catalog](/en/catalog)
[Course](/en/catalog/courses/niftory)
Niftory

# Chapter 1 Lesson 4 - The different types of authentication

Youâve already [built and deployed the sample app](src/lib/content/courses/niftory/en/chapter1/lesson3.md) in the last lesson so weâre going to take this time to learn more about the authentication modes that Niftory supports. This should help clarify the various ways we do things in the sample app and help you make the decision of which modes to support in your DApp.

## Authentication modes

For simple commands (generally getting data like your NFTs, Wallets, etc), you can just use your API Key, which is safe to call for any application. For privileged commands, youâll use the Client Secret or our OAuth integrations.

In our SDK samples, youâll usually see us creating a separate client for simple use-cases vs the privileged use-cases.

### Standard SDK Client

If you look at the client declaration below, youâll see we only pass the client our public API key and our public client ID. None of this is particularly sensitive info.

js

```
		
			import { EnvironmentName, NiftoryClient, NiftoryProvider } from "@niftory/sdk"
import { useMemo } from "react"
import { useWalletContext } from "../hooks/useWalletContext"

export const NiftoryClientProvider = ({ children }) => {
  const client = useMemo(() => {
    return new NiftoryClient({
      environmentName: process.env.NEXT_PUBLIC_BLOCKCHAIN_ENV as EnvironmentName,
      appId: process.env.NEXT_PUBLIC_CLIENT_ID,
      apiKey: process.env.NEXT_PUBLIC_API_KEY,
    })
  }, [])

  return <NiftoryProvider client={client}>{children}</NiftoryProvider>
}
		 
	
```

### Privileged Niftory SDK Client (API Key + Client Secret)

Some operations require more privileged authentication â for example, if any user could invoke the [transfer](https://app.gitbook.com/o/ShoAj2x7X0erlYafyocL/s/1itXKRjyFqqWGYkUXFnP/core-concepts/nfts/transferring-nfts) mutation, they would be able to transfer as many NFTs as they wanted to themselves, so we probably only want the application to be able to initiate that operation!

js

```
		
			import { EnvironmentName, NiftoryClient } from "@niftory/sdk"
let client: NiftoryClient

/**
 * Gets a NIFTORY client for use in the backend.
 * @returns A NiftorySdk client.
 */
export function getBackendNiftoryClient() {
  client =
    client ||
    new NiftoryClient({
      environmentName: process.env.NEXT_PUBLIC_BLOCKCHAIN_ENV as EnvironmentName,
      appId: process.env.NEXT_PUBLIC_CLIENT_ID,
      apiKey: process.env.NEXT_PUBLIC_API_KEY,
      clientSecret: process.env.CLIENT_SECRET,
    })

  return client
}
		 
	
```

For operations that should only be initiated from the app or app adminâs context, we support two forms of privileged authentication: (1) Backend authentication and (2) Admin authentication.

### Backend Authentication

Backend authentication amounts to your application authenticating as itself, instead of in the AppUser context.

> Backend authentication allows the App to perform any privileged operation against your applicationâs resources. *For this reason, itâs extremely important to only use this kind of authentication in your backend.*

There are two ways of doing backend authentication - using your client secret or using OAuth.

1. Client Secret: Add your client secret header into the API Call (backend only).
2. Open ID and OAuth: Authenticate using the [OAuth Client Credentials](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/) grant. Many OAuth libraries support this.

For a more detailed discussion of this, check out our official [docs](https://docs.niftory.com/home/v/api/core-concepts/authentication/privileged-authentication). We also have some handy code-snippets for you embedded in that page.

## Conclusion

That about wraps things up for us in the Niftory mini-course. With Niftory as your guide, youâre ready to embark on a fantastic voyage across the waves of the Flowverse!

## Quests

1. What are the different types of authentication you may encounter with Niftory? Which ones seem the mose suitable for your DApp?

![User avatar](https://i.imgur.com/bymjTdC.png)

Author

[Team Niftory](https://twitter.com/niftory)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/niftory/en/chapter1/lesson4.md)

[Basic Niftory App](/en/catalog/courses/niftory/chapter1/lesson3)



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