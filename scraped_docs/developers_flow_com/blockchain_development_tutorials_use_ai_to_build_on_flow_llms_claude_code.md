# Source: https://developers.flow.com/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code

Claude Code for Flow Development | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        + [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)

          - [Use ChatGPT](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/chatgpt)- [Use Gemini AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini)- [Claude Code Flow Guide](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code)+ [Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

            + [AI Agents](/blockchain-development-tutorials/use-AI-to-build-on-flow/agents)

              + [Flow MCP](/blockchain-development-tutorials/use-AI-to-build-on-flow/mcp)* [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Large Language Models (LLMs)](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms)* Claude Code Flow Guide

On this page

# Claude Code for Flow Development

[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) (Claude) provides an AI-powered coding assistant specifically designed for iterative, systematic development, which transforms the development experience. Unlike general-purpose AI tools, Claude breaks down tasks into manageable, incremental steps while it maintains context across your entire development lifecycle.

What makes Claude exceptionally powerful is it can maintain unlimited context windows, which allows it to understand entire codebases without the compression limitations that plague other AI coding tools. This comprehensive knowledge allows Claude to deploy multiple subagent instances that work in parallel on complex tasks, iterate continuously until optimal solutions are achieved, and maintain persistent memory of your project's architecture and coding standards across all development sessions.

## Learning objectives[​](#learning-objectives "Direct link to Learning objectives")

After you complete this guide, you'll be able to:

* Set up and configure Claude for optimal Flow blockchain development workflows.
* Implement the four-stage development methodology (Idea → Visualization → Planning → Build) for Cadence projects.
* Configure persistent project context with `CLAUDE.md` files with Flow-specific instructions and MCP tools.
* Apply iterative development practices with git-based checkpoint systems for safe blockchain development.
* Use advanced Claude features such subagents, auto-verification, and specialized debugging workflows.
* Integrate Claude with Flow CLI, FCL, and other Flow development tools for comprehensive project management.
* Create and manage team-wide development standards through shared `CLAUDE.md` configurations.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you proceed with this guide, you should have:

### Technical requirements[​](#technical-requirements "Direct link to Technical requirements")

* [Claude Code Subscription](https://claude.ai/upgrade): $200/month plan recommended for comprehensive Flow development features.
* [Flow CLI](https://developers.flow.com/tools/flow-cli): Installed and configured for emulator, testnet, and mainnet interactions.
* [Git](https://git-scm.com/downloads): Version control system for checkpoint-based development workflow.
* [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm): For Claude, FCL integration, and frontend development components.

## Claude setup and configuration[​](#claude-setup-and-configuration "Direct link to Claude setup and configuration")

### What is Claude?[​](#what-is-claude "Direct link to What is Claude?")

Claude is an AI-powered code assitant that integrated directly into your terminal. This allows you to use it in any integrated development environment (IDE) or simply from your terminal. The power of Claude comes from its ability to explain complex and large codebases, manage Git workflows, and iterate for long periods of time to accomplish a task.

Most IDEs like Cursor rely on their ability to compress the context window that is fed to agents so that their business model justifies a $20 charge while they use expensive LLM models. This naturally decreases the ability of the agents to have a comprehensive understanding of the working codebase when they manage with large or complex codebases.

This is why Claude can be so powerful, because it can include entire codebases in its context, deploy other instances of Claude to work on multiple actions in parallel, and iterate on its results in order to achieve better results.

### Installation and subscription[​](#installation-and-subscription "Direct link to Installation and subscription")

Claude requires a [subscription](https://claude.ai/upgrade) to access its full development capabilities. There are three subscription levels: Pro, Max 5x, and Max 20x.

The Pro plan is very limited, so expect it to only be sufficient for testing and experimentation.

The $200/month Max 20x plan is recommended for developers with a lot of projects or if you need to build something quickly where time is crucial. This plan grants you access to:

* Unlimited context windows for complex smart contract projects.
* Advanced subagent capabilities for parallel development tasks.
* Persistent memory across development sessions.
* Integration with MCP (Model Context Protocol) servers.
* Team collaboration features through shared configurations.

You can also use the API pricing, but we don't recommend it, since any meaningful implementation of Claude most likely requires more than $100 in API credits.

### Initial configuration[​](#initial-configuration "Direct link to Initial configuration")

To install Claude, run the following command:

`_10

npm install -g @anthropic-ai/claude-code`

After the installation process completes, navigate to your project and start Claude:

`_10

cd your-awesome-project

_10

claude`

This automatically installs the extension. Run the `/ide` command in the Claude terminal to make sure your IDE is connected to Claude. With the extension installed, click on the orange Anthropic logo on the upper right hand of the screen in order to launch Claude in a separate window.

![Claude Code Extension](/assets/images/CC_logo-bd70eeecc96271a5b8d108354cec98d7.png)

### CLAUDE.md files[​](#claudemd-files "Direct link to CLAUDE.md files")

`CLAUDE.md` files are configuration files that contain project-specific instructions and context for Claude. They allow you to define development standards, frequently used commands, and project architecture that the AI remembers across all coding sessions. They are similar to Cursor Rules, but they differ in that `CLAUDE.md` only specifies the configuration of Claude.

If you know what type of information to place in your `CLAUDE.md` file, create your primary `CLAUDE.md` file in the project root. Use the `/init` command in Claude to generate the initial structure, then customize for Flow development:

Create your Flow project with the standard directory structure:

`_15

flow-project/

_15

├── .claude/

_15

│ └── CLAUDE.md # Project-wide AI instructions

_15

├── cadence/

_15

│ ├── .claude/

_15

│ │ └── CLAUDE.md # Cadence-specific instructions

_15

│ ├── contracts/

_15

│ ├── transactions/

_15

│ └── scripts/

_15

├── frontend/

_15

│ ├── .claude/

_15

│ │ └── CLAUDE.md # Frontend-specific instructions

_15

│ └── src/

_15

├── flow.json # Flow project configuration

_15

└── package.json`

#### 3. Root CLAUDE.md configuration[​](#3-root-claudemd-configuration "Direct link to 3. Root CLAUDE.md configuration")

Place `CLAUDE.md` in the root file sets the instructions you want Claude to do frequently, such as:

* Bash commands you want to run frequently.
* Files it should really know about when it makes changes or big architectural decisions.
* MCP servers.

This file is great to share across your team so you set it once and everyone has the same extended functionality.

**Team Configuration Setup**:

`` _38

_38

# Flow Project AI assistant configuration

_38

_38

## Project overview

_38

_38

This is a Flow blockchain application with Cadence smart contracts and FCL frontend integration.

_38

_38

## Team-wide development standards

_38

_38

- MCP servers standardized across development environments.

_38

- Git workflow and commit message standards enforced.

_38

- Follow official Flow documentation patterns.

_38

- Use incremental, checkpoint-based development.

_38

- Test on emulator before testnet deployment.

_38

- Implement proper resource handling with @ and & syntax

_38

- Follow MetadataViews standards for NFT projects.

_38

_38

## Frequently used commands

_38

_38

- `flow emulator start` - Start local development environment.

_38

- `flow project deploy --network emulator` - Deploy contracts locally.

_38

- `flow transactions send ./cadence/transactions/example.cdc --network emulator` - Execute transactions locally.

_38

- `npm run dev` - Start frontend development server.

_38

_38

## Key files to reference

_38

_38

- `flow.json` - Project configuration and contract deployments.

_38

- `cadence/contracts/` - Smart contract implementations.

_38

- `frontend/src/config.js` - FCL configuration and contract addresses.

_38

_38

## MCP servers

_38

_38

- Use flow-mcp to read blockchain data, manage accounts, check balances, and interact with native contracts.

_38

- Use flow-defi-mcp to check token prices, swap tokens on decentralized exchanges, and interact with ERC20 tokens.

_38

_38

## Architecture notes

_38

_38

Document your specific project architecture, contract relationships, and deployment strategies ``

#### 3. Nested CLAUDE.md files[​](#3-nested-claudemd-files "Direct link to 3. Nested CLAUDE.md files")

To maintain a more granular control of the capabilities of Claude when you work with different areas of your repo, you can create specialized instructions for different project areas. To do this, place a nested `CLAUDE.md` file in subdirectories in your repo(cadence, frontend, backend, and so on). Claude will automatically read these files when working on these subdirectories. Here is an example:

**cadence/.claude/CLAUDE.md:**

`_25

# Cadence development instructions

_25

_25

## Syntax requirements

_25

_25

- Always use proper resource syntax: @{NonFungibleToken.NFT}

_25

- Implement required interfaces: NonFungibleToken, MetadataViews.

_25

- Use view functions for read-only operations.

_25

- Follow auth capability patterns for transactions.

_25

_25

## Testing protocol

_25

_25

- Write unit tests for all contract functions.

_25

- Test resource creation and destruction.

_25

- Verify proper event emission.

_25

- Validate access controls and permissions.

_25

- Test for breaking changes and edge cases.

_25

_25

## Standard patterns

_25

_25

Reference the Flow documentation for:

_25

_25

- Contract deployment and initialization.

_25

- Resource collection patterns.

_25

- Proper error handling and panics.

_25

- Gas optimization techniques.`

**frontend/.claude/CLAUDE.md:**

`_14

# Frontend FCL integration instructions

_14

_14

## Configuration management

_14

_14

- Keep contract addresses in environment variables.

_14

- Use proper network switching logic.

_14

- Implement user authentication flows.

_14

- Handle transaction status updates.

_14

_14

## Best practices

_14

_14

- Show loading states for blockchain interactions.

_14

- Provide clear error messages for failed transactions.

_14

- Cache contract data when appropriate.`

#### Local Claude.md[​](#local-claudemd "Direct link to Local Claude.md")

You can also create a `CLAUDE.local.md` file that is used just for you and not shared with your team.

## Workflow strategies[​](#workflow-strategies "Direct link to Workflow strategies")

Claude excels when it follows a structured development approach. We recommend you implement this four-stage methodology:

### Stage 1: Idea development[​](#stage-1-idea-development "Direct link to Stage 1: Idea development")

**Objective**: Bounce ideas with Claude to better understand of what you can build and why it would work.

**Process**:

1. Click `Shift` + `Tab` to cycle through the different response forms that Claude offers until you reach the Plan Mode.

![Plan Mode](/assets/images/plan_mode-9f5209f2cfeffd4f5b0061e58377046b.png)

2. Describe your Flow project concept to Claude.
3. Ask for requirement analysis and technical feasibility assessment.

**Example conversation**:

`_10

User: "I want to create a collectible card game on Flow where players can battle and evolve their cards"

_10

_10

Claude Response: [Analyzes requirements, suggests NFT architecture, identifies game mechanics, proposes contract structure]`

**Outputs**:

* Detailed project requirements document.
* Technical architecture overview.
* Flow-specific implementation considerations.
* Resource and timeline estimates.

### Stage 2: Visualization[​](#stage-2-visualization "Direct link to Stage 2: Visualization")

**Objective**: Create visual representations and demos to validate project concepts before development. You can use Claude with this process, but it is best to combine LLM models like Gemini 2.5 in order to create the visual representations.

**Tools and techniques**:

* **Mermaid Diagrams**: Generate contract relationship diagrams, user flow charts, and system architecture visuals.
* **UI Mockups**: Create interface mockups for frontend applications.
* **Contract Schemas**: Visualize data structures and resource relationships.
* **Transaction Flow Maps**: Diagram user interactions and blockchain state changes.

**Example workflow**:

`_10

User: "Create a diagram showing how card evolution works in my game"

_10

_10

[Claude generates Mermaid diagram showing contract interactions, resource transformations, and event emissions]`

**Claude code commands**:

* Use image upload to share visual concepts.
* Request Mermaid diagrams for complex systems.
* Ask for UI mockups based on Flow wallet integration patterns.

### Stage 3: Planning with Claude code[​](#stage-3-planning-with-claude-code "Direct link to Stage 3: Planning with Claude code")

**Objective**: Break down the project into manageable, incremental development tasks with Claude's planning capabilities.

**Planning process**:

1. **Turn On Planning Mode**: Explicitly tell Claude you're in planning phase or cycle through the different modes (with `Shift` + `Tab`) until you reach Plan Mode.
2. **Confirm Knowledge Comprehension**: Ask Claude to read important files first and then confirm the knowledge with you. Immediately ask it questions about the codebase to verify its knowledge.
3. **Plan Generation**: Tell Claude to generate an action plan that is incremental and has specific goals and checkpoints (this file can be called `T0-DO.md` and placed in a `/tasks` folder that contains relevant information about the completion of specific tasks or steps).
4. **Task Breakdown**: Request comprehensive task decomposition for incremental changes.
5. **Dependency Mapping**: Identify task dependencies and critical path.
6. **Checkpoint Strategy**: Define git commit points and testing milestones.

**Example planning session**:

`_18

User: "Set up a roadmap and plan of the to-do's that need to be completed for my card game NFT contracts"

_18

_18

Claude Response:

_18

Task 1: Set up basic NFT contract structure

_18

- Implement NonFungibleToken interface

_18

- Add MetadataViews compatibility

_18

- Create basic card resource

_18

- Write deployment transaction

_18

- Checkpoint: Basic NFT functionality

_18

_18

Task 2: Add game mechanics

_18

- Implement battle system

_18

- Add evolution functionality

_18

- Create game state management

_18

- Write game transaction scripts

_18

- Checkpoint: Core game mechanics

_18

_18

[Continues with detailed breakdown]`

**Plan outputs**:

* Generate a detailed to-do list that is thoroughly divided between goals, objectives, checkpoints and tasks that need to be achieved in an incremental manner.
* Dependency graph showing task relationships.
* Test strategies for each development phase.
* Deployment sequence and validation protocols.

A downside of Claude is that it doesn't have a checkpoint control like the agent chat does in Cursor. If you make frequent git commits and work on separate branches, it can help mitigate this. Never attempt to give Claude a big task as it most likely doesn't have enough knowledge about the task at hand to complete it successfully.

### Stage 4: Build execution[​](#stage-4-build-execution "Direct link to Stage 4: Build execution")

**Objective**: Implement planned tasks systematically with Claude's development capabilities.

**Build process**:

1. **Task Assignment**: Work on one incremental task at a time.
2. **Implementation**: Use Claude to generate code, debug issues, and optimize solutions.
3. **Reporting**: After it completes a task, Claude generates a report of what it did and why it did it in a `.md` file in the `/tasks` folder so that you can have better understand the changes made.
4. **Validation**: Test each component thoroughly before you proceed.
5. **Documentation**: Generate inline documentation and update project docs.
6. **Checkpoint**: Commit working code with descriptive messages.
7. **Updating**: Ask Claude to update the `TO-DO.md` with the completed steps and changes after the commit is approved.

**Development workflow**:

`_11

User: "Implement Task 1: Basic NFT contract structure"

_11

_11

[Claude generates contract code, deployment scripts, and tests]

_11

_11

User: "Test this implementation"

_11

_11

[Claude provides testing commands and validation scripts]

_11

_11

User: "Commit this checkpoint"

_11

_11

[Claude suggests commit message and validates completion]`

## Advanced Claude features[​](#advanced-claude-features "Direct link to Advanced Claude features")

### Subagent utilization[​](#subagent-utilization "Direct link to Subagent utilization")

For complex Flow projects, leverage Claude's subagent capabilities to handle parallel development tasks:

**When to use subagents**:

* To develop multiple contracts simultaneously.
* Frontend and backend development in parallel.
* To test different implementation approaches.
* Documentation generation while coding.
* To deal with a big task so that Claude can deploy subagents to break down the task into smaller components that are running in parallel.

**Example subagent usage**:

`_10

User: "Create subagents to develop the NFT contract and the marketplace contract in parallel"

_10

_10

[Claude spawns separate conversation threads for each contract, which maintains coordination between them.]`

### Auto-verification and iteration[​](#auto-verification-and-iteration "Direct link to Auto-verification and iteration")

Configure Claude to automatically verify its work and iterate for improvements:

**Verification patterns**:

* **Compilation Checks**: Automatically test Cadence syntax after code generation.
* **Test Execution**: Run unit tests and integration tests after implementation.
* **Deployment Validation**: Verify contract deployment on emulator before you suggest testnet deployment.

### Memory and context management[​](#memory-and-context-management "Direct link to Memory and context management")

**Use the # memory mode**:
Press `#` to enter memory mode and specify important information for Claude to remember:

`_10

# Remember that this project uses a modular NFT architecture with separate traits contracts.

_10

# Remember that we need to use a DS Proxy system for contract upgrades.`

**Context optimization**:

* Use `Ctrl+R` for verbose output when you debug complex issues.
* Compact conversations at natural breakpoints (around 20% context usage).
* Constantly refactor `CLAUDE.md` to take into accounts changes made throughout the development process.
* Maintain focused conversations for specific development tasks.

## Development workflows and best practices[​](#development-workflows-and-best-practices "Direct link to Development workflows and best practices")

Give Claude some sort of tool it can use for feedback (MCP or tool) to check its work and it will iterate by itself to get better results. Claude can iterate for hours if needed, but it needs to be able to analyze its work. These alternative workflows can be very useful as well, but they depend on your ability to close the feedback loop so that Claude can analyze and comprehend the results of its code generation:

### Test-driven development with Claude[​](#test-driven-development-with-claude "Direct link to Test-driven development with Claude")

**Workflow**: Write Tests → Commit → Code → Iterate → Commit

`_10

User: "Write tests for card evolution functionality first"

_10

_10

[Claude generates comprehensive test suite]

_10

_10

User: "Now implement the evolution logic to pass these tests"

_10

_10

[Claude implements feature with test-driven approach]`

### Screenshot-driven development[​](#screenshot-driven-development "Direct link to Screenshot-driven development")

**Workflow**: Write Code → Screenshot Result → Iterate

Particularly useful for frontend development:

`_10

User: "Implement this card display component"

_10

_10

[Claude generates React component]

_10

_10

User: [Uploads screenshot of result]

_10

_10

Claude: "I see the card layout needs improvement. Let me adjust the CSS..."`

### Checkpoint-based development[​](#checkpoint-based-development "Direct link to Checkpoint-based development")

**Best practices**:

* Commit after each completed task.
* Use descriptive commit messages that Claude generates.
* Create branches for experimental features.
* Tag stable releases for easy rollback.

**Example checkpoint strategy**:

`_10

git commit -m "feat: implement basic NFT contract with MetadataViews

_10

_10

- Add NonFungibleToken interface implementation

_10

- Include required MetadataViews for marketplace compatibility

_10

- Create basic card resource with metadata

_10

- Add deployment transaction and initialization script

_10

- All tests passing on emulator

_10

_10

Checkpoint: Basic NFT functionality complete"`

### Error resolution and debugging[​](#error-resolution-and-debugging "Direct link to Error resolution and debugging")

**Systematic debugging approach**:

1. **Error Analysis**: Provide Claude with complete error messages and context.
2. **Root Cause Investigation**: Let Claude analyze potential causes.
3. **Solution Implementation**: Apply suggested fixes incrementally.
4. **Verification**: Test fixes thoroughly before you proceed.
5. **Documentation**: Update project documentation with lessons learned.

**Example debugging session**:

`_10

User: "Getting authorization error in my transaction"

_10

_10

Claude: "Let me analyze the auth capability requirements. I see the issue is with the granular auth pattern. Here's the fix..."

_10

_10

[Provides corrected transaction with proper auth syntax]`

### Multi-network deployment[​](#multi-network-deployment "Direct link to Multi-network deployment")

**Deployment workflow with Claude**:

1. **Emulator Testing**: Comprehensive local testing and validation.
2. **Configuration Update**: Update flow.json and FCL config for testnet.
3. **Testnet Deployment**: Deploy and validate on testnet.
4. **Frontend Integration**: Update frontend configuration and test user flows.
5. **Mainnet Preparation**: Final validation and deployment to mainnet.

### MCP server share[​](#mcp-server-share "Direct link to MCP server share")

You can set up [MCPs](https://docs.anthropic.com/en/docs/claude-code/mcp) for Claude to use as tools. These can also be set up in the `CLAUDE.md` file so that every team member consistently uses the same MCPs. Share the `/Claude/mcp.json` files so that the team can use the same MCP servers.

**Team MCP configuration**:

To grant Claude Code [access to use an MCP server](https://docs.anthropic.com/en/docs/claude-code/mcp), run the following commands:

`_10

# Adding a MCP server

_10

claude mcp add <name> <command> [args...]

_10

_10

# Adding a local server

_10

claude mcp add my-server -e API_KEY=123 -- /path/to/server arg1 arg2`

You can also try these [MCPs for Flow development](https://github.com/Outblock/flow-mcp-monorepo):

`_10

# Shared MCP servers for team consistency

_10

claude mcp add flow_mcp

_10

claude mcp add flow-defi-mcp`

### Version control for AI configuration[​](#version-control-for-ai-configuration "Direct link to Version control for AI configuration")

**Best practices**:

* Include `CLAUDE.md` files in version control.
* Document MCP server configurations in README.
* Share `CLAUDE.local.md` patterns (and don't commit personal configs).
* Maintain team coding standards through shared AI instructions.

## Key bindings and shortcuts[​](#key-bindings-and-shortcuts "Direct link to Key bindings and shortcuts")

### Essential Claude shortcuts[​](#essential-claude-shortcuts "Direct link to Essential Claude shortcuts")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shortcut Function Flow Development Usage|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `#` Memory mode Store project architecture decisions|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `Shift+Tab` Auto-accept edits Quickly accept generated Cadence code|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `!` Bash mode Execute Flow CLI commands directly|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `@` Add file/folder Reference contracts, transactions, configs|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `Esc` Cancel operation Stop incorrect generation and execution|  |  |  | | --- | --- | --- | | `Ctrl+R` Verbose output Detailed debugging for complex issues | | | | | | | | | | | | | | | | | | | | |

### Flow-specific usage patterns[​](#flow-specific-usage-patterns "Direct link to Flow-specific usage patterns")

**Memory mode examples**:

`_10

# This project follows the composite NFT pattern with separate trait contracts.

_10

# Gas optimization is critical - avoid loops in public functions.

_10

# All contracts must support MetadataViews for marketplace compatibility.`

**File reference patterns**:

`_10

@flow.json - Project configuration

_10

@cadence/contracts/MyNFT.cdc - Main NFT contract`

## Troubleshooting and optimization[​](#troubleshooting-and-optimization "Direct link to Troubleshooting and optimization")

### Common issues and solutions[​](#common-issues-and-solutions "Direct link to Common issues and solutions")

**Context window management**:

* Compact conversations at natural breakpoints or manually when around 20% of context usage remains.
* Use focused sub-conversations for specific tasks.
* Reference key files rather than copying entire contents.

**Performance optimization**:

* Use the $200/month plan for complex Flow projects.
* Turn on auto-compact to prevent context overflow.
* Break large tasks into smaller, focused conversations.
* Hit `Esc` often if you see the agent on the wrong path and ask it to undo its recent action.

**Integration problems**:

* Verify MCP server configurations.
* Check Flow CLI integration and permissions.
* Validate `CLAUDE.md` file syntax and structure.

### Best practices for Flow development[​](#best-practices-for-flow-development "Direct link to Best practices for Flow development")

**Project management**:

* Maintain clear separation between contracts, transactions, and frontend code.
* Use nested `CLAUDE.md` files for different development areas.
* Keep project documentation synchronized with implementation.

**Code quality**:

* Always compile Cadence code before deployment.
* Use Claude for security review suggestions.
* Implement comprehensive testing at each development stage.

**Deployment management**:

* Test thoroughly on emulator before testnet deployment.
* Validate FCL configuration changes across networks.
* Use systematic deployment checklists that Claude generates.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this guide, you explored how to leverage Claude for efficient Flow blockchain and Cadence development. You learned to implement a systematic four-stage development methodology that transforms ideas into production-ready applications through AI-assisted visualization, planning, and execution.

You discovered how to configure persistent project context through `CLAUDE.md` files, allowing your AI assistant to maintain comprehensive understanding of Flow-specific patterns, project architecture, and team standards across all development sessions. The integration of specialized tools like Flow CLI, FCL configuration management, and MCP servers creates a comprehensive development environment optimized for blockchain application building.

The systematic approaches covered - from test-driven development and checkpoint-based workflows to subagent utilization and auto-verification - provide a foundation for building complex Flow applications with confidence and efficiency. The emphasis on incremental development, comprehensive testing, and systematic deployment ensures your projects meet the reliability requirements essential for blockchain applications.

Now that you have completed this guide, you should be able to:

* Set up and configure Claude for optimal Flow blockchain development workflows with persistent context and specialized tooling.
* Implement the four-stage development methodology (Idea → Visualization → Planning → Build) for systematic Cadence project development.
* Apply advanced Claude features including subagents, auto-verification, and team collaboration patterns for complex Flow applications.
* Integrate Claude seamlessly with Flow CLI, FCL, and other Flow development tools for comprehensive project management across emulator, testnet, and mainnet environments.

The combination of AI-powered development assistance with Flow's comprehensive toolchain creates an unprecedented opportunity for building sophisticated blockchain applications efficiently and reliably. As you continue developing on Flow, these systematic approaches will help you maintain high code quality while aClaudeelerating your development velocity.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/claude-code.md)

Last updated on **Nov 20, 2025** by **cshannon1218**

[Previous

Use Gemini AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/llms/gemini)[Next

Use Cursor AI](/blockchain-development-tutorials/use-AI-to-build-on-flow/cursor)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning objectives](#learning-objectives)* [Prerequisites](#prerequisites)
    + [Technical requirements](#technical-requirements)* [Claude setup and configuration](#claude-setup-and-configuration)
      + [What is Claude?](#what-is-claude)+ [Installation and subscription](#installation-and-subscription)+ [Initial configuration](#initial-configuration)+ [CLAUDE.md files](#claudemd-files)* [Workflow strategies](#workflow-strategies)
        + [Stage 1: Idea development](#stage-1-idea-development)+ [Stage 2: Visualization](#stage-2-visualization)+ [Stage 3: Planning with Claude code](#stage-3-planning-with-claude-code)+ [Stage 4: Build execution](#stage-4-build-execution)* [Advanced Claude features](#advanced-claude-features)
          + [Subagent utilization](#subagent-utilization)+ [Auto-verification and iteration](#auto-verification-and-iteration)+ [Memory and context management](#memory-and-context-management)* [Development workflows and best practices](#development-workflows-and-best-practices)
            + [Test-driven development with Claude](#test-driven-development-with-claude)+ [Screenshot-driven development](#screenshot-driven-development)+ [Checkpoint-based development](#checkpoint-based-development)+ [Error resolution and debugging](#error-resolution-and-debugging)+ [Multi-network deployment](#multi-network-deployment)+ [MCP server share](#mcp-server-share)+ [Version control for AI configuration](#version-control-for-ai-configuration)* [Key bindings and shortcuts](#key-bindings-and-shortcuts)
              + [Essential Claude shortcuts](#essential-claude-shortcuts)+ [Flow-specific usage patterns](#flow-specific-usage-patterns)* [Troubleshooting and optimization](#troubleshooting-and-optimization)
                + [Common issues and solutions](#common-issues-and-solutions)+ [Best practices for Flow development](#best-practices-for-flow-development)* [Conclusion](#conclusion)

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