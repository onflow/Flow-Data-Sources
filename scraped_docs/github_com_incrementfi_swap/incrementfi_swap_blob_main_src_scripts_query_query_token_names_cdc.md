# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_token_names.cdc

```

access(all) fun main(queryAddr: Address): [String] {
    let names = getAccount(queryAddr).contracts.names

    let tokenNames: [String] = []

    let colon: UInt8 = 58
    let space: UInt8 = 32
    let brace: UInt8 = 123
    /// utf8 code of "FungibleToken"
    let tokenIndentifier: [UInt8] = [70, 117, 110, 103, 105, 98, 108, 101, 84, 111, 107, 101, 110] 
    let indentifierLength = tokenIndentifier.length

    for name in names {
        let code = getAccount(queryAddr).contracts.get(name: name)!.code
        let codeLength = code.length
    

        var isToken = false

        var i = 13
        while(i < codeLength-1) {
            // only check the begnning of the code, terminate at "{"
            if code[i] == brace {
                break
            }
            // search code: "pub contract XXX:(\s*)FungibleToken {"
            if code[i] == colon && code[i+1] == space {
                i = i + 1
                while(code[i] == space && i < codeLength) {
                    i = i + 1
                }
                var j = 0
                while(j < indentifierLength && i < codeLength) {
                    if code[i] == tokenIndentifier[j] {
                        i = i + 1
                        j = j + 1
                    } else {
                        break
                    }
                }
                if j == indentifierLength && (code[i]==space || code[i]==brace) {
                    isToken = true
                    break
                }

            } else {
                i = i + 1
            }
            
        }
        if isToken {
            tokenNames.append(name)
        }
    }
    log(tokenNames)
    return tokenNames
}
```