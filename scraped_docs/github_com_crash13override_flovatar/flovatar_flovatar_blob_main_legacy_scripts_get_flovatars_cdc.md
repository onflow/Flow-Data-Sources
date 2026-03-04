# Source: https://github.com/flovatar/flovatar/blob/main/legacy/scripts/get_flovatars.cdc

```
// Get All the Flovatars for a Specific Address
import Flovatar from "../contracts/Flovatar.cdc"

pub fun main(address:Address) : [Flovatar.FlovatarData] {
    return Flovatar.getFlovatars(address: address)
}

```