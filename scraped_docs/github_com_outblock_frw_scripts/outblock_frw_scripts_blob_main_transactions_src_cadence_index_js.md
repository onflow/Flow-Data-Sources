# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/index.js

```
import fs from 'fs'
import path from 'path'

const fsPromises = fs.promises

let cadebceScripts = {}

const underscoreToCamelCase = (fileName) => {
  let name = fileName.replace(/_([a-z])/g, function (match, letter) {
    return letter.toUpperCase()
  })

  name = name.replace('Nft', 'NFT')
  name = name.replace('Ft', 'FT')

  return name
}

const readDirRecursive = async (dirPath, addressMapping) => {
  // let resolvedPath = path.resolve(dirPath)

  let files = await fsPromises.readdir(dirPath)

  for (file of files) {
    const filePath = path.join(dirPath, file)

    let stats = await fsPromises.stat(filePath)
    // console.log(stats)
    if (stats.isDirectory()) {
      await readDirRecursive(filePath, addressMapping)
    } else {
      if (filePath.indexOf('.cdc') == -1 || filePath.indexOf('_test.cdc') > 0)
        continue
      let fileContent = await fsPromises.readFile(filePath, 'utf8')
      fileContent = replaceAddress(fileContent, addressMapping)
      // console.log(`Content of ${filePath}: ${data}`)
      const pathArr = filePath.split('/')
      const key = pathArr[pathArr.length - 2]
      let fileName = pathArr[pathArr.length - 1].split('.')[0]
      fileName = underscoreToCamelCase(fileName)
      // const base64Script = base64encode(fileContent)
      if (cadebceScripts[key]) {
        cadebceScripts[key] = {
          ...cadebceScripts[key],
          [fileName]: fileContent,
        }
      } else {
        cadebceScripts[key] = { [fileName]: fileContent }
      }
    }
  }
  return cadebceScripts
}

export const readCadenceScripts = async (path = './', addressMapping) => {
  return await readDirRecursive(path)
}

export const readScript = async (path, addressMapping) => {
  const fileContent = await fsPromises.readFile(path, 'utf8')
  return replaceAddress(fileContent, addressMapping)
}

export const replaceAddress = (script, addressMapping = {}) => {
  let keys = Object.keys(addressMapping)

  keys.forEach((key) => {
    let addr = addressMapping[key]
    if (addr) {
      const regex = new RegExp(`${key}\n`, 'g')
      script = script.replace(regex, `${addressMapping[key]}\n`)
    }
  })

  return script
}

```