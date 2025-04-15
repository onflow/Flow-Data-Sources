# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/index.js

```
import * as fcl from '@onflow/fcl'
import { readCadenceScripts, replaceAddress } from './cadence'

let scriptsMap = null

export const exportScripts = async (addressMapping = {}) => {
  scriptsMap = await readCadenceScripts('./', addressMapping)
  return scriptsMap
}

export const queryScripts = async (scriptPath, args, addressMapping = {}) => {
  let pathArr = scriptPath.split('/')
  if (scriptsMap == null) {
    scriptsMap = await readCadenceScripts()
  }

  let script = scriptsMap[pathArr[0]][pathArr[1]]
  if (script == null) {
    throw new Error(`Script ${path} not found`)
  }
  script = replaceAddress(script, addressMapping)
  const response = await fcl.send([fcl.script(script), fcl.args(args)])
  return await fcl.decode(response)
}

export const exportScript = async (scriptPath, addressMapping = {}) => {
  let pathArr = scriptPath.split('/')
  if (scriptsMap == null) {
    scriptsMap = await readCadenceScripts()
  }
  let script = scriptsMap[pathArr[0]][pathArr[1]]
  script = replaceAddress(script, addressMapping)
  return script
}

```