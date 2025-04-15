# Source: https://github.com/Outblock/FRW-scripts/blob/main/package.json

```
{
  "workspaces": [
    "./scripts/*",
    "./scriptTest/*",
    "./transactions/*",
    "./transactionTest/*",
    "./temp/*"
  ],
  "type": "module",
  "scripts": {
    "build": "pnpm build",
    "changeset": "changeset",
    "release": "npm run build && npm run changeset publish"
  },
  "dependencies": {
    "@changesets/cli": "^2.26.2",
    "semver": "^7.6.3"
  },
  "publishConfig": {
    "access": "public"
  }
}
```