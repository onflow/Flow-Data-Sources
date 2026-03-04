# Source: https://github.com/Flowtyio/flowty-drops/blob/main/contracts/FlowtyPricers.cdc

```
import "FlowtyDrops"
import "FlowToken"

/*
This contract contains implementations of the FlowtyDrops.Pricer interface.
You can use these, or any custom implementation for the phases of your drop.
*/
access(all) contract FlowtyPricers {

    /*
    The FlatPrice Pricer implementation has a set price and token type. Every mint is the same cost regardless of
    the number minter, or what address is minting
    */
    access(all) struct FlatPrice: FlowtyDrops.Pricer {
        access(all) var price: UFix64
        access(all) let paymentTokenType: String

        access(all) view fun getPrice(num: Int, paymentTokenType: Type, minter: Address?): UFix64 {
            return self.price * UFix64(num)
        }

        access(all) view fun getPaymentTypes(): [Type] {
            return [CompositeType(self.paymentTokenType)!]
        }

        access(Mutate) fun setPrice(price: UFix64) {
            self.price = price
        }

        init(price: UFix64, paymentTokenType: Type) {
            self.price = price
            self.paymentTokenType = paymentTokenType.identifier
        }
    }

    /*
    The Free Pricer can be used for a free mint, it has no price and always marks its payment type as @FlowToken.Vault
    */
    access(all) struct Free: FlowtyDrops.Pricer {
        access(all) fun getPrice(num: Int, paymentTokenType: Type, minter: Address?): UFix64 {
            return 0.0
        }

        access(all) fun getPaymentTypes(): [Type] {
            return [Type<@FlowToken.Vault>()]
        }
    }
}
```