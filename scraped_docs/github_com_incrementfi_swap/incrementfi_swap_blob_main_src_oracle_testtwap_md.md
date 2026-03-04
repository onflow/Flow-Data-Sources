# Source: https://github.com/IncrementFi/Swap/blob/main/src/oracle/TestTwap.md

import os
import json
import re
import DeployTools
import Config

Network = Config.Network
ContractNameToAddress = DeployTools.ExtractContractNameToAddress('./flow.json', Network)


with open('./flow.json', 'r') as f:
    flow_json = json.load(f)


print('add small liquidity')
cmd = 'node ./utils/js/AddLiquidity.js emulator "A.f8d6e0586b0a20c7.FUSD" "A.f8d6e0586b0a20c7.USDC" "0.1" "0.1" "0.0" "0.0" "184467440737"'
os.system(cmd)
#os.system('flow scripts execute ./src/')
#os.system('flow scripts execute ./cadence/oracle/query_twap_info.cdc "A.f8d6e0586b0a20c7.FUSD" "A.f8d6e0586b0a20c7.USDC"')


#node ./utils/js/AddLiquidity.js emulator "A.f8d6e0586b0a20c7.FUSD" "A.f8d6e0586b0a20c7.USDC" "0.1" "1" "10" "0.0" "184467440737"
#node ./utils/js/QueryTimestamp.js emulator

#flow transactions send ./cadence/oracle/initPrice.cdc

#flow transactions send ./cadence/oracle/updatePrice.cdc

#flow scripts execute ./cadence/oracle/quote.cdc "A.f8d6e0586b0a20c7.FUSD"