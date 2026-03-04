# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/get_drop_summary.cdc

```
import "DropTypes"

access(all) fun main(nftTypeIdentifier: String, dropID: UInt64, minter: Address?, quantity: Int?, paymentIdentifier: String?): DropTypes.DropSummary? {
    return DropTypes.getDropSummary(
        nftTypeIdentifier: nftTypeIdentifier,
        dropID: dropID,
        minter: minter,
        quantity: quantity,
        paymentIdentifiers: paymentIdentifier != nil ? [paymentIdentifier!]: []
    )
}
```