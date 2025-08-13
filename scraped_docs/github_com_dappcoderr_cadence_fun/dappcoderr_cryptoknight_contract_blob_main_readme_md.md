# Source: https://github.com/DappCoderr/CryptoKnight-Contract/blob/main/README.md

# 🛡️ CryptoKnight

**CryptoKnight** is an educational project designed to help developers learn [Cadence](https://developers.flow.com/cadence) — the resource-oriented smart contract language on the [Flow blockchain](https://www.flow.com/). By building and experimenting with a simple NFT-based battle game, you'll gain hands-on experience with core blockchain concepts like account storage, resource management, capabilities, and the Flow NFT standard.

Whether you're a complete beginner or a seasoned developer, **CryptoKnight** offers an engaging way to sharpen your Cadence skills and develop your own crypto games on Flow.

---

## 🗂️ Project Structure

Here's a quick overview of the project structure:

```
.
├── cadence/              # Cadence smart contract code
│   ├── contracts/        # All main and standard contracts (e.g., CryptoKnight, NFT standards, MetadataViews, ViewResolver)
│   ├── scripts/          # Read-only Cadence scripts
│   ├── transactions/     # State-changing Cadence transactions
│
└── flow.json             # Flow project config (like package.json)
```

## 🚀 Getting Started

You can try out and test Cadence code using the [Flow Playground](https://play.flow.com/). It allows you to run contracts, transactions, and scripts in a sandbox environment.

### 🛠️ To Run Locally:

1. **Install the Flow CLI**
   Follow instructions at [Flow CLI Install Guide](https://developers.flow.com/tools/flow-cli/install)

2. **Clone this repository**:

   ```bash
   git clone https://github.com/your-username/CryptoKnight.git
   cd CryptoKnight
   ```

3. **Start the Flow emulator**:

   ```bash
   flow emulator
   ```

4. **Deploy the contracts**:

   ```bash
   flow project deploy
   ```

5. **Interact with the contracts**:

   ```bash
   flow transactions send ./cadence/transactions/setup_account.cdc

   flow transactions send ./cadence/transactions/mintKnight.cdc "Knight 1" 0

   flow scripts execute ./cadence/scripts/checkCollection.cdc

   flow scripts execute ./cadence/scripts/getKnightIDs.cdc
   ```

---

### 🌐 To Use on Testnet:

1. Generate Flow account keys:

   ```bash
   flow keys generate
   ```

2. Go to the [Flow Testnet Faucet](https://faucet.flow.com/create-account) and create a new testnet account using your **public key**.

3. Update the `flow.json` file:

   - Add the new **testnet address** and **private key** under the `accounts` section.
   - Ensure the `deployments` section includes `testnet`.

4. Deploy and interact with contracts:

   ```bash
   flow transactions send ./cadence/transactions/setup_account.cdc --network=testnet --signer testnet

   flow transactions send ./cadence/transactions/mintKnight.cdc --network=testnet --signer testnet "Sean" 1

   flow scripts execute ./cadence/scripts/get_totalSupply.cdc --network=testnet
   ```

For more details, refer to the [Flow CLI deployment guide](https://developers.flow.com/tools/flow-cli/deployment/deploy-project-contracts).

## ⚙️ How to Use This Repository

There are **two main ways** you can use this repository:

### 1. **Learn Cadence**

Use this repo as a guided example while learning Cadence:

- Explore `/contracts` to study resource-oriented programming
- Modify and experiment with `/transactions` and `/scripts` to deepen your understanding.
- Use the Flow Playground or CLI to test changes.

### 2. **Build Your Own Game**

Use this as a starter template:

- Fork the repo
- Customize the `CryptoKnight.cdc` contract to suit your game mechanics.
- Use or extend the React frontend in the `/web` directory to create your own dApp.

## 👤 Created By

**CryptoKnight** is a Flow Developer Grant project built by [**DC**](https://x.com/dappcoder_), a Flow Dev Ambassador and smart contract engineer from India. Our mission is to make Cadence education accessible, engaging, and beginner-friendly — while empowering you to build your own blockchain applications across domains like Games, DeFi, RWAs, NFTs, DAOs, and more.

Let’s bring some fun to smart contract development on Flow! 🧙‍♂️⚔️
