# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/dss-collection-nft/transactions/admin/destroy_admin_resource.cdc

```
import DSSCollection from "../../contracts/DSSCollection.cdc"


transaction() {
    let adminResource: @DSSCollection.Admin

    prepare(signer: AuthAccount) {
        self.adminResource <- signer.load<@DSSCollection.Admin>(from: DSSCollection.AdminStoragePath)
            ?? panic("Could not load admin resource")
    }

    execute {
        destroy self.adminResource
    }
}
```