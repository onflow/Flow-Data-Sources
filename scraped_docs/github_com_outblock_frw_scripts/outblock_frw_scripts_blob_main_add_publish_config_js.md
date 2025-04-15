# Source: https://github.com/Outblock/FRW-scripts/blob/main/add-publish-config.js

```
const fs = require('fs');
const path = require('path');

// Function to update package.json files with publishConfig
const updatePackageJson = (dir) => {
  const packageJsonPath = path.join(dir, 'package.json');

  if (fs.existsSync(packageJsonPath)) {
    const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));

    // Check if "publishConfig" exists and if not, add it
    if (!packageJson.publishConfig) {
      packageJson.publishConfig = { access: 'public' };
      
      // Write the updated package.json file
      fs.writeFileSync(packageJsonPath, JSON.stringify(packageJson, null, 2), 'utf8');
      console.log(`Updated publishConfig in ${packageJsonPath}`);
    } else {
      console.log(`publishConfig already exists in ${packageJsonPath}`);
    }
  }
};

// Recursively find all package.json files in the directory
const findPackageJsonFiles = (dir) => {
  fs.readdirSync(dir).forEach((file) => {
    const fullPath = path.join(dir, file);

    // Ignore node_modules directories
    if (fs.statSync(fullPath).isDirectory() && file !== 'node_modules') {
      // Recurse into subdirectories
      findPackageJsonFiles(fullPath);
    } else if (file === 'package.json') {
      // Update package.json file
      updatePackageJson(dir);
    }
  });
};

// Start at the root of your monorepo (current directory)
findPackageJsonFiles(process.cwd());
```