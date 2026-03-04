# Source: https://github.com/onflow/cadence/blob/master/tools/staged-contracts-report-printer/README.md

# Readme

A tool that takes in a JSON report produced from staged contract migration, and outputs a more
human-readable report in Markdown format.

```sh
go run . --report /path/to/staged-contracts-migrator_report.json
```

This will produce a Markdown format report with the same name, but with the makdown extension.
e.g: `/path/to/staged-contracts-migrator_report.md`