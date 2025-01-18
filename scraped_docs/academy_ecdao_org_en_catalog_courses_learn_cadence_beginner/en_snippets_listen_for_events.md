# Source: https://academy.ecdao.org/en/snippets/listen-for-events


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Listen for Events in FCL

# Listen for Events in FCL


Snippet



javascript
```
		
			import * as fcl from "@onflow/fcl";

// We need to point FCL to some access node.
// We will use Mainnet REST endpoint for this, as the contract
// we want to listen to is deployed there

fcl.config({
  "accessNode.api": "https://rest-mainnet.onflow.org",
  // we will set the poll rate for events to 3 seconds
  "fcl.eventPollRate": 3000
});

// FlowFees is the most active contract, since every transaction will
// trigger "FeesDeducted" event, so it will be easier to see that our code
// is working correctly
const contractAddress = "f919ee77447b7497";
const contractName = "FlowFees";
const eventName = "FeesDeducted";
// Event name consist of 2 or 4 parts
// 2 part event name have only system events
// For deployed contract, event should be constructed from 4 parts
// - "A" prefix, stands for "account"
// - address where contract, holding definition of event is deployed
// - contract name
// - event name
const event = `A.${contractAddress}.${contractName}.${eventName}`;

console.log(
  `Listening for event "${eventName}" from "${contractName}" deployed on account 0x${contractAddress}`
);
fcl.events(event).subscribe((eventData) => {
  console.log(eventData);
});
		 
	
```


![User avatar](https://pbs.twimg.com/profile_images/1476344533172510722/5Bka7etN_400x400.jpg)

Author

[Max Starka](https://twitter.com/MaxStalker)


[Run Code](https://codesandbox.io/s/listen-for-events-njfli3)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/listen-for-events/readme.md)


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



