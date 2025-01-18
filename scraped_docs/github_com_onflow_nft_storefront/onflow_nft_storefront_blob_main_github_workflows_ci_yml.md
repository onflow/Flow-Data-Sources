# Source: https://github.com/onflow/nft-storefront/blob/main/.github/workflows/ci.yml

```
name: CI

on:
  - push
  - pull_request

jobs:
  V2-Integration-Tests:
    name: NFTStorefront V2 Integration Tests
    timeout-minutes: 10
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        submodules: "true"
    - name: Set up Go
      uses: actions/setup-go@v3
      with:
        go-version: 1.20
    - name: Install Flow CLI
      run: sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
    - name: Run tests
      run: flow test -f ./flow.testing.json --cover --covercode="contracts/NFTStorefrontV2.cdc" ./test/NFTStorefrontV2_test.cdc
  V2-Integration-Tests:
    name: NFTStorefront V1 Integration Tests
    timeout-minutes: 10
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        submodules: "true"
    - name: Set up Go
      uses: actions/setup-go@v3
      with:
        go-version: 1.20
    - name: Install Flow CLI
      run: sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
    - name: Run tests
      run: flow test -f ./flow.testing.json --cover --covercode="contracts/NFTStorefront.cdc" ./test/NFTStorefrontV1_test.cdc


```