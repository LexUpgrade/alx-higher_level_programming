#!/usr/bin/node
const path = require('path');
const fs = require('fs');

const prog = path.basename(__filename);
const argv = process.argv;
const filename = path.basename(argv[2]);
const data = argv[3];

if (argv.length < 4) {
  console.log(`Usage: ./${prog} <filename> <data-as-string>`);
} else {
  fs.writeFile(filename, data, 'utf-8', (err) => {
    if (err) console.log(err);
  });
}
