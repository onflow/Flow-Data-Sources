# Source: https://github.com/IncrementFi/Swap/blob/main/src/transactions/factory/deploy_pair_template.cdc

```
import FlowToken from "../../contracts/tokens/FlowToken.cdc"

/// deploy code copied by a deployed contract
transaction(pairTemplateCode: String) {
    prepare(deployAccount: auth(AddContract) &Account) {
        let token0Vault <- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>())
        let token1Vault <- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>())
        deployAccount.contracts.add(name: "SwapPair", code: pairTemplateCode.utf8, token0Vault: <-token0Vault, token1Vault: <-token1Vault)
    }
}
```