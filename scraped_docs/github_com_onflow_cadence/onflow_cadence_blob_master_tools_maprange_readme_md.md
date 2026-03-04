# Source: https://github.com/onflow/cadence/blob/master/tools/maprange/README.md

# maprange

A Go analyzer which detects uses of for-range statements over maps.
For such statements, iteration order is undefined / nondeterministic. 
