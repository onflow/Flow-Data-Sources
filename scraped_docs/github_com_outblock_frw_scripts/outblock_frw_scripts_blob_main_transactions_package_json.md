# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/package.json

```
{
  "name": "@outblock/frw-transactions",
  "version": "0.0.5",
  "description": "Flow transactions",
  "license": "Apache-2.0",
  "type": "module",
  "source": "src/index.js",
  "main": "dist/index.js",
  "module": "dist/index.module.mjs",
  "exports": {
    "require": "./dist/index.js",
    "default": "./dist/index.module.mjs"
  },
  "scripts": {
    "build": "microbundle src/index.js",
    "start": "microbundle watch"
  },
  "peerDependencies": {
    "@onflow/config": ">=1.1.0",
    "@onflow/fcl": ">=1.4.0 || >=1.5.0 || >=1.6.0 || >=1.7.0",
    "@onflow/types": ">=1.1.0"
  },
  "devDependencies": {
    "microbundle": "0.12.0-next.8"
  },
  "publishConfig": {
    "access": "public"
  }
}
```