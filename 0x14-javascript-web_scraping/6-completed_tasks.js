#!/usr/bin/node
const request = require('request');
const path = require('path');

if (process.argv.length < 2) {
  console.error(`Usage: ./${path.basename(__filename)} <apu-url>`);
} else {
  request(process.argv[2], function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      if (response.statusCode === 200) {
        const data = JSON.parse(body);
        const completed = {};
        for (const datum of data) {
          if (datum.completed) {
            if (completed[datum.userId] === undefined) {
              completed[datum.userId] = 1;
            } else {
              completed[datum.userId]++;
            }
          }
        }
        console.log(completed);
      } else {
        console.log(`An error occured. Status code: ${response.statusCode}`);
      }
    }
  });
}
