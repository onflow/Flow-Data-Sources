# Source: https://github.com/onflow/flow-ft/blob/master/flow.json

```
{
  "contracts": {
    "FungibleToken": {
      "source": "./contracts/FungibleToken.cdc",
      "aliases": {
        "emulator": "0xee82856bf20e2aa6",
        "testing": "0x0000000000000007",
        "testnet": "0x9a0766d93b6608b7",
        "mainnet": "0xf233dcee88fe0abe"
      }
    },
    "FungibleTokenSwitchboard": {
      "source": "./contracts/FungibleTokenSwitchboard.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000007",
        "mainnet": "0xf233dcee88fe0abe",
        "testnet": "0x9a0766d93b6608b7"
      }
    },
    "FungibleTokenMetadataViews": {
      "source": "./contracts/FungibleTokenMetadataViews.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000007",
        "mainnet": "0xf233dcee88fe0abe",
        "testnet": "0x9a0766d93b6608b7"
      }
    },
    "ExampleToken": {
      "source": "./contracts/ExampleToken.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000007"
      }
    },
    "MaliciousToken": {
        "source": "./contracts/test/MaliciousToken.cdc",
        "aliases": {
          "testing": "0x0000000000000007"
        }
      },
    "PrivateReceiverForwarder": {
      "source": "./contracts/utility/PrivateReceiverForwarder.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000007"
      }
    },
    "TokenForwarding": {
      "source": "./contracts/utility/TokenForwarding.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testnet": "0x51ea0e37c27a1f1a",
        "testing": "0x0000000000000007"
      }
    },
    "ViewResolver": {
      "source": "./contracts/utility/ViewResolver.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000001",
        "mainnet": "0x1d7e57aa55817448",
        "testnet": "0x631e88ae7f1d7c20"
      }
    },
    "Burner": {
      "source": "./contracts/utility/Burner.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000007",
        "testnet": "0x9a0766d93b6608b7"
      }
    },
    "NonFungibleToken": {
      "source": "./contracts/utility/NonFungibleToken.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000001",
        "mainnet": "0x1d7e57aa55817448",
        "testnet": "0x631e88ae7f1d7c20"
      }
    },
    "MetadataViews": {
      "source": "./contracts/utility/MetadataViews.cdc",
      "aliases": {
        "emulator": "0xf8d6e0586b0a20c7",
        "testing": "0x0000000000000001",
        "mainnet": "0x1d7e57aa55817448",
        "testnet": "0x631e88ae7f1d7c20"
      }
    },
    "FlowToken": {
      "source": "./contracts/utility/FlowToken.cdc",
      "aliases": {
        "testing": "0x0000000000000003",
        "emulator": "0x0ae53cb6e3f42a79",
        "testnet": "0x7e60df042a9c0868",
        "mainnet": "0x1654653399040a61"
      }
    },
    "FiatToken": {
      "source": "./contracts/utility/USDC/FiatToken.cdc",
      "aliases": {
        "testnet": "0xa983fecbed621163",
        "mainnet": "0x1654653399040a61"
      }
    },
    "LostAndFound": {
      "source": "./contracts/utility/L&F/LostAndFound.cdc",
      "aliases": {
        "testnet": "0xbe4635353f55bbd4",
        "mainnet": "0x473d6a2c37eab5be"
      }
    }
  },
  "networks": {
    "emulator": "127.0.0.1:3569",
    "testing": "127.0.0.1:3569",
    "testnet": "access.devnet.nodes.onflow.org:9000",
    "mainnet": "access.mainnet.nodes.onflow.org:9000"
  },
  "accounts": {
    "emulator-account": {
      "address": "0xf8d6e0586b0a20c7",
      "key": "1a05ba433be5af2988e814d1e4fa08f1574140e6cb5649a861cc6377718c51be"
    }
  },
  "deployments": {
    "emulator": {
      "emulator-account": [
        "FungibleToken",
        "NonFungibleToken",
        "MetadataViews",
        "FungibleTokenMetadataViews",
        "FungibleTokenSwitchboard",
        "TokenForwarding"
      ]
    }
  }
}

```