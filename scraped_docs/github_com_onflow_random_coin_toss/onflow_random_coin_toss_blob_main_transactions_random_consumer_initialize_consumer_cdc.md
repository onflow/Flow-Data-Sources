# Source: https://github.com/onflow/random-coin-toss/blob/main/transactions/random-consumer/initialize_consumer.cdc

```
import "RandomConsumer"

transaction {
    prepare(signer: &Account) {}

    execute {
        RandomConsumer.initializeConsumer()
    }
}
```