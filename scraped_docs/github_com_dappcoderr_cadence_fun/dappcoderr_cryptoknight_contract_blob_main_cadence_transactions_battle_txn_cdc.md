# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/cadence/transactions/battle.txn.cdc

```
// Import the CryptoKnight contract
import CryptoKnight from "../contracts/CryptoKnight.cdc"

// This transaction triggers a battle between two CryptoKnight NFTs owned by different users
transaction(userA: Address, userAKnightId: UInt64, userB: Address, userBKnightId: UInt64) {

    prepare(signer: &Account) {
        // The prepare phase is included but not used in this transaction
        // No action is needed from the signer directly
        // You can uncomment the line below if you want to run battle logic during preparation
        // CryptoKnight.battle(userA: userA, userAKnight: userAKnightId, userB: userB, userBKnight: userBKnightId)
    }

    execute {
        // Call the battle function from the CryptoKnight contract
        // This will compare the XP of the two knights and update win/loss and XP accordingly
        CryptoKnight.battle(userA: userA, userAKnight: userAKnightId, userB: userB, userBKnight: userBKnightId)
    }
}

```