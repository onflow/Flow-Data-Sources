# Source: https://developers.flow.com/tutorials/ai-plus-flow/agentkit-flow-guide

Build Custom AI Agents on Flow with AgentKit | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [AI Plus Flow](/tutorials/ai-plus-flow)

  + [Use Cursor AI](/tutorials/ai-plus-flow/cursor)
  + [Use ChatGPT](/tutorials/ai-plus-flow/chatgpt)
  + [Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources)
  + [Using AgentKit on Flow](/tutorials/ai-plus-flow/agentkit-flow-guide)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

* [AI Plus Flow](/tutorials/ai-plus-flow)
* Using AgentKit on Flow

On this page

# Getting Started with AgentKit on Flow

AgentKit is an ecosystem-agnostic modular developer toolkit that lets you rapidly build, deploy, and iterate on AI agents using pre-configured environments and ready-to-use templates.

In this guide, you'll set up your own custom agent running on **Flow's EVM-compatible testnet**, powered by **Langchain** and **Anthropic's Claude** LLM.

---

## Quickstart - Starting From Scratch[​](#quickstart---starting-from-scratch "Direct link to Quickstart - Starting From Scratch")

Open your terminal and run:

`_10

npm create onchain-agent@latest`

Follow the interactive setup:

1. Type `y` to proceed, then press **Enter**.
2. Select your framework: **Langchain**
3. Choose your network: **EVM**
4. Set the custom Chain ID:
   * `545` for **Flow Testnet**
   * `747` for **Flow Mainnet**
5. JSON-RPC endpoint:

   `_10

   https://testnet.evm.nodes.onflow.org`

---

## Project Setup[​](#project-setup "Direct link to Project Setup")

Once your scaffold is ready:

`_10

cd onchain-agent

_10

npm install`

Now open the project in your preferred IDE (e.g. Cursor).

### Environment Configuration[​](#environment-configuration "Direct link to Environment Configuration")

1. Create a `.env.local` file (or edit the one generated).
2. Add your API keys (we'll use **Anthropic** here).

> You can also use OpenAI, DeepSeek, or any other supported LLM.

### Get Your Anthropic API Key[​](#get-your-anthropic-api-key "Direct link to Get Your Anthropic API Key")

* Head to [Anthropic Console](https://console.anthropic.com/dashboard)
* Create an account and **purchase credits**
* Click **Create Key**, name it, and copy the API key
* Add this to your `.env.local`:

`_10

ANTHROPIC_API_KEY=your_api_key_here`

### Wallet Setup with MetaMask[​](#wallet-setup-with-metamask "Direct link to Wallet Setup with MetaMask")

1. Add [Flow Testnet](https://developers.flow.com/evm/using) to MetaMask
2. Use the [Faucet](https://faucet.flow.com/fund-account) to fund your wallet
3. Get your private key:
   * Click the `...` menu in MetaMask > **Account Details**
   * Enter your password, copy the private key
4. Add it to `.env.local`:

`_10

PRIVATE_KEY=your_private_key_here`

Your `.env.local` should look something like this:

`_10

PRIVATE_KEY=...

_10

ANTHROPIC_API_KEY=...`

Now run:

`_10

mv .env.local .env

_10

npm run dev`

Visit your local server:

`_10

http://localhost:3000`

---

## Configure Your LLM[​](#configure-your-llm "Direct link to Configure Your LLM")

If your agent doesn't respond yet — no worries! You still need to configure your **LLM and client libraries**.

### Choose a Model[​](#choose-a-model "Direct link to Choose a Model")

Langchain supports many LLMs ([full list here](https://python.langchain.com/docs/integrations/llms/)).

For this example, we'll use **Anthropic's `claude-3-5-haiku-20241022`**, a lightweight and affordable model. Alternatively, [DeepSeek](https://deepseek.com/) is highly recommended for budget-friendly usage.

### Update `create-agent.ts`[​](#update-create-agentts "Direct link to update-create-agentts")

Change the default model from OpenAI:

`_10

const llm = new ChatOpenAI({ model: 'gpt-4o-mini' });`

To Anthropic:

`_10

import { ChatAnthropic } from '@langchain/anthropic';

_10

_10

const llm = new ChatAnthropic({ model: 'claude-3-5-haiku-20241022' });`

Install the package:

`_10

npm install @langchain/anthropic`

---

## Configure Flow and Viem Wallet[​](#configure-flow-and-viem-wallet "Direct link to Configure Flow and Viem Wallet")

### Update the Faucet Provider Logic[​](#update-the-faucet-provider-logic "Direct link to Update the Faucet Provider Logic")

Change this:

`_10

const canUseFaucet = walletProvider.getNetwork().networkId == 'base-sepolia';`

To:

`_10

const canUseFaucet = walletProvider.getNetwork().networkId == 'flow-testnet';`

### Add Flow Context Message to Agent[​](#add-flow-context-message-to-agent "Direct link to Add Flow Context Message to Agent")

This gives your agent context about the Flow testnet:

`_16

const flowContextMessage = canUseFaucet

_16

? `

_16

You are now operating on the Flow blockchain testnet using a Viem wallet. Flow is a fast, decentralized, and

_16

developer-friendly blockchain designed for NFTs, games, and apps.

_16

_16

Key facts about Flow:

_16

- Flow uses a proof-of-stake consensus mechanism

_16

- The native token is FLOW

_16

- Flow has a unique multi-role architecture for high throughput

_16

- The testnet is EVM-compatible (works with MetaMask + Viem)

_16

- RPC URL: https://testnet.evm.nodes.onflow.org

_16

- Chain ID: 545

_16

_16

Your wallet address is \${await walletProvider.getAddress()}.

_16

`

_16

: '';`

Then inject it into the agent message modifier:

`_16

agent = createReactAgent({

_16

llm,

_16

tools,

_16

checkpointSaver: memory,

_16

messageModifier: `

_16

You are a helpful agent interacting with the Flow blockchain testnet using a Viem wallet.

_16

Flow testnet supports EVM, so you can use Ethereum-compatible tools.

_16

\${flowContextMessage}

_16

_16

Before your first action, check the wallet details. If you see a 5XX error, ask the user to try again later.

_16

If a task is unsupported, let the user know and point them to CDP SDK + AgentKit at:

_16

https://docs.cdp.coinbase.com or https://developers.flow.com.

_16

_16

Be concise, helpful, and avoid repeating tool descriptions unless asked.

_16

`,

_16

});`

---

## You're Done![​](#youre-done "Direct link to You're Done!")

You now have a working AI agent connected to Flow testnet using AgentKit!

You can send faucet tokens to your wallet and start testing smart contract interactions or on-chain workflows.

---

## Starter Project[​](#starter-project "Direct link to Starter Project")

Want to skip the setup?

> [Fork the Flow AgentKit Starter](https://github.com/Aliserag/flow-agentkit-starter)

This starter includes all necessary config to start building immediately on Flow.

---

## Adding AgentKit to an Existing Project[​](#adding-agentkit-to-an-existing-project "Direct link to Adding AgentKit to an Existing Project")

Already have a project and want to add AgentKit? Follow these steps to integrate it into your existing codebase:

### Install the Package[​](#install-the-package "Direct link to Install the Package")

Run this command in your project's root directory:

`_10

npm install onchain-agent@latest`

This will:

* Download and install the latest version of the `onchain-agent` package
* Add it to the dependencies section of your `package.json`
* Update your `node_modules` folder accordingly

### Configure Environment[​](#configure-environment "Direct link to Configure Environment")

1. Create or update your `.env` file with the necessary API keys:

`_10

PRIVATE_KEY=your_wallet_private_key

_10

ANTHROPIC_API_KEY=your_anthropic_api_key

_10

# Or other LLM API keys`

2. Configure your RPC endpoints for Flow:

`_10

FLOW_TESTNET_RPC_URL=https://testnet.evm.nodes.onflow.org

_10

FLOW_MAINNET_RPC_URL=https://mainnet.evm.nodes.onflow.org`

### Integrate AgentKit in Your Code[​](#integrate-agentkit-in-your-code "Direct link to Integrate AgentKit in Your Code")

Import and configure AgentKit in your application:

`_28

// Import AgentKit components

_28

import { createReactAgent, ChatAnthropic } from 'onchain-agent';

_28

import { createWalletClient, http, createPublicClient } from 'viem';

_28

_28

// Set up your Flow wallet provider

_28

const walletClient = createWalletClient({

_28

transport: http('https://testnet.evm.nodes.onflow.org'),

_28

chain: {

_28

id: 545, // Flow Testnet

_28

name: 'Flow Testnet',

_28

},

_28

account: yourPrivateKey,

_28

});

_28

_28

// Configure the LLM

_28

const llm = new ChatAnthropic({

_28

model: 'claude-3-5-haiku-20241022',

_28

});

_28

_28

// Create your agent

_28

const agent = createReactAgent({

_28

llm,

_28

tools: yourSelectedTools,

_28

// Additional configuration

_28

});

_28

_28

// Use the agent in your application

_28

// ...`

### Add Specialized Tools (Optional)[​](#add-specialized-tools-optional "Direct link to Add Specialized Tools (Optional)")

To add specialized blockchain tools to your agent:

`_19

import { viem, ViemToolConfig } from 'onchain-agent';

_19

_19

// Configure Viem tools for Flow

_19

const viemTools = viem.createTools({

_19

chain: {

_19

id: 545,

_19

name: 'Flow Testnet',

_19

},

_19

transport: http('https://testnet.evm.nodes.onflow.org'),

_19

} as ViemToolConfig);

_19

_19

// Add these tools to your agent

_19

const agent = createReactAgent({

_19

llm,

_19

tools: [

_19

...viemTools,

_19

// Other tools

_19

],

_19

});`

---

## Resources[​](#resources "Direct link to Resources")

* [AgentKit Docs](https://docs.cdp.coinbase.com/agentkit)
* [Flow EVM Guide](https://developers.flow.com/evm/using)
* [Langchain LLM Integrations](https://python.langchain.com/docs/integrations/llms/)
* [Anthropic Model Comparison](https://docs.anthropic.com/en/docs/about-claude/models/all-models#model-comparison-table)

---

Happy hacking on Flow!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/ai-plus-flow/agentkit-flow-guide.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

Flow Data Sources](/tutorials/ai-plus-flow/flow-data-sources)[Next

Token Launch](/tutorials/token-launch)

###### Rate this page

😞😐😊

* [Quickstart - Starting From Scratch](#quickstart---starting-from-scratch)
* [Project Setup](#project-setup)
  + [Environment Configuration](#environment-configuration)
  + [Get Your Anthropic API Key](#get-your-anthropic-api-key)
  + [Wallet Setup with MetaMask](#wallet-setup-with-metamask)
* [Configure Your LLM](#configure-your-llm)
  + [Choose a Model](#choose-a-model)
  + [Update `create-agent.ts`](#update-create-agentts)
* [Configure Flow and Viem Wallet](#configure-flow-and-viem-wallet)
  + [Update the Faucet Provider Logic](#update-the-faucet-provider-logic)
  + [Add Flow Context Message to Agent](#add-flow-context-message-to-agent)
* [You're Done!](#youre-done)
* [Starter Project](#starter-project)
* [Adding AgentKit to an Existing Project](#adding-agentkit-to-an-existing-project)
  + [Install the Package](#install-the-package)
  + [Configure Environment](#configure-environment)
  + [Integrate AgentKit in Your Code](#integrate-agentkit-in-your-code)
  + [Add Specialized Tools (Optional)](#add-specialized-tools-optional)
* [Resources](#resources)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.