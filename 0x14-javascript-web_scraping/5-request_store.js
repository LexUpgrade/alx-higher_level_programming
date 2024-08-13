#!/usr/bin/node
const request = require('request');
const path = require('path');
const fs = require('fs');

if (process.argv.length < 3) {
  console.error(`Usage: ./${path.basename(__filename)} <url> <filename>`);
} else {
  request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
}
