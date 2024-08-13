#!/usr/bin/node

const fs = require('node:fs');
const path = require('node:path');

const app = path.basename(__filename);
if (process.argv.length !== 3) {
  console.error(`Usage: ./${app} <filename>`);
} else {
  const filename = path.basename(process.argv[2]);
  fs.readFile(filename, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
