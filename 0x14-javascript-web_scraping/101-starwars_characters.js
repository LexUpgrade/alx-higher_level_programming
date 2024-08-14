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
        const characters = data.characters;
        printCharacters(characters, 0);
      } else {
        console.log(`An error occured. Status Code: ${response.statusCode}`);
      }
    }
  });
}

function printCharacters (listOfCharacters, index) {
  if (index >= listOfCharacters.length) {
    return;
  }
  request(listOfCharacters[index], function (error, response, body) {
    if (error) {
      console.error(error);
    } else {
      if (response.statusCode === 200) {
        console.log(JSON.parse(body).name);
        printCharacters(listOfCharacters, ++index);
      } else {
        console.log(`An error occured while fetching ${response.url} === with status code: ${response.statusCode}`);
      }
    }
  });
}
