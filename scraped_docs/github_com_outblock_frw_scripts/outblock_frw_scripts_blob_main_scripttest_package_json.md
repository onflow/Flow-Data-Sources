# Source: https://github.com/Outblock/FRW-scripts/blob/main/scriptTest/package.json

```
{
    "name": "@outblock/frw-scriptTest",
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
        "@outblock/frw-scripts": "workspace:*"
    },
    "devDependencies": {
        "microbundle": "0.12.0-next.8"
    }
}
```