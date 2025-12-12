# Source: https://developers.flow.com/build/cadence/smart-contracts/testing-strategy

Testing Smart Contracts | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            - [Learn Cadence ↗️](/build/cadence/learn-cadence)- [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)- [Deploying Contracts](/build/cadence/smart-contracts/deploying)- [Testing Smart Contracts](/build/cadence/smart-contracts/testing-strategy)- [Cadence Testing Framework](/build/cadence/smart-contracts/testing)- [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)+ [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Writing and Deploying Smart Contracts* Testing Smart Contracts

On this page

# Testing Smart Contracts

This document describes a single, pragmatic strategy to test on Flow. Use layers that are deterministic and isolated by default, add realism with forks when needed, and keep a minimal set of live network checks before release.

## At a glance[​](#at-a-glance "Direct link to At a glance")

* **Unit & Property — Test Framework**: Hermetic correctness and invariants.
* **Integration — Fork Testing**: Real contracts and data; mutations stay local.
* **Local integration sandbox (interactive, `flow emulator --fork`)**: Drive apps/E2E against production-like state.
* **Staging (testnet)**: Final plumbing and config checks.
* **Post-deploy (read-only)**: Invariant dashboards and alerts.

## Layers[​](#layers "Direct link to Layers")

### Unit and property — test framework[​](#unit-and-property--test-framework "Direct link to Unit and property — test framework")

* Use `flow test`
* **Use when**: You validate Cadence logic, invariants, access control, error paths, footprint.
* **Why**: Fully deterministic and isolated; highest-regression signal.
* **Run**: Every commit/PR; wide parallelism.
* **Notes**: Write clear success andfailure tests, add simple “this should always hold” rules when helpful, and avoid external services.

See also: [Running Cadence Tests](/build/tools/flow-cli/tests).

### Integration — fork testing[​](#integration--fork-testing "Direct link to Integration — fork testing")

* **Use when**: You interact with real on-chain contracts or data (FTand NFT standards, AMMs, wallets, oracles, bridges), upgrade checks, historical repro.
* **Why**: Real addresses, capability paths, and resource schemas; catches drift early.
* **Run**: On Pull Requests (PRs), run the full forked suite if practical (pinned), or a small quick set; run more cases nightly or on main.
* **How**: Configure with `#test_fork(network: "mainnet", height: nil)` in your test file, or use `flow test --fork` CLI flags.
* **Notes**:
  + Pin with `height: 85432100` in the pragma (or `--fork-height` CLI flag) where reproducibility matters.
  + Prefer local deployment + impersonation over real mainnet accounts.
  + Mutations are local to the forked runtime; the live network is never changed.
  + Be mindful of access-node availability and rate limits.
  + External oracles and protocols: forked tests do not call off-chain services or other chains; mock these or run a local stub.

See also: [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing), [Fork Testing Flags](/build/tools/flow-cli/tests#fork-testing-flags).

### Local integration sandbox — `flow emulator --fork`[​](#local-integration-sandbox--flow-emulator---fork "Direct link to local-integration-sandbox--flow-emulator---fork")

* **Use when**: You drive dApps, wallets, bots, indexers, or exploratory debugging outside the test framework.
* **Why**: Production-like state with local, disposable control; great for end to end (E2E) and migrations.
* **Run**: Dev machines and focused E2E CI jobs.
* **Notes**:

  + Pin height; run on dedicated ports; impersonation is built-in; mutations are local; off-chain/oracle calls are not live—mock or run local stubs
  + What to run: Manual exploration and debugging of flows against a forked state; frontend connected to the emulator (for example, `npm run dev` pointed at `http://localhost:8888`); automated E2E/FE suites (for example, Cypress or Playwright) against the local fork; headless clients, wallets/bots/indexers, and migration scripts.
  + Not for the canonical Cadence test suite—prefer fork testing with `flow test` for scripted Cadence tests (see [Fork Testing Flags](/build/tools/flow-cli/tests#fork-testing-flags) and [Running Cadence Tests](/build/tools/flow-cli/tests))

  Quick start example:

  `_10

  # Start a fork (pinning height recommended for reproducibility)

  _10

  flow emulator --fork mainnet --fork-height <BLOCK>`

  `_10

  // In your root component (e.g., App.tsx)

  _10

  import { FlowProvider } from '@onflow/react-sdk';

  _10

  _10

  function App() {

  _10

  return (

  _10

  <FlowProvider config={{ accessNodeUrl: 'http://localhost:8888' }}>

  _10

  {/* Your app components */}

  _10

  </FlowProvider>

  _10

  );

  _10

  }`

  `_10

  # Run app

  _10

  npm run dev

  _10

  _10

  # Run E2E tests

  _10

  npx cypress run`

See also: [Flow Emulator](/build/tools/emulator).

### Staging — Testnet[​](#staging--testnet "Direct link to Staging — Testnet")

* **Use when**: Final network plumbing and configuration checks before release.
* **Why**: Validates infra differences you cannot fully simulate.
* **Run**: Pre-release and on infra changes.
* **Notes**:

  + Keep canaries minimal and time-boxed; protocol and partner support may be limited on testnet (not all third-party contracts are deployed or up to date).
  + What to run: Minimal app smoke tests (login and auth, key flows, mint and transfer, event checks); frontend connected to Testnet with a small Cypress/Playwright smoke set; infra or config checks (endpoints, contract addresses oraliases, env vars, service or test accounts)
  + Not for the canonical Cadence test suite — prefer fork testing with `flow test` for scripted tests (see [Fork Testing Flags](/build/tools/flow-cli/tests#fork-testing-flags) and [Running Cadence Tests](/build/tools/flow-cli/tests))

  Quick start example:

  `_12

  // In your root component (e.g., App.tsx)

  _12

  import { FlowProvider } from '@onflow/react-sdk';

  _12

  _12

  function App() {

  _12

  return (

  _12

  <FlowProvider

  _12

  config={{ accessNodeUrl: 'https://rest-testnet.onflow.org' }}

  _12

  >

  _12

  {/* Your app components */}

  _12

  </FlowProvider>

  _12

  );

  _12

  }`

  `_10

  # Run app

  _10

  npm run dev

  _10

  _10

  # Run smoke tests

  _10

  npx cypress run --spec "cypress/e2e/smoke.*"`

See also: [Flow Networks](/protocol/flow-networks).

### Post-deploy monitoring (read-only)[​](#post-deploy-monitoring-read-only "Direct link to Post-deploy monitoring (read-only)")

* **Use when**: After releases to confirm invariants and event rates.
* **Why**: Detects real-world anomalies quickly.
* **Run**: Continuous dashboards and alerts tied to invariants.

## Reproducibility and data management[​](#reproducibility-and-data-management "Direct link to Reproducibility and data management")

* **Pin where reproducibility matters**: Use `--fork-height <block>` for both `flow test --fork` and `flow emulator --fork`. Pins are per‑spork; historical data beyond spork boundaries is unavailable. For best results, keep a per‑spork stable pin and also run a "latest" freshness job.
* **Named snapshots**: Maintain documented pin heights (for example, in CI vars or a simple file) with names per dependency or protocol
* **Refresh policy**: Advance pins via a dedicated “freshness” PR; compare old vs. new pins
* **Goldens**: Save a few canonical samples (for example, event payloads, resource layouts, key script outputs) as JSON in your repo, and compare them in CI to catch accidental schema/shape changes. Update the samples intentionally as part of upgrades.

## CI tips[​](#ci-tips "Direct link to CI tips")

* PRs: Run emulator unit or property and forked integration (pinned). Full suite is fine if practical; otherwise a small quick set.
* Nightly/Main: Add a latest pin job and expand fork coverage as needed.
* E2E (optional): Use `flow emulator --fork` at a stable pin and run your browser tests.

## Test selection and tagging[​](#test-selection-and-tagging "Direct link to Test selection and tagging")

* **Optional naming helpers**: Use simple suffixes in test names like `_fork`, `_smoke`, `_e2e` if helpful.
* Pass files and directories to run the tests you care about: `flow test FILE1 FILE2 DIR1 ...` (most common).
* Optionally, use `--name <substring>` to match test functions when it’s convenient.
* **Defaults**: PRs can run the full fork suite (pinned) or a small quick set; nightly runs broader coverage (and optional E2E).

## Troubleshooting tips[​](#troubleshooting-tips "Direct link to Troubleshooting tips")

* Re-run at the same `--fork-height`, then at latest
* Compare contract addresses/aliases in `flow.json`
* Diff event or resource shapes against your stored samples
* Check access-node health and CI parallelism or sharding

## Dos and Don’ts[​](#dos-and-donts "Direct link to Dos and Don’ts")

* **Do**: Keep a fast, hermetic base; pin forks; tag tests; maintain tiny PR smoke sets; document pins and set a simple refresh schedule (for example, after each spork or monthly).
* **Don't**: Make "latest" your default in CI; create or rely on real mainnet accounts; conflate fork testing (`flow test`) with the emulator's fork mode (`flow emulator --fork`).

## Related docs[​](#related-docs "Direct link to Related docs")

* Guide → Running tests: [Running Cadence Tests](/build/tools/flow-cli/tests)
* Guide → How-to: [Cadence Testing Framework](/build/cadence/smart-contracts/testing)
* Tutorial → Step-by-step: [Fork Testing with Cadence](/blockchain-development-tutorials/cadence/fork-testing)
* Tool → Emulator (including fork mode): [Flow Emulator](/build/tools/emulator)
* Reference → Fork testing flags: [Fork Testing Flags](/build/tools/flow-cli/tests#fork-testing-flags)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/smart-contracts/testing-strategy.md)

Last updated on **Dec 4, 2025** by **cshannon1218**

[Previous

Deploying Contracts](/build/cadence/smart-contracts/deploying)[Next

Cadence Testing Framework](/build/cadence/smart-contracts/testing)

###### Rate this page

😞😐😊

Copy as Markdown

* [At a glance](#at-a-glance)* [Layers](#layers)
    + [Unit and property — test framework](#unit-and-property--test-framework)+ [Integration — fork testing](#integration--fork-testing)+ [Local integration sandbox — `flow emulator --fork`](#local-integration-sandbox--flow-emulator---fork)+ [Staging — Testnet](#staging--testnet)+ [Post-deploy monitoring (read-only)](#post-deploy-monitoring-read-only)* [Reproducibility and data management](#reproducibility-and-data-management)* [CI tips](#ci-tips)* [Test selection and tagging](#test-selection-and-tagging)* [Troubleshooting tips](#troubleshooting-tips)* [Dos and Don’ts](#dos-and-donts)* [Related docs](#related-docs)

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