# Source: https://developers.flow.com/build/tools/flow-cli/flow.json/security

Security | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                      - [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                * [Initialize Configuration](/build/tools/flow-cli/flow.json/initialize-configuration)* [Configuration](/build/tools/flow-cli/flow.json/configuration)* [Manage Configuration](/build/tools/flow-cli/flow.json/manage-configuration)* [Security](/build/tools/flow-cli/flow.json/security)- [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Flow.json* Security

On this page

# Security

Managing accounts and private keys requires careful attention to security. This guide covers best practices for keeping your Flow accounts and private keys secure when using the Flow CLI.

## Security Overview[​](#security-overview "Direct link to Security Overview")

⚠️ **Critical Warning**: Never commit private keys to source control. Always use secure methods to store and manage your private keys.

The Flow CLI provides several secure options for managing private account data:

1. **File-based keys** - Store keys in separate files
2. **Environment variables** - Use system environment variables
3. **Private configuration files** - Separate sensitive config from main config
4. **Multiple config files** - Merge secure and public configurations

## File-Based Keys[​](#file-based-keys "Direct link to File-Based Keys")

Store private keys in separate files that are excluded from source control.

### Setup[​](#setup "Direct link to Setup")

1. **Create a key file** (e.g., `my-account.key`):

`_10

# Only the hex-encoded private key

_10

334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111`

2. **Add to `.gitignore`**:

`_10

# Private key files

_10

*.key

_10

*.pkey

_10

private.json

_10

.env`

3. **Configure in `flow.json`**:

`_11

{

_11

"accounts": {

_11

"my-testnet-account": {

_11

"address": "3ae53cb6e3f42a79",

_11

"key": {

_11

"type": "file",

_11

"location": "./my-account.key"

_11

}

_11

}

_11

}

_11

}`

### Benefits[​](#benefits "Direct link to Benefits")

* ✅ Keys are never stored in configuration files
* ✅ Easy to manage multiple keys
* ✅ Clear separation of concerns
* ✅ Works with all Flow CLI commands

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Use environment variables for sensitive data like private keys and addresses.

### Setup[​](#setup-1 "Direct link to Setup")

1. **Set environment variables**:

`_10

export FLOW_PRIVATE_KEY="334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_10

export FLOW_ACCOUNT_ADDRESS="3ae53cb6e3f42a79"`

2. **Reference in `flow.json`**:

`_10

{

_10

"accounts": {

_10

"my-testnet-account": {

_10

"address": "$FLOW_ACCOUNT_ADDRESS",

_10

"key": "$FLOW_PRIVATE_KEY"

_10

}

_10

}

_10

}`

3. **Use with CLI commands**:

`_10

FLOW_PRIVATE_KEY="your-key" flow project deploy`

### Benefits[​](#benefits-1 "Direct link to Benefits")

* ✅ Keys never stored in files
* ✅ Easy to manage different environments
* ✅ Works with CI/CD systems
* ✅ Can be rotated easily

## Private Configuration Files[​](#private-configuration-files "Direct link to Private Configuration Files")

Create separate configuration files for sensitive data and merge them when needed.

### Setup[​](#setup-2 "Direct link to Setup")

1. **Main configuration** (`flow.json`):

`_10

{

_10

"networks": {

_10

"testnet": "access.devnet.nodes.onflow.org:9000"

_10

},

_10

"contracts": {

_10

"MyContract": "./cadence/contracts/MyContract.cdc"

_10

}

_10

}`

2. **Private configuration** (`private.json`):

`_10

{

_10

"accounts": {

_10

"my-testnet-account": {

_10

"address": "3ae53cb6e3f42a79",

_10

"key": "334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_10

}

_10

}

_10

}`

3. **Add to `.gitignore`**:

`_10

private.json

_10

secrets.json

_10

*.private.json`

4. **Use with CLI commands**:

`_10

flow project deploy -f flow.json -f private.json`

### Benefits[​](#benefits-2 "Direct link to Benefits")

* ✅ Clear separation of public and private data
* ✅ Easy to manage multiple environments
* ✅ Can be shared safely (without private files)
* ✅ Works with all CLI commands

## Environment Files (.env)[​](#environment-files-env "Direct link to Environment Files (.env)")

Use `.env` files for local development with automatic loading by the CLI.

### Setup[​](#setup-3 "Direct link to Setup")

1. **Create `.env` file**:

`_10

# .env

_10

FLOW_PRIVATE_KEY=334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111

_10

FLOW_ACCOUNT_ADDRESS=3ae53cb6e3f42a79

_10

FLOW_NETWORK=testnet`

2. **Reference in `flow.json`**:

`_11

{

_11

"accounts": {

_11

"my-testnet-account": {

_11

"address": "$FLOW_ACCOUNT_ADDRESS",

_11

"key": "$FLOW_PRIVATE_KEY"

_11

}

_11

},

_11

"networks": {

_11

"testnet": "access.devnet.nodes.onflow.org:9000"

_11

}

_11

}`

3. **Add to `.gitignore`**:

`_10

.env

_10

.env.local

_10

.env.*.local`

### Benefits[​](#benefits-3 "Direct link to Benefits")

* ✅ Automatic loading by CLI
* ✅ Easy local development
* ✅ Can have different files for different environments
* ✅ Standard practice for many tools

## Multiple Configuration Files[​](#multiple-configuration-files "Direct link to Multiple Configuration Files")

Merge multiple configuration files for complex setups.

### Priority Order[​](#priority-order "Direct link to Priority Order")

When using multiple files, they are merged in order:

1. **Left to right** - Files specified first have lowest priority
2. **Later files override** - Properties in later files take precedence
3. **Non-overlapping properties** - Are combined from all files

### Example[​](#example "Direct link to Example")

`_10

flow project deploy -f flow.json -f private.json -f local.json`

**Result**: `local.json` overrides `private.json`, which overrides `flow.json`

### Use Cases[​](#use-cases "Direct link to Use Cases")

* **Development**: `flow.json` + `dev-private.json`
* **Staging**: `flow.json` + `staging-private.json`
* **Production**: `flow.json` + `prod-private.json`

## Security Best Practices[​](#security-best-practices "Direct link to Security Best Practices")

### 1. Never Commit Private Keys[​](#1-never-commit-private-keys "Direct link to 1. Never Commit Private Keys")

`_10

# Always add these to .gitignore

_10

*.key

_10

*.pkey

_10

private.json

_10

secrets.json

_10

.env

_10

.env.local

_10

*.private.json`

### 2. Use Different Keys for Different Environments[​](#2-use-different-keys-for-different-environments "Direct link to 2. Use Different Keys for Different Environments")

* **Development**: Use testnet keys
* **Staging**: Use separate testnet keys
* **Production**: Use mainnet keys with highest security

### 3. Rotate Keys Regularly[​](#3-rotate-keys-regularly "Direct link to 3. Rotate Keys Regularly")

* Generate new keys periodically
* Update configuration files
* Test with new keys before switching

### 4. Limit Key Permissions[​](#4-limit-key-permissions "Direct link to 4. Limit Key Permissions")

* Use keys with minimal required permissions
* Consider using different keys for different operations
* Monitor key usage

### 5. Secure Key Storage[​](#5-secure-key-storage "Direct link to 5. Secure Key Storage")

* Use hardware security modules (HSMs) for production
* Consider cloud key management services
* Encrypt key files when possible

## Common Security Mistakes[​](#common-security-mistakes "Direct link to Common Security Mistakes")

### ❌ Don't Do This[​](#-dont-do-this "Direct link to ❌ Don't Do This")

`_10

// flow.json - NEVER do this

_10

{

_10

"accounts": {

_10

"my-account": {

_10

"address": "3ae53cb6e3f42a79",

_10

"key": "334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_10

}

_10

}

_10

}`

### ✅ Do This Instead[​](#-do-this-instead "Direct link to ✅ Do This Instead")

`_12

// flow.json - Safe to commit

_12

{

_12

"accounts": {

_12

"my-account": {

_12

"address": "3ae53cb6e3f42a79",

_12

"key": {

_12

"type": "file",

_12

"location": "./my-account.key"

_12

}

_12

}

_12

}

_12

}`

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Environment Variables Not Loading[​](#environment-variables-not-loading "Direct link to Environment Variables Not Loading")

Check that your environment variables are set:

`_10

echo $FLOW_PRIVATE_KEY`

### Key File Not Found[​](#key-file-not-found "Direct link to Key File Not Found")

Verify the key file path in your configuration:

`_10

ls -la ./my-account.key`

### Multiple Config Files Not Merging[​](#multiple-config-files-not-merging "Direct link to Multiple Config Files Not Merging")

Check the order of your `-f` flags:

`_10

# Correct order (left to right, later overrides earlier)

_10

flow config add account -f flow.json -f private.json`

## Related Commands[​](#related-commands "Direct link to Related Commands")

* [`flow config add`](/build/tools/flow-cli/flow.json/manage-configuration) - Add configuration items securely
* [`flow project deploy`](/build/tools/flow-cli/deployment/deploy-project-contracts) - Deploy with secure configuration
* [`flow accounts create`](/build/tools/flow-cli/accounts/create-accounts) - Create accounts securely

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/flow.json/security.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Manage Configuration](/build/tools/flow-cli/flow.json/manage-configuration)[Next

Get Block](/build/tools/flow-cli/get-flow-data/get-blocks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Security Overview](#security-overview)* [File-Based Keys](#file-based-keys)
    + [Setup](#setup)+ [Benefits](#benefits)* [Environment Variables](#environment-variables)
      + [Setup](#setup-1)+ [Benefits](#benefits-1)* [Private Configuration Files](#private-configuration-files)
        + [Setup](#setup-2)+ [Benefits](#benefits-2)* [Environment Files (.env)](#environment-files-env)
          + [Setup](#setup-3)+ [Benefits](#benefits-3)* [Multiple Configuration Files](#multiple-configuration-files)
            + [Priority Order](#priority-order)+ [Example](#example)+ [Use Cases](#use-cases)* [Security Best Practices](#security-best-practices)
              + [1. Never Commit Private Keys](#1-never-commit-private-keys)+ [2. Use Different Keys for Different Environments](#2-use-different-keys-for-different-environments)+ [3. Rotate Keys Regularly](#3-rotate-keys-regularly)+ [4. Limit Key Permissions](#4-limit-key-permissions)+ [5. Secure Key Storage](#5-secure-key-storage)* [Common Security Mistakes](#common-security-mistakes)
                + [❌ Don't Do This](#-dont-do-this)+ [✅ Do This Instead](#-do-this-instead)* [Troubleshooting](#troubleshooting)
                  + [Environment Variables Not Loading](#environment-variables-not-loading)+ [Key File Not Found](#key-file-not-found)+ [Multiple Config Files Not Merging](#multiple-config-files-not-merging)* [Related Commands](#related-commands)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.