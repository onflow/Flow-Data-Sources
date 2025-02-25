# Source: https://cadence-lang.org/

Hello from Cadence | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

Cadence

## Forge the future of decentralized apps.Unleash **utility**, **composability**,and **safety** in smart contracts.

[Get started](/learn)

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
access(all)
resource NFT {

    access(all)
    fun greet(): String {
        return "I'm NFT #"
            .concat(self.uuid.toString())
    }
}

access(all)
fun main(): String {
    let nft <- create NFT()
    let greeting = nft.greet()
    destroy nft
    return greeting
}
```

Together, we are working to build a programming language to empower everyone to push the boundaries of smart contracts and on-chain logic.

Announced in 2020, the Cadence programming language introduced a new paradigm of resource-oriented programming. By leveraging the power of resources, Cadence brings exciting new ideas to the world of smart contracts. Cadence makes it easy to write maximally on-chain smart contracts that are secure by design. Our goals for Cadence are to enable ambitious developers to make daring & complex ideas possible while making them easy, fun & developer-friendly, as well as safe and secure.

Join us in shaping the future of blockchain, one line of code at a time. Get started today!

### Safety by design

Cadence provides security and safety guarantees that greatly simplify the development of secure smart contracts.

As smart contracts often deal with valuable assets, Cadence provides the [resource-oriented programming paradigm](https://cadence-lang.org/docs/language/resources), which guarantees that assets can only exist in one location at a time, cannot be copied, and cannot be accidentally lost or deleted.

Cadence includes several language features that prevent entire classes of bugs via a strong static type system, [design by contract](https://cadence-lang.org/docs/language/functions#function-preconditions-and-postconditions), and [capability-based access control](https://cadence-lang.org/docs/language/capabilities).

These security and safety features allow smart contract developers to focus on the business logic of their contract, instead of preventing security footguns and attacks.

### Built for permissionless composability

[Resources](https://cadence-lang.org/docs/language/resources) are stored directly in users' accounts, and can flow freely between contracts. They can be passed as arguments to functions, returned from functions, or even combined in arbitrary data structures. This makes implementing business logic easier and promotes the reuse of existing logic.

[Interfaces](https://cadence-lang.org/docs/language/interfaces) enable interoperability of contracts and resources allowing developers to integrate their applications into existing experiences easily.

In addition, the [attachments](https://cadence-lang.org/docs/language/attachments) feature of Cadence allows developers to extend existing types with new functionality and data, without requiring the original author of the type to plan or account for the intended behavior.

### Easy to learn, build and ship

Cadence's syntax is inspired by popular modern general-purpose programming languages like Swift, Kotlin, and Rust, so developers will find the syntax and the semantics familiar. Practical tooling, [documentation](https://cadence-lang.org/docs/language), and examples enable developers to start creating programs quickly and effectively.

### Powerful transactions for mainstream experiences

In Cadence, a transaction has a lot more flexibility and the power to perform multiple operations with a single transaction, as opposed to multiple, separate smart contract calls like in other languages. It allows complex, multi-step interactions to be one-click user experiences.

Developers can easily batch multiple transactions, turning complicated user journeys into a few clicks. For example, imagine approving and completing the listing of an NFT from a new collection in the same transaction, or adding and sending funds with just one approval.

### 🧰 Best-in-class tooling

Cadence comes with great IDE support. Use your favorite editor, like [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=onflow.cadence), Vim or Emacs, to get diagnostics, code completion, refactoring support, and more.

To further enhance the developer experience, there is also a native testing framework, which allows developers to write unit & integration tests using Cadence.

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.