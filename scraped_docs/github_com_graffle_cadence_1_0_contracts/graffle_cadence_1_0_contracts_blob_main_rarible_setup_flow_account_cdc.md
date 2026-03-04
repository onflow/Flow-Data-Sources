# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/rarible/setup-flow-account.cdc

```
import NonFungibleToken from "NonFungibleToken"
import MetadataViews from "MetadataViews"
import FungibleToken from "FungibleToken"
import FlowToken from "FlowToken"

transaction() {
		prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
			if acct.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault) == nil {
					// Create a new flowToken Vault and put it in storage
					acct.storage.save(<-FlowToken.createEmptyVault(), to: /storage/flowTokenVault)

					// Create a public capability to the Vault that only exposes
					// the deposit function through the Receiver interface
					let vaultCap = acct.capabilities.storage.issue<&FlowToken.Vault>(
							/storage/flowTokenVault
					)

					acct.capabilities.publish(
							vaultCap,
							at: /public/flowTokenReceiver
					)

					// Create a public capability to the Vault that only exposes
					// the balance field through the Balance interface
					let balanceCap = acct.capabilities.storage.issue<&FlowToken.Vault>(
							/storage/flowTokenBalance
					)

					acct.capabilities.publish(
							balanceCap,
							at: /public/usdcFlowMetadata
					)
			}

    }
    execute {

    }
}
```