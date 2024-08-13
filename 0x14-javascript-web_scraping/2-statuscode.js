#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, respond, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${respond.statusCode}`);
  }
});
