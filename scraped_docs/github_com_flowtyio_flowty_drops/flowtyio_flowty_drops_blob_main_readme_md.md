# Source: https://github.com/Flowtyio/flowty-drops/blob/main/README.md

# Flowty Drops

A system of contracts designed to make it easy to expose drops to platforms on the 
Flow Blockchain. Using FlowtyDrops and its supporting contracts, you can easily integrate
an open framework for anyone to showcase your drop on their own site/platform

## Overview

FlowtyDrops is made up of a few core resources and structs:
1. @Drop - Coordinates drops. Drop resources contain an array of Phase resources, details, and a capability to a Minter
    interface for it to us
2. @Phase - A stage of a drop. Many drops are segments into multiple stages (such as an allow-list followed by a public mint), phases
    are a way to represent this. Phases dictate what accounts can mint, how many, for what price. Each phase is independent of others,
    and be asked if it is active or not.
3. @Container - Holds Drop resources in it.
4. @{Minter} - A resource interface that creators can implement to be compatible with FlowtyDrops. When constructing a drop, you must
    supply a `Capability<&{Minter}>` to it.
5. {ActiveChecker} - A struct interface that is responsible for whether a phase is active or not. For example, one implementation could be configured
    to start a phase at a time in the future, while another could turn start based on block height.
6. {AddressVerifier} - A struct interface that is responsible for determining if an account is permitted to mint or not. For example,
    one implementation might permit any account to mint as many as it wants, while another might check an allow-list.
7. {Pricer} - A struct interface that is responsible for the price of a mint. For example, one implementation could be for a set flat
    fee while another could be dynamic based on an account's ownership of a certain collection


## Contracts

1. FlowtyDrops - The primary contract. All core resources and structs can
    be found here. All other contracts represent sample implementations
    of the definitions found here
2. DropFactory - Helper method to create pre-configured popular drop options
3. FlowtyAddressVerifiers - Implementations of the AddressVerifiers struct
    interface. AddressVerifiers handle whether a minter is permitted to
    mint with the given parameters they are using. Some verifiers might
    permit any kind of activity whereas others might require server-side
    signatures or prescence on an allow-list.
4. FlowtyPricers - Implementations of the Pricer struct interface. Pricers
    are responsible for handling how much an attempted mint should cost.
    For example, you might make a drop free, or might configure a drop to
    be a flat fee regardless of how many are being minted at once.
5. FlowtyActiveCheckers - Implementations of the ActiveChecker struct interface.
    ActiveCheckers are responsible for flagging if a drop is live or not. For
    example, a drop might go live a certain unix timestamp and end at a
    future date, or it might be on perpetually until manually turned off.