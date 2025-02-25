# Source: https://cadence-lang.org/docs/measuring-time

Measuring Time In Cadence | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Measuring Time

On this page

# Measuring Time In Cadence

## Accessing Time From Cadence[​](#accessing-time-from-cadence "Direct link to Accessing Time From Cadence")

Both the [block height and the block timestamp](/docs/language/environment-information#block-information) are accessible from within Cadence code.

This means that they can be used to calculate dates and durations by smart contracts on Flow
that need to lock resources until a particular point in the future, calculate values between a range of dates,
or otherwise deal with the passage of time.

There are two popular strategies that are used to measure time on blockchains:

1. Use the timestamp, and optionally check that the average duration of the last n blocks
   is close enough to the block target duration to make an attack unlikely.
2. Use the block height directly. Block height can be treated intuitively
   (a hundred blocks, a thousand blocks) or can be related to estimated timestamps
   and thereby to time off-chain by the methods described in this article.

## Time On The Flow Blockchain[​](#time-on-the-flow-blockchain "Direct link to Time On The Flow Blockchain")

> Flow targets 1 second block times but the protocol is still early in its development
> and further optimizations are needed to achieve that.
> As of Feb 2021, the rate of block finalization on Mainnet is more than 0.5 blocks/s; with a standard deviation of ±0.1 blocks/s.
> Hence, a new block is finalized on average every 2 seconds.
> Note that block height only has a loose correlation with time,
> as [the block rate naturally fluctuates](https://developers.flow.com/build/run-and-secure/nodes/faq/operators.mdx#does-the-blockheight-go-up-1-every-second).

In addition to the natural variation described above,
there are several theoretical block production attacks that could skew this relationship even further.
These attacks are unlikely on Flow in the absence of byzantine nodes.
The timestamp cannot be earlier than the timestamp of the previous block,
and cannot be too far into the future ([currently ten seconds](https://github.com/onflow/flow-go/blob/master/module/builder/consensus/builder.go#L60))

* proposed blocks that fail to satisfy these conditions will be rejected by Flow's consensus algorithm.
  But the mere possibility of these attacks places an additional limit on the confidence
  with which we can use block heights or block timestamps to determine off-chain time from protocol-level data on-chain.

The block timestamp is not the only way to identify a block within the flow of off-chain time.
Each block is numbered successively by its "height", block 70000 is followed by block 70001, 70002,
and so on. Blocks with heights out of sequence are rejected by Flow's consensus algorithm.
In theory the timestamp on a block should be roughly equivalent to the timestamp on the Flow genesis block,
plus the block height multiplied by the target block rate.
But as we have seen both the target and the on-chain average rate of block production may vary over time.
This makes such calculations more difficult.

### Using The Timestamp[​](#using-the-timestamp "Direct link to Using The Timestamp")

Given that [Flow consensus will reject new blocks with a timestamp more than ten seconds into the future from the previous block](https://github.com/onflow/flow-go/blob/1e8a2256171d5fd576f442d0c335c9bcc06e1e09/module/builder/consensus/builder.go#L525-L536),
as long as you do not require an accuracy of less than ten seconds
it is probably safe to use the block timestamp for events lasting a few days - in the absence of a change in block production rate targets.
Or, more intuitively, your timestamp is highly likely to be the correct hour,
very likely to be the correct minute, and may well be within ten seconds of the correct second.
Which of these scales is tolerable for your use case depends on how long the events you need to represent will take.
In an auction lasting several days, you are probably safe with any scale above ten seconds.

`_10

// To get the timestamp of the block that the code is being executed in

_10

getCurrentBlock().timestamp

_10

_10

// To get the timestamp of a known previous block, if available

_10

getBlock(at: 70001)?.timestamp`

### Using The Block Height[​](#using-the-block-height "Direct link to Using The Block Height")

In theory block numbers are more reliable than timestamps,
as the block height is incremented for each block in a fork.
But in practice we must still relate block numbers to off-chain time values,
and to do this requires that we assume that the average block time will hold.
This can vary due to factors other than attacks.
Given that block time targets will vary as Flow development continues,
this will affect any calculations you may make in order to relate block numbers to calendar time.

`_10

// To get the block number of the block that the code is being executed in

_10

getCurrentBlock().height

_10

_10

// To get the block number of a known previous block, if available

_10

getBlock(at: 70001)?.height`

## Recommendations[​](#recommendations "Direct link to Recommendations")

If your contract code can tolerate the limitations described above, use block timestamps.
If not, you may need to consider more exotic solutions (time oracles, etc.).

Whichever method you use, be careful not to hardcode any assumptions
about block rates production rates into your code, on-chain or off,
in a way that cannot be updated later.

On-chain auctions and similar mechanisms should always have an extension mechanism.
If someone bids at the last moment (which is easier to do with a block production attack),
the end time for the auction extends (if necessary) to N minutes past the last bid.
(10 minutes, 30 minutes, an hour). As N increases, this becomes more secure:
N=5 should be more than enough. with the current parameters of the Flow blockchain.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/measuring-time.mdx)

[Previous

JSON-Cadence format](/docs/json-cadence-spec)[Next

Testing](/docs/testing-framework)

###### Rate this page

😞😐😊

* [Accessing Time From Cadence](#accessing-time-from-cadence)
* [Time On The Flow Blockchain](#time-on-the-flow-blockchain)
  + [Using The Timestamp](#using-the-timestamp)
  + [Using The Block Height](#using-the-block-height)
* [Recommendations](#recommendations)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.