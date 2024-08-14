#!/usr/bin/node
const request = require('request');
const path = require('path');

if (process.argv.length < 2) {
  console.log(`Usage: ./${path.basename(__filename)} <Movie ID>`);
} else {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      if (response.statusCode === 200) {
        const data = JSON.parse(body);
        const character = data.characters;
        character.forEach((personUrl) => {
          request(personUrl, function (error, response, body) {
            if (error) {
              console.error(error);
            } else {
              if (response.statusCode === 200) {
                console.log(JSON.parse(body).name);
              } else {
                console.log(`An error occured. Status code: ${response.statusCode}`);
              }
            }
          });
        });
      } else {
        console.log(`An error occured. Status code: ${response.statusCode}`);
      }
    }
  });
}
