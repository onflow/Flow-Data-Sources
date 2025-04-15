# Source: https://github.com/onflow/flow-nft/blob/master/transactions/scripts/get_contract_storage_path.cdc

```
import "MetadataViews"
import "ViewResolver"

access(all) fun main(addr: Address, name: String): StoragePath? {
    let t = Type<MetadataViews.NFTCollectionData>()
    let borrowedContract = getAccount(addr).contracts.borrow<&{ViewResolver}>(name: name)
        ?? panic("Could not borrow ViewResolver reference to the contract. Make sure the provided contract name "
                  .concat(name).concat(" and address ").concat(addr.toString()).concat(" are correct!"))

    let view = borrowedContract.resolveContractView(resourceType: nil, viewType: t)
    if view == nil {
        return nil
    }

    let cd = view! as! MetadataViews.NFTCollectionData
    return cd.storagePath
}

```