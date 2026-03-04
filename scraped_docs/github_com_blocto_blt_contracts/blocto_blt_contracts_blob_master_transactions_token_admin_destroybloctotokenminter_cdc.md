# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/token/admin/destroyBloctoTokenMinter.cdc

```
import "BloctoToken"

transaction {
    prepare(stakingAdmin: auth(Storage) &Account) {
        destroy stakingAdmin.storage.load<@BloctoToken.Minter>(from: /storage/bloctoTokenStakingMinter)
    }
}

```