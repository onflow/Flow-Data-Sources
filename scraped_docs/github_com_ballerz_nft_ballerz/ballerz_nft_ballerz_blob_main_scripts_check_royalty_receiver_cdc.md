# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/scripts/check_royalty_receiver.cdc

```
import "FungibleToken"

// Reports whether the given addresses have working FungibleToken.Receiver
// capabilities at /public/dapperUtilityCoinReceiver and /public/flowTokenReceiver.
// Used to validate that a wallet can actually receive royalty payouts from
// the Gaia contract's MetadataViews.Royalties view.

access(all) struct ReceiverCheck {
    access(all) let address: Address
    access(all) let dapperReceiverWorks: Bool
    access(all) let dapperReceiverType: String
    access(all) let flowReceiverWorks: Bool
    access(all) let flowReceiverType: String

    init(address: Address, dw: Bool, dt: String, fw: Bool, ft: String) {
        self.address = address
        self.dapperReceiverWorks = dw
        self.dapperReceiverType = dt
        self.flowReceiverWorks = fw
        self.flowReceiverType = ft
    }
}

access(all) fun main(addresses: [Address]): [ReceiverCheck] {
    let results: [ReceiverCheck] = []
    for addr in addresses {
        let acct = getAccount(addr)

        let dapperCap = acct.capabilities.get<&{FungibleToken.Receiver}>(/public/dapperUtilityCoinReceiver)
        let dapperWorks = dapperCap.check()
        let dapperType = dapperCap.borrow()?.getType()?.identifier ?? "<not borrowable>"

        let flowCap = acct.capabilities.get<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)
        let flowWorks = flowCap.check()
        let flowType = flowCap.borrow()?.getType()?.identifier ?? "<not borrowable>"

        results.append(ReceiverCheck(
            address: addr,
            dw: dapperWorks,
            dt: dapperType,
            fw: flowWorks,
            ft: flowType
        ))
    }
    return results
}

```