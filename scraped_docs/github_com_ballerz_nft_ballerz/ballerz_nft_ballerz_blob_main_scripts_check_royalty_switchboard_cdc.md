# Source: https://github.com/Ballerz-NFT/Ballerz/blob/main/scripts/check_royalty_switchboard.cdc

```
import "FungibleToken"
import "FungibleTokenSwitchboard"

// which tokens the account's generic receiver at /public/GenericFTReceiver
// accepts, by vault type identifier. empty when there is no switchboard

access(all) fun main(address: Address): [String] {
    let out: [String] = []
    if let receiver = getAccount(address).capabilities
        .borrow<&{FungibleToken.Receiver}>(FungibleTokenSwitchboard.ReceiverPublicPath) {
        for t in receiver.getSupportedVaultTypes().keys {
            out.append(t.identifier)
        }
    }
    return out
}

```