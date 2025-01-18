# Source: https://github.com/onflow/flow-nft/blob/master/.github/workflows/release.yml

```
name: "🚀 release"

on:
  push:
    branches:
      - master

concurrency: ${{ github.workflow }}-${{ github.ref }}

jobs:
  release:
    name: 🚀 release
    runs-on: ubuntu-latest
    steps:
      - name: 📚 checkout
```