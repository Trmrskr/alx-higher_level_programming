#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  let fileContents = '';

  fileContents = fileContents.concat(fs.readFileSync(process.argv[2]));
  fileContents = fileContents.concat(fs.readFileSync(process.argv[3]));

  fs.writeFileSync(process.argv[4], fileContents);
}
