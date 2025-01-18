# Source: https://academy.ecdao.org/en/snippets/cadence-time


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Time in Cadence

# Time in Cadence


Snippet



cadence
```
		
			access(all) fun main() {
  // in seconds
  let currentTime: UFix64 = getCurrentBlock().timestamp

  // 1 minute from now
  let oneMinuteFromNow: UFix64 = currentTime + 60.0

  // 1 hour from now
  let oneHourFromNow: UFix64 = currentTime + (60.0 * 60.0)

  // 1 day from now
  let oneDayFromNow: UFix64 = currentTime + (60.0 * 60.0 * 24.0)

  // and so on...
}
		 
	
```


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Run Code](https://run.ecdao.org?code=cHViIGZ1biBtYWluKCk6IFVGaXg2NCB7CiAgLy8gaW4gc2Vjb25kcwogIGxldCBjdXJyZW50VGltZTogVUZpeDY0ID0gZ2V0Q3VycmVudEJsb2NrKCkudGltZXN0YW1wCgogIC8vIDEgbWludXRlIGZyb20gbm93CiAgbGV0IG9uZU1pbnV0ZUZyb21Ob3c6IFVGaXg2NCA9IGN1cnJlbnRUaW1lICsgNjAuMAoKICAvLyAxIGhvdXIgZnJvbSBub3cKICBsZXQgb25lSG91ckZyb21Ob3c6IFVGaXg2NCA9IGN1cnJlbnRUaW1lICsgKDYwLjAgKiA2MC4wKQoKICAvLyAxIGRheSBmcm9tIG5vdwogIGxldCBvbmVEYXlGcm9tTm93OiBVRml4NjQgPSBjdXJyZW50VGltZSArICg2MC4wICogNjAuMCAqIDI0LjApCgogIC8vIGFuZCBzbyBvbi4uLgoKICByZXR1cm4gY3VycmVudFRpbWUKfQo%3D&network=mainnet&args=e30%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/cadence-time/readme.md)


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



