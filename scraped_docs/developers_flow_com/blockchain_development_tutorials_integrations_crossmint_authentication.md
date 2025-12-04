# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/crossmint/authentication

Authentication Integration Guide | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

                      + [Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)+ [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)

                          - [Authentication Integration Guide](/blockchain-development-tutorials/integrations/crossmint/authentication)- [Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)- [Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)- [Crossmint Smart Wallets](/blockchain-development-tutorials/integrations/crossmint/smart-wallets)

* * [Third-Party Integrations](/blockchain-development-tutorials/integrations)* [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)* Authentication Integration Guide

On this page

# Authentication Integration Guide

Crossmint provides a comprehensive user management solution tightly integrated with all other Crossmint products. Authenticate users with Web3 or traditional sign-in methods, with seamless wallet creation and unified identity management.

**Why this matters:**

* **Unified identity system**: Single user account across your backend and Web3 app.
* **Multiple auth methods**: Email OTP, social logins, wallet connections, and Farcaster.
* **Automatic wallet creation**: Optionally create or link wallets with user accounts.
* **Drag and drop integration**: Setup in under five minutes.

## 🎯 Available authentication methods[​](#-available-authentication-methods "Direct link to 🎯 Available authentication methods")

### 1. Email OTP authentication[​](#1-email-otp-authentication "Direct link to 1. Email OTP authentication")

Passwordless sign-in with one-time codes delivered to the user's email.

* No passwords required
* Secure and user-friendly
* Automatic account creation

### 2. Social account authentication[​](#2-social-account-authentication "Direct link to 2. Social account authentication")

Sign in with popular social platforms:

* Google
* Apple
* X (Twitter)
* And more

### 3. Farcaster integration[​](#3-farcaster-integration "Direct link to 3. Farcaster integration")

Use the [Sign In With Farcaster (SIWF) standard](https://github.com/farcasterxyz/protocol/discussions/110)

* Web3-native authentication
* Decentralized identity support

### 4. External wallet authentication[​](#4-external-wallet-authentication "Direct link to 4. External wallet authentication")

Connect with crypto wallets for Web3 authentication:

* MetaMask
* WalletConnect
* Flow wallets
* And other Web3 wallets

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Make sure you have:

**Crossmint account:**

* [Crossmint Console](https://staging.crossmint.com) account
* Client API key with authentication scopes

**React/Next.js project:**

* React 16.8+ or Next.js 13+
* TypeScript support (recommended)

**Technical knowledge:**

* Basic React hooks and state management
* Understanding of authentication flows

## Quick start[​](#quick-start "Direct link to Quick start")

### Step 1: install the SDK[​](#step-1-install-the-sdk "Direct link to Step 1: install the SDK")

`_10

npm i @crossmint/client-sdk-react-ui`

### Step 2: add crossmint providers[​](#step-2-add-crossmint-providers "Direct link to Step 2: add crossmint providers")

`_17

"use client";

_17

_17

import {

_17

CrossmintProvider,

_17

CrossmintAuthProvider,

_17

CrossmintWalletProvider

_17

} from "@crossmint/client-sdk-react-ui";

_17

_17

export function Providers({ children }: { children: React.ReactNode }) {

_17

return (

_17

<CrossmintProvider apiKey="<crossmint-client-api-key>">

_17

<CrossmintAuthProvider>

_17

{children}

_17

</CrossmintAuthProvider>

_17

</CrossmintProvider>

_17

);

_17

}`

### Step 3: create authentication component[​](#step-3-create-authentication-component "Direct link to Step 3: create authentication component")

`_39

"use client";

_39

_39

import { useAuth } from "@crossmint/client-sdk-react-ui";

_39

_39

export function AuthButton() {

_39

const { login, logout, user, jwt } = useAuth();

_39

_39

return (

_39

<div className="flex gap-4">

_39

{user == null ? (

_39

<button

_39

type="button"

_39

onClick={login}

_39

className="bg-blue-500 text-white font-bold py-2 px-4 rounded"

_39

>

_39

Login

_39

</button>

_39

) : (

_39

<button

_39

type="button"

_39

onClick={logout}

_39

className="bg-black text-white font-bold py-2 px-4 rounded border-2 border-blue-500"

_39

>

_39

Logout

_39

</button>

_39

)}

_39

_39

{/* Display user information */}

_39

<div className="user-info">

_39

<p>User ID: {user?.userId}</p>

_39

<p>Email: {user?.email ?? "None"}</p>

_39

<p>Phone: {user?.phoneNumber ?? "None"}</p>

_39

<p>Farcaster: {user?.farcaster?.username ?? "None"}</p>

_39

<p>Google: {user?.google?.displayName ?? "None"}</p>

_39

<p>JWT: {jwt}</p>

_39

</div>

_39

</div>

_39

);

_39

}`

### Environment configuration[​](#environment-configuration "Direct link to Environment configuration")

`_10

// Use environment-specific API keys

_10

const crossmintConfig = {

_10

apiKey: process.env.NODE_ENV === 'production'

_10

? process.env.CROSSMINT_PROD_API_KEY

_10

: process.env.CROSSMINT_STAGING_API_KEY,

_10

environment: process.env.NODE_ENV === 'production' ? 'production' : 'staging'

_10

};`

## Production deployment[​](#production-deployment "Direct link to Production deployment")

### 1. Create production account[​](#1-create-production-account "Direct link to 1. Create production account")

1. Create a developer account on the [Production Console](https://www.crossmint.com/signin?callbackUrl=/console).
   ![Production Console Login](/assets/images/staging-6ab5f042d30972f081aeaa1ff5142981.png)
2. Complete account verification and KYB process.

### 2. Configure production API keys[​](#2-configure-production-api-keys "Direct link to 2. Configure production API keys")

1. Create a production client API key.

Navigate to **Integrate > API Keys**

![API Keys](/assets/images/api_keys-77de82bff170cc37fc434ab3df62d7c1.png)

2. Activate required scopes:
   * `users.create`
   * `users.read`
   * `wallets.read`
   * `wallets.create`

### 3. Update environment variables[​](#3-update-environment-variables "Direct link to 3. Update environment variables")

`_10

# Production

_10

CROSSMINT_API_KEY=your_production_client_api_key

_10

CROSSMINT_ENVIRONMENT=production

_10

_10

# Staging (for testing)

_10

CROSSMINT_API_KEY=your_staging_client_api_key

_10

CROSSMINT_ENVIRONMENT=staging`

### 4. Test authentication flow[​](#4-test-authentication-flow "Direct link to 4. Test authentication flow")

`_12

// Test authentication in staging first

_12

const testAuth = async () => {

_12

const { login, user } = useAuth();

_12

_12

await login();

_12

_12

if (user) {

_12

console.log('Authentication successful:', user);

_12

// Test wallet creation

_12

await createUserWallet();

_12

}

_12

};`

## 🔧 Troubleshooting[​](#-troubleshooting "Direct link to 🔧 Troubleshooting")

### Common issues[​](#common-issues "Direct link to Common issues")

**Authentication fails:**

* Verify API key is correct.
* Check authentication scopes are activated.
* Make sure you're using the right environment (staging vs. production)

**Wallet creation fails:**

* Verify user is authenticated.
* Check wallet creation scopes.
* Ensure proper wallet configuration for Flow.

### Get Help[​](#get-help "Direct link to Get Help")

* **[Crossmint Authentication Docs](https://docs.crossmint.com/authentication/introduction)**
* **[Flow Developer Portal](https://developers.flow.com/)**

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/integrations/crossmint/authentication.md)

Last updated on **Nov 14, 2025** by **Brian Doyle**

[Previous

Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)[Next

Payment Checkout Integration](/blockchain-development-tutorials/integrations/crossmint/payment-checkout)

###### Rate this page

😞😐😊

Copy as Markdown

* [🎯 Available authentication methods](#-available-authentication-methods)
  + [1. Email OTP authentication](#1-email-otp-authentication)+ [2. Social account authentication](#2-social-account-authentication)+ [3. Farcaster integration](#3-farcaster-integration)+ [4. External wallet authentication](#4-external-wallet-authentication)* [Prerequisites](#prerequisites)* [Quick start](#quick-start)
      + [Step 1: install the SDK](#step-1-install-the-sdk)+ [Step 2: add crossmint providers](#step-2-add-crossmint-providers)+ [Step 3: create authentication component](#step-3-create-authentication-component)+ [Environment configuration](#environment-configuration)* [Production deployment](#production-deployment)
        + [1. Create production account](#1-create-production-account)+ [2. Configure production API keys](#2-configure-production-api-keys)+ [3. Update environment variables](#3-update-environment-variables)+ [4. Test authentication flow](#4-test-authentication-flow)* [🔧 Troubleshooting](#-troubleshooting)
          + [Common issues](#common-issues)+ [Get Help](#get-help)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2025 Flow Foundation. All Rights Reserved.