# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/FlowtyAddressVerifiers.cdc

```
import "FlowtyDrops"

/*
This contract contains implementations of the FlowtyDrops.AddressVerifier struct interface
*/
access(all) contract FlowtyAddressVerifiers {
    /*
    The AllowAll AddressVerifier allows any address to mint without any verification
    */
    access(all) struct AllowAll: FlowtyDrops.AddressVerifier {
        access(all) var maxPerMint: Int

        access(all) view fun canMint(addr: Address, num: Int, totalMinted: Int, data: {String: AnyStruct}): Bool {
            return num <= self.maxPerMint
        }

        access(all) view fun getMaxPerMint(addr: Address?, totalMinted: Int, data: {String: AnyStruct}): Int? {
            return self.maxPerMint
        }

        access(Mutate) fun setMaxPerMint(_ value: Int) {
            self.maxPerMint = value
        }

        init(maxPerMint: Int) {
            pre {
                maxPerMint > 0: "maxPerMint must be greater than 0"
            }

            self.maxPerMint = maxPerMint
        }
    }

    /*
    The AllowList Verifier only lets a configured set of addresses participate in a drop phase. The number
    of mints per address is specified to allow more granular control of what each address is permitted to do.
    */
    access(all) struct AllowList: FlowtyDrops.AddressVerifier {
        access(self) let allowedAddresses: {Address: Int}

        access(all) view fun canMint(addr: Address, num: Int, totalMinted: Int, data: {String: AnyStruct}): Bool {
            if let allowedMints = self.allowedAddresses[addr] {
                return allowedMints >= num + totalMinted
            }

            return false
        }

        access(all) view fun remainingForAddress(addr: Address, totalMinted: Int): Int? {
            if let allowedMints = self.allowedAddresses[addr] {
                return allowedMints - totalMinted
            }
            return nil
        }

        access(all) view fun getMaxPerMint(addr: Address?, totalMinted: Int, data: {String: AnyStruct}): Int? {
            return addr != nil ? self.remainingForAddress(addr: addr!, totalMinted: totalMinted) : nil
        }

        access(Mutate) fun setAddress(addr: Address, value: Int) {
            self.allowedAddresses[addr] = value
        }

        access(Mutate) fun removeAddress(addr: Address) {
            self.allowedAddresses.remove(key: addr)
        }

        init(allowedAddresses: {Address: Int}) {
            self.allowedAddresses = allowedAddresses
        }
    }
}
```