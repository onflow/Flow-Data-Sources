# Source: https://github.com/onflow/cadence/blob/master/sema/gen/testdata/nested/test.cdc

```
struct Foo {
    /// foo
    access(all) fun foo()

    /// Bar
    access(all) let bar: Foo.Bar

    struct Bar {
        /// bar
        access(all) fun bar()
    }
}

```