#!/usr/bin/node
/* Prints the number of movies where the character "Wedge Antilles" is present */
const request = require('request');
const path = require('path');

if (process.argv.length < 2) {
  console.log(`./${path.basename(__filename)} <api-url>`);
} else {
  request
    .get(process.argv[2])
    .on('error', (error) => {
      console.error(error);
    })
    .on('response', (response) => {
      let body = '';
      response.on('data', (chunk) => {
        body += chunk;
      });

      response.on('end', () => {
        try {
          const data = JSON.parse(body);
          const list = [];
          for (const datum of data.results) {
            list.push(datum.characters);
          }
          let num = 0;
          for (const item of list) {
            if (item.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
              num += 1;
            }
          }
          console.log(num);
        } catch (error) {
          console.error(error);
        }
      });
    });
}
