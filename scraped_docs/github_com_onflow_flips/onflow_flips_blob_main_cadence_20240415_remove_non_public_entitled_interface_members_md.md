# Source: https://github.com/onflow/flips/blob/main/cadence/20240415-remove-non-public-entitled-interface-members.md

---
status: approved
flip: 262
authors: Bastian Müller (bastian.mueller@flowfoundation.org)
updated: 2024-04-15
---

# FLIP 262: Require matching access modifiers for interface implementation members

## Objective

This FLIP proposes to require access modifiers of members in the implementation
of an interface to match the access modifiers of the interface,
to avoid confusion and potential footguns.

## Motivation

Currently, the access modifier of a member in a type conforming to / implementing an interface
must not be more restrictive than the access modifier of the member in the interface.
That means an implementation may choose to use a more permissive access modifier than the interface.

This might be surprising to developers, as they might assume that the access modifier of the member
in the interface is a _requirement_ / _maximum_, not just a minimum, especially when using
a non-public / non-entitled access modifier (e.g. `access(contract)`, `access(account)`).

Requiring access modifiers of members in the implementation to match the access modifiers
of members given in the interface, should avoid confusion and potential footguns.

## User Benefit

Developers will hopefully be no longer confused and won't make assumptions
that might lead to security issues.

## Design Proposal

If an interface member has an access modifier, a composite type that conforms to it / implements
the interface must use exactly the same access modifier.

### Drawbacks

This proposal adds a new restriction to Cadence which might impact existing code.

Even though the impact on code is likely low, including this proposal in Cadence 1.0 means
that there is yet another breaking change, fairly late in the process of its release.

### Alternatives Considered

None

### Performance Implications

None

### Dependencies

None

### Engineering Impact

Very low.

The is is very easy to update the Cadence type checker to enforce access modifiers of members
in implementations match those of interfaces.

Most effort will be spent on updating existing and adding new test cases.

### Tutorials and Examples

For example, the following interface and composite type definitions are currently legal,
but will be no longer valid:

```cadence
access(all)
contract C1 {

    access(all)
    struct interface SI {

        access(contract)
        fun foo()
    }
}

access(all)
contract C2 {

    access(all)
    struct S: C1.SI {

        access(all)
        //     ^^^ invalid with this proposal,
        //     must be `contract`, like in interface SI
        fun foo() {}
    }
}
```

### Compatibility

The proposed changes might break existing Cadence programs.

### User Impact

This change is planned to be included in Cadence 1.0,
which already contains many other breaking changes.
