# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/transactions/exampleNFT/mint_exampleNFT.cdc

```
import NonFungibleToken from 0x{{.NonFungibleToken}}
import ExampleNFT from 0x{{.ExampleNFT}}

transaction(recipient: Address) {

    let minter: &ExampleNFT.NFTMinter

    prepare(signer: AuthAccount) {
        self.minter = signer
            .borrow<&ExampleNFT.NFTMinter>(from: ExampleNFT.MinterStoragePath)!
    }

    execute {
        let receiver = getAccount(recipient)
            .getCapability(ExampleNFT.CollectionPublicPath)!
            .borrow<&{NonFungibleToken.CollectionPublic}>()!

        self.minter.mintNFT(recipient: receiver)
    }
}

```