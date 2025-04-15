# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactionTest/package.json

```
{
    "name": "@outblock/frw-transactionTest",
    "version": "0.0.1",
    "description": "",
    "type": "module",
    "source": "src/index.js",
    "main": "dist/index.umd.js",
    "module": "dist/index.module.mjs",
    "scripts": {
        "build": "microbundle",
        "test": "node src/script.js"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
        "@onflow/fcl": "^1.13.4",
        "@onflow/types": ">=1.1.0",
        "@onflow/transport-http": "^1.10.5",
        "@outblock/frw-transactions": "workspace:*"
    },
    "devDependencies": {
        "microbundle": "0.12.0-next.8",
        "elliptic": "^6.5.4",
        "sha3": "^2.1.4",
        "@onflow/util-encode-key": "^0.0.2"
    }
}
```