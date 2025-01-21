# Source: https://github.com/onflow/flow-core-contracts/blob/master/lib/go/templates/README.md

```
# Core Contracts Transaction Templates

This module contains transaction and script templates for the Flow core contracts,
primarly templates for staking and delegating FLOW.

## Generated manifest files

The `manifest.mainnet.json` and `testnet.mainnet.json` files declare all transaction templates
in a portable format for mainnet and testnet respectively.

To update the manifest files:

- Add your desired templates to [cmd/manifest/manifest.go](./cmd/manifest/manifest.go).
- Run `make generate` in this directory.

```