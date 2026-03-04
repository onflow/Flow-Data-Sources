# Source: https://github.com/Flowtyio/flowty-drops/blob/main/scripts/get_drop_summaries.cdc

```
import "DropTypes"

access(all) fun main(nftTypeIdentifier: String, minter: Address?, quantity: Int?, paymentIdentifier: String?): [DropTypes.DropSummary] {
    return DropTypes.getAllDropSummaries(
        nftTypeIdentifier: nftTypeIdentifier,
        minter: minter,
        quantity: quantity,
        paymentIdentifiers: paymentIdentifier != nil ? [paymentIdentifier!] : []
    )
}
```