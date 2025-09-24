# Source: https://cadence-lang.org/docs/json-cadence-spec

JSON-Cadence Data Interchange Format | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* JSON-Cadence Format

On this page

# JSON-Cadence Data Interchange Format

> Version 0.3.1

JSON-Cadence is a data interchange format used to represent Cadence values as language-independent JSON objects.

This format includes less type information than a complete [ABI](https://en.wikipedia.org/wiki/Application_binary_interface), and instead promotes the following tenets:

* **Human-readability** — JSON-Cadence is easy to read and comprehend, which speeds up development and debugging.
* **Compatibility** — JSON is a common format with built-in support in most high-level programming languages, making it easy to parse on a variety of platforms.
* **Portability** — JSON-Cadence is self-describing and thus can be transported and decoded without accompanying type definitions (i.e., an ABI).

The following provides reference information and examples when working with various values and types.

## Values[​](#values "Direct link to Values")

### Void[​](#void "Direct link to Void")

`_10

{

_10

"type": "Void"

_10

}`

**Example**

`_10

{

_10

"type": "Void"

_10

}`

---

### Optional[​](#optional "Direct link to Optional")

`_10

{

_10

"type": "Optional",

_10

"value": null | <value>

_10

}`

**Example**

`_16

// Non-nil

_16

_16

{

_16

"type": "Optional",

_16

"value": {

_16

"type": "UInt8",

_16

"value": "123"

_16

}

_16

}

_16

_16

// Nil

_16

_16

{

_16

"type": "Optional",

_16

"value": null

_16

}`

### Bool[​](#bool "Direct link to Bool")

`_10

{

_10

"type": "Bool",

_10

"value": true | false

_10

}`

**Example**

`_10

{

_10

"type": "Bool",

_10

"value": true

_10

}`

### String[​](#string "Direct link to String")

`_10

{

_10

"type": "String",

_10

"value": "..."

_10

}`

**Example**

`_10

{

_10

"type": "String",

_10

"value": "Hello, world!"

_10

}`

### Address[​](#address "Direct link to Address")

`_10

{

_10

"type": "Address",

_10

"value": "0x0" // as hex-encoded string with 0x prefix

_10

}`

**Example**

`_10

{

_10

"type": "Address",

_10

"value": "0x1234"

_10

}`

### Integers[​](#integers "Direct link to Integers")

`[U]Int`, `[U]Int8`, `[U]Int16`, `[U]Int32`,`[U]Int64`,`[U]Int128`, `[U]Int256`, `Word8`, `Word16`, `Word32`, `Word64`, `Word128` or `Word256`.

Although JSON supports integer literals up to 64 bits, all integer types are encoded as strings for consistency.

While the static type is not strictly required for decoding, it is provided to inform the client of the potential range.

`_10

{

_10

"type": "<type>",

_10

"value": "<decimal string representation of integer>"

_10

}`

**Example**

`_10

{

_10

"type": "UInt8",

_10

"value": "123"

_10

}`

### Fixed point numbers[​](#fixed-point-numbers "Direct link to Fixed point numbers")

* `[U]Fix64`

Although fixed point numbers are implemented as integers, JSON-Cadence uses a decimal string representation for readability.

`_10

{

_10

"type": "[U]Fix64",

_10

"value": "<integer>.<fractional>"

_10

}`

**Example**

`_10

{

_10

"type": "Fix64",

_10

"value": "12.3"

_10

}`

### Array[​](#array "Direct link to Array")

`_10

{

_10

"type": "Array",

_10

"value": [

_10

<value at index 0>,

_10

<value at index 1>

_10

// ...

_10

]

_10

}`

**Example**

`_17

{

_17

"type": "Array",

_17

"value": [

_17

{

_17

"type": "Int16",

_17

"value": "123"

_17

},

_17

{

_17

"type": "String",

_17

"value": "test"

_17

},

_17

{

_17

"type": "Bool",

_17

"value": true

_17

}

_17

]

_17

}`

### Dictionary[​](#dictionary "Direct link to Dictionary")

Dictionaries are encoded as a list of key-value pairs to preserve the deterministic ordering implemented by Cadence.

`_10

{

_10

"type": "Dictionary",

_10

"value": [

_10

{

_10

"key": "<key>",

_10

"value": <value>

_10

},

_10

...

_10

]

_10

}`

**Example**

`_16

{

_16

"type": "Dictionary",

_16

"value": [

_16

{

_16

"key": {

_16

"type": "UInt8",

_16

"value": "123"

_16

},

_16

"value": {

_16

"type": "String",

_16

"value": "test"

_16

}

_16

}

_16

]

_16

// ...

_16

}`

### Composites (Struct, Resource, Event, Contract, Enum)[​](#composites-struct-resource-event-contract-enum "Direct link to Composites (Struct, Resource, Event, Contract, Enum)")

Composite fields are encoded as a list of name-value pairs in the order in which they appear in the composite type declaration.

`_13

{

_13

"type": "Struct" | "Resource" | "Event" | "Contract" | "Enum",

_13

"value": {

_13

"id": "<fully qualified type identifier>",

_13

"fields": [

_13

{

_13

"name": "<field name>",

_13

"value": <field value>

_13

},

_13

// ...

_13

]

_13

}

_13

}`

**Example**

`_12

{

_12

"type": "Resource",

_12

"value": {

_12

"id": "0x3.GreatContract.GreatNFT",

_12

"fields": [

_12

{

_12

"name": "power",

_12

"value": { "type": "Int", "value": "1" }

_12

}

_12

]

_12

}

_12

}`

### Path[​](#path "Direct link to Path")

`_10

{

_10

"type": "Path",

_10

"value": {

_10

"domain": "storage" | "private" | "public",

_10

"identifier": "..."

_10

}

_10

}`

**Example**

`_10

{

_10

"type": "Path",

_10

"value": {

_10

"domain": "storage",

_10

"identifier": "flowTokenVault"

_10

}

_10

}`

### Type value[​](#type-value "Direct link to Type value")

`_10

{

_10

"type": "Type",

_10

"value": {

_10

"staticType": <type>

_10

}

_10

}`

**Example**

`_10

{

_10

"type": "Type",

_10

"value": {

_10

"staticType": {

_10

"kind": "Int"

_10

}

_10

}

_10

}`

### InclusiveRange[​](#inclusiverange "Direct link to InclusiveRange")

`_10

{

_10

"type": "InclusiveRange",

_10

"value": {

_10

"start": <start_value>,

_10

"end": <end_value>,

_10

"step": <step_value>

_10

}

_10

}`

**Example**

`_17

{

_17

"type": "InclusiveRange",

_17

"value": {

_17

"start": {

_17

"type": "Int256",

_17

"value": "10"

_17

},

_17

"end": {

_17

"type": "Int256",

_17

"value": "20"

_17

},

_17

"step": {

_17

"type": "Int256",

_17

"value": "5"

_17

}

_17

}

_17

}`

### Capability[​](#capability "Direct link to Capability")

`_10

{

_10

"type": "Capability",

_10

"value": {

_10

"id": <Number>,

_10

"address": "0x0", // as hex-encoded string with 0x prefix

_10

"borrowType": <type>,

_10

}

_10

}`

**Example**

`_10

{

_10

"type": "Capability",

_10

"value": {

_10

"id": "1",

_10

"address": "0x1",

_10

"borrowType": {

_10

"kind": "Int"

_10

}

_10

}

_10

}`

### Functions[​](#functions "Direct link to Functions")

`_10

{

_10

"type": "Function",

_10

"value": {

_10

"functionType": <type>

_10

}

_10

}`

Function values can only be exported — they cannot be imported.

**Example**

`_13

{

_13

"type": "Function",

_13

"value": {

_13

"functionType": {

_13

"kind": "Function",

_13

"typeID": "fun():Void",

_13

"parameters": [],

_13

"return": {

_13

"kind": "Void"

_13

}

_13

}

_13

}

_13

}`

## Types[​](#types "Direct link to Types")

### Simple Types[​](#simple-types "Direct link to Simple Types")

These are basic types such as `Int`, `String`, or `StoragePath`.

`_10

{

_10

"kind": <kind>

_10

}`

Where `kind` is one of:

* `Account`
* `AccountCapabilityController`
* `AccountKey`
* `Address`
* `AnyResource`
* `AnyResourceAttachment`
* `AnyStruct`
* `AnyStructAttachment`
* `Block`
* `Bool`
* `Capability`
* `CapabilityPath`
* `Character`
* `DeployedContract`
* `DeploymentResult`
* `Fix64`
* `FixedPoint`
* `FixedSizeUnsignedInteger`
* `HashAlgorithm`
* `HashableStruct`
* `Int`
* `Int128`
* `Int16`
* `Int256`
* `Int32`
* `Int64`
* `Int8`
* `Integer`
* `Never`
* `Number`
* `Path`
* `PrivatePath`
* `PublicKey`
* `PublicPath`
* `SignatureAlgorithm`
* `SignedFixedPoint`
* `SignedInteger`
* `SignedNumber`
* `StorageCapabilityController`
* `StoragePath`
* `String`
* `Type`
* `UFix64`
* `UInt`
* `UInt128`
* `UInt16`
* `UInt256`
* `UInt32`
* `UInt64`
* `UInt8`
* `Void`
* `Word128`
* `Word16`
* `Word256`
* `Word32`
* `Word64`
* `Word8`

**Example**

`_10

{

_10

"kind": "UInt8"

_10

}`

### Optional types[​](#optional-types "Direct link to Optional types")

`_10

{

_10

"kind": "Optional",

_10

"type": <type>

_10

}`

**Example**

`_10

{

_10

"kind": "Optional",

_10

"type": {

_10

"kind": "String"

_10

}

_10

}`

### Variable sized array types[​](#variable-sized-array-types "Direct link to Variable sized array types")

`_10

{

_10

"kind": "VariableSizedArray",

_10

"type": <type>

_10

}`

**Example**

`_10

{

_10

"kind": "VariableSizedArray",

_10

"type": {

_10

"kind": "String"

_10

}

_10

}`

### Constant sized array types[​](#constant-sized-array-types "Direct link to Constant sized array types")

`_10

{

_10

"kind": "ConstantSizedArray",

_10

"type": <type>,

_10

"size": <length of array>,

_10

}`

**Example**

`_10

{

_10

"kind": "ConstantSizedArray",

_10

"type": {

_10

"kind": "String"

_10

},

_10

"size": 3

_10

}`

### Dictionary types[​](#dictionary-types "Direct link to Dictionary types")

`_10

{

_10

"kind": "Dictionary",

_10

"key": <type>,

_10

"value": <type>

_10

}`

**Example**

`_10

{

_10

"kind": "Dictionary",

_10

"key": {

_10

"kind": "String"

_10

},

_10

"value": {

_10

"kind": "UInt16"

_10

}

_10

}`

### Composite types[​](#composite-types "Direct link to Composite types")

`_15

{

_15

"kind": "Struct" | "Resource" | "Event" | "Contract" | "StructInterface" | "ResourceInterface" | "ContractInterface",

_15

"type": "", // this field exists only to keep parity with the enum structure below; the value must be the empty string

_15

"typeID": "<fully qualified type ID>",

_15

"initializers": [

_15

<initializer at index 0>,

_15

<initializer at index 1>

_15

// ...

_15

],

_15

"fields": [

_15

<field at index 0>,

_15

<field at index 1>

_15

// ...

_15

],

_15

}`

**Example**

`_24

{

_24

"kind": "Resource",

_24

"type": "",

_24

"typeID": "0x3.GreatContract.GreatNFT",

_24

"initializers": [

_24

[

_24

{

_24

"label": "foo",

_24

"id": "bar",

_24

"type": {

_24

"kind": "String"

_24

}

_24

}

_24

]

_24

],

_24

"fields": [

_24

{

_24

"id": "foo",

_24

"type": {

_24

"kind": "String"

_24

}

_24

}

_24

]

_24

}`

### Field types[​](#field-types "Direct link to Field types")

`_10

{

_10

"id": "<name of field>",

_10

"type": <type>

_10

}`

**Example**

`_10

{

_10

"id": "foo",

_10

"type": {

_10

"kind": "String"

_10

}

_10

}`

### Parameter types[​](#parameter-types "Direct link to Parameter types")

`_10

{

_10

"label": "<label>",

_10

"id": "<identifier>",

_10

"type": <type>

_10

}`

**Example**

`_10

{

_10

"label": "foo",

_10

"id": "bar",

_10

"type": {

_10

"kind": "String"

_10

}

_10

}`

### Initializer types[​](#initializer-types "Direct link to Initializer types")

Initializer types are encoded as a list of parameters to the initializer.

`_10

[

_10

<parameter at index 0>,

_10

<parameter at index 1>,

_10

// ...

_10

]`

**Example**

`_10

[

_10

{

_10

"label": "foo",

_10

"id": "bar",

_10

"type": {

_10

"kind": "String"

_10

}

_10

}

_10

]`

### Function types[​](#function-types "Direct link to Function types")

`_11

{

_11

"kind": "Function",

_11

"typeID": "<function name>",

_11

"parameters": [

_11

<parameter at index 0>,

_11

<parameter at index 1>,

_11

// ...

_11

],

_11

"purity: "view" | undefined,

_11

"return": <type>

_11

}`

**Example**

`_17

{

_17

"kind": "Function",

_17

"typeID": "foo",

_17

"parameters": [

_17

{

_17

"label": "foo",

_17

"id": "bar",

_17

"type": {

_17

"kind": "String"

_17

}

_17

}

_17

],

_17

"purity": "view",

_17

"return": {

_17

"kind": "String"

_17

}

_17

}`

### Reference types[​](#reference-types "Direct link to Reference types")

`_12

{

_12

"kind": "Reference",

_12

"authorization": {

_12

"kind": "Unauthorized" | "EntitlementMapAuthorization" | "EntitlementConjunctionSet" | "EntitlementDisjunctionSet",

_12

"entitlements": [

_12

<entitlement at index 0>,

_12

<entitlement at index 1>

_12

// ...

_12

]

_12

},

_12

"type": <type>

_12

}`

**Example**

`_17

{

_17

"kind": "Reference",

_17

"authorization": {

_17

{

_17

"kind": "EntitlementMapAuthorization",

_17

"entitlements": [

_17

{

_17

"kind": "EntitlementMap",

_17

"typeID": "foo"

_17

}

_17

]

_17

}

_17

},

_17

"type": {

_17

"kind": "String"

_17

}

_17

}`

### Intersection types[​](#intersection-types "Direct link to Intersection types")

`_10

{

_10

"kind": "Intersection",

_10

"typeID": "<fully qualified type ID>",

_10

"types": [

_10

<type at index 0>,

_10

<type at index 1>,

_10

//...

_10

]

_10

}`

**Example**

`_20

{

_20

"kind": "Intersection",

_20

"typeID": "{0x1.FungibleToken.Receiver}",

_20

"types": [

_20

{

_20

"kind": "ResourceInterface",

_20

"typeID": "0x1.FungibleToken.Receiver",

_20

"fields": [

_20

{

_20

"id": "uuid",

_20

"type": {

_20

"kind": "UInt64"

_20

}

_20

}

_20

],

_20

"initializers": [],

_20

"type": ""

_20

}

_20

]

_20

}`

### Capability types[​](#capability-types "Direct link to Capability types")

`_10

{

_10

"kind": "Capability",

_10

"type": <type>

_10

}`

**Example**

`_13

{

_13

"kind": "Capability",

_13

"type": {

_13

"kind": "Reference",

_13

"authorization": {

_13

"kind": "Unauthorized",

_13

"entitlements": null

_13

},

_13

"type": {

_13

"kind": "String"

_13

}

_13

}

_13

}`

### Enum types[​](#enum-types "Direct link to Enum types")

`_12

{

_12

"kind": "Enum",

_12

"type": <type>,

_12

"typeID": "<fully qualified type ID>",

_12

"initializers":[],

_12

"fields": [

_12

{

_12

"id": "rawValue",

_12

"type": <type>

_12

}

_12

]

_12

}`

**Example**

`_16

{

_16

"kind": "Enum",

_16

"type": {

_16

"kind": "String"

_16

},

_16

"typeID": "0x3.GreatContract.GreatEnum",

_16

"initializers": [],

_16

"fields": [

_16

{

_16

"id": "rawValue",

_16

"type": {

_16

"kind": "String"

_16

}

_16

}

_16

]

_16

}`

### Repeated types[​](#repeated-types "Direct link to Repeated types")

When a composite type appears more than once within the same JSON type encoding, either because it is recursive or because it is repeated (e.g., in a composite field), the composite is instead represented by its type ID.

**Example**

`_20

{

_20

"type": "Type",

_20

"value": {

_20

"staticType": {

_20

"kind": "Resource",

_20

"typeID": "0x3.GreatContract.NFT",

_20

"fields": [

_20

{

_20

"id": "foo",

_20

"type": {

_20

"kind": "Optional",

_20

"type": "0x3.GreatContract.NFT" // recursive NFT resource type is instead encoded as an ID

_20

}

_20

}

_20

],

_20

"initializers": [],

_20

"type": ""

_20

}

_20

}

_20

}`

### Inclusive range types[​](#inclusive-range-types "Direct link to Inclusive range types")

`_10

{

_10

"kind": "InclusiveRange",

_10

"element": <integer_type>

_10

}`

**Example**

`_10

{

_10

"kind": "InclusiveRange",

_10

"element": {

_10

"kind": "Int"

_10

}

_10

}`

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/json-cadence-spec.md)

[Previous

Security Best Practices](/docs/security-best-practices)[Next

Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)

###### Rate this page

😞😐😊

* [Values](#values)
  + [Void](#void)
  + [Optional](#optional)
  + [Bool](#bool)
  + [String](#string)
  + [Address](#address)
  + [Integers](#integers)
  + [Fixed point numbers](#fixed-point-numbers)
  + [Array](#array)
  + [Dictionary](#dictionary)
  + [Composites (Struct, Resource, Event, Contract, Enum)](#composites-struct-resource-event-contract-enum)
  + [Path](#path)
  + [Type value](#type-value)
  + [InclusiveRange](#inclusiverange)
  + [Capability](#capability)
  + [Functions](#functions)
* [Types](#types)
  + [Simple Types](#simple-types)
  + [Optional types](#optional-types)
  + [Variable sized array types](#variable-sized-array-types)
  + [Constant sized array types](#constant-sized-array-types)
  + [Dictionary types](#dictionary-types)
  + [Composite types](#composite-types)
  + [Field types](#field-types)
  + [Parameter types](#parameter-types)
  + [Initializer types](#initializer-types)
  + [Function types](#function-types)
  + [Reference types](#reference-types)
  + [Intersection types](#intersection-types)
  + [Capability types](#capability-types)
  + [Enum types](#enum-types)
  + [Repeated types](#repeated-types)
  + [Inclusive range types](#inclusive-range-types)