# Source: https://academy.ecdao.org/en/cadence-by-example/13-structs
















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Cadence by Example](/en/cadence-by-example)
Structs

# Structs

You can define your own structs that have data and functions inside of them.

They are useful for grouping together related data.

Structs can be defined inside contracts or scripts. A struct defined in a contract can be created anywhere.

cadence
```
		
			// Contract file: Art.cdc
// Deployed to 0x01
access(all) contract Art {

   // this will act as an 'id' for
   // new art pieces
   access(all) var totalArtPieces: Int
   access(all) let artPieces: {Int: ArtPiece}

   access(all) struct ArtPiece {
      access(all) let id: Int
      access(all) let name: String
      access(all) let artLink: String
      access(all) let hoursWorkedOn: Int

      // Like contracts, structs (and later - resources) 
      // must have an `init` function to initialzie their variables.
      init(id: Int, name: String, artLink: String, hoursWorkedOn: Int) {
         self.id = id
         self.name = name
         self.artLink = artLink
         self.hoursWorkedOn = hoursWorkedOn
      }
   }

   access(all) fun uploadArt(name: String, artLink: String, hoursWorkedOn: Int) {
      let id: Int = Art.totalArtPieces
      let newArtPiece = ArtPiece(id: id, name: name, artLink: artLink, hoursWorkedOn: hoursWorkedOn)
      // store the new art piece, mapped to its `id`
      self.artPieces[id] = newArtPiece
      // increment the amount of art pieces by one
      Art.totalArtPieces = Art.totalArtPieces + 1
   }

   init() {
      self.totalArtPieces = 0
      self.artPieces = {}
   }
}
		 
	
```

cadence
```
		
			// Transaction file: create_art_piece.cdc
import Art from 0x01

transaction(name: String, artLink: String, hoursWorkedOn: Int) {

   prepare(signer: &Account) {}

   execute {
      Art.uploadArt(name: name, artLink: artLink, hoursWorkedOn: hoursWorkedOn)
   }
}
		 
	
```

cadence
```
		
			// Script file: read_art_piece.cdc
import Art from 0x01

// Returns an object that holds `ArtPiece` data.
// If the art piece with `id` does not exist, returns nil.
access(all) fun main(id: Int): Art.ArtPiece? {
   return Art.artPieces[id]
}
		 
	
```


[Optional Binding](/en/cadence-by-example/12-optional-binding)
[Resources](/en/cadence-by-example/14-resources)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/cadence-by-example/en/13-structs.md)

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



