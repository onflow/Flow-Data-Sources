# Source: https://academy.ecdao.org/en/snippets/nbatopshot-read-user-moments


















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Snippets](/en/snippets)
Get all User NBATopShot Moments

# Get all User NBATopShot Moments


Snippet



cadence
```
		
			import TopShot from 0x0b2a3299cc857e29

access(all) fun main(user: Address): [MomentData] {
  let account = getAccount<auth(Storage) &Account>(user)
  let momentCollection = account.storage.borrow<&TopShot.Collection>(from: /storage/MomentCollection)
                            ?? panic("User does not have a TopShot Collection")

  let answer: [MomentData] = []

  // Iterate through all of the user's moments
  for id in momentCollection.getIDs() {
    // borrow the nft reference
    let moment: &TopShot.NFT = momentCollection.borrowMoment(id: id)!
    // get extra metadata about the specific "play"
    let play: {String: String} = TopShot.getPlayMetaData(playID: moment.data.playID)!

    let momentData: MomentData = MomentData(
      id: moment.id,
      s: moment.data.serialNumber,
      p: play["FullName"] ?? "N/A",
      t: play["TeamAtMoment"] ?? "N/A",
      d: play["DateOfMoment"] ?? "N/A",
      pc: play["PlayCategory"] ?? "N/A",
      sn: TopShot.getSetName(setID: moment.data.setID)!
    )
    answer.append(momentData)
  }

  return answer
}

// define our own struct to neatly organize
// data so we can return an array of it
access(all) struct MomentData {
  access(all) let id: UInt64
  access(all) let serialNumber: UInt32
  access(all) let player: String
  access(all) let team: String
  access(all) let date: String
  access(all) let playCategory: String
  access(all) let setName: String

  init(id: UInt64, s: UInt32, p: String, t: String, d: String, pc: String, sn: String) {
    self.id = id
    self.serialNumber = s
    self.player = p
    self.team = t
    self.date = d
    self.playCategory = pc
    self.setName = sn
  }
}
		 
	
```


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Run Code](https://run.ecdao.org/?code=aW1wb3J0IFRvcFNob3QgZnJvbSAweDBiMmEzMjk5Y2M4NTdlMjkKCnB1YiBmdW4gbWFpbih1c2VyOiBBZGRyZXNzKTogW01vbWVudERhdGFdIHsKICBsZXQgYXV0aEFjY291bnQ6IEF1dGhBY2NvdW50ID0gZ2V0QXV0aEFjY291bnQodXNlcikKICBsZXQgbW9tZW50Q29sbGVjdGlvbiA9IGF1dGhBY2NvdW50LmJvcnJvdzwmVG9wU2hvdC5Db2xsZWN0aW9uPihmcm9tOiAvc3RvcmFnZS9Nb21lbnRDb2xsZWN0aW9uKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgPz8gcGFuaWMoIlVzZXIgZG9lcyBub3QgaGF2ZSBhIFRvcFNob3QgQ29sbGVjdGlvbiIpCgogIGxldCBhbnN3ZXI6IFtNb21lbnREYXRhXSA9IFtdCgogIGZvciBpZCBpbiBtb21lbnRDb2xsZWN0aW9uLmdldElEcygpIHsKICAgIGxldCBtb21lbnQ6ICZUb3BTaG90Lk5GVCA9IG1vbWVudENvbGxlY3Rpb24uYm9ycm93TW9tZW50KGlkOiBpZCkhCiAgICBsZXQgcGxheToge1N0cmluZzogU3RyaW5nfSA9IFRvcFNob3QuZ2V0UGxheU1ldGFEYXRhKHBsYXlJRDogbW9tZW50LmRhdGEucGxheUlEKSEKCiAgICBsZXQgbW9tZW50RGF0YTogTW9tZW50RGF0YSA9IE1vbWVudERhdGEoCiAgICAgIGlkOiBtb21lbnQuaWQsCiAgICAgIHM6IG1vbWVudC5kYXRhLnNlcmlhbE51bWJlciwKICAgICAgcDogcGxheVsiRnVsbE5hbWUiXSA%2FPyAiTi9BIiwgCiAgICAgIHQ6IHBsYXlbIlRlYW1BdE1vbWVudCJdID8%2FICJOL0EiLCAKICAgICAgZDogcGxheVsiRGF0ZU9mTW9tZW50Il0gPz8gIk4vQSIsIAogICAgICBwYzogcGxheVsiUGxheUNhdGVnb3J5Il0gPz8gIk4vQSIsCiAgICAgIHNuOiBUb3BTaG90LmdldFNldE5hbWUoc2V0SUQ6IG1vbWVudC5kYXRhLnNldElEKSEKICAgICkKICAgIGFuc3dlci5hcHBlbmQobW9tZW50RGF0YSkKICB9CgogIHJldHVybiBhbnN3ZXIKfQoKcHViIHN0cnVjdCBNb21lbnREYXRhIHsKICBwdWIgbGV0IGlkOiBVSW50NjQKICBwdWIgbGV0IHNlcmlhbE51bWJlcjogVUludDMyCiAgcHViIGxldCBwbGF5ZXI6IFN0cmluZwogIHB1YiBsZXQgdGVhbTogU3RyaW5nCiAgcHViIGxldCBkYXRlOiBTdHJpbmcKICBwdWIgbGV0IHBsYXlDYXRlZ29yeTogU3RyaW5nCiAgcHViIGxldCBzZXROYW1lOiBTdHJpbmcKCiAgaW5pdChpZDogVUludDY0LCBzOiBVSW50MzIsIHA6IFN0cmluZywgdDogU3RyaW5nLCBkOiBTdHJpbmcsIHBjOiBTdHJpbmcsIHNuOiBTdHJpbmcpIHsKICAgIHNlbGYuaWQgPSBpZAogICAgc2VsZi5zZXJpYWxOdW1iZXIgPSBzCiAgICBzZWxmLnBsYXllciA9IHAKICAgIHNlbGYudGVhbSA9IHQKICAgIHNlbGYuZGF0ZSA9IGQKICAgIHNlbGYucGxheUNhdGVnb3J5ID0gcGMKICAgIHNlbGYuc2V0TmFtZSA9IHNuCiAgfQp9&network=mainnet&args=eyJ1c2VyIjoiMHg1NjgwZmEwNzY0MmI1MDJhIn0%3D)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/snippets/nbatopshot-read-user-moments/readme.md)


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



