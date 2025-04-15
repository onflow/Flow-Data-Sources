# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/admin/create_set_and_play_struct.cdc

```
import TopShot from 0xTOPSHOTADDRESS

transaction() {
    
    prepare(acct: auth(BorrowValue) &Account) {

        let metadata: {String: String} = {"PlayType": "Shoe becomes untied"}

        let newPlay = TopShot.Play(metadata: metadata)

        let newSet = TopShot.SetData(name: "Sneaky Sneakers")
    }
}
```