#!/usr/bin/node
/* Prints the title of a Star Wars movie where the episode number matches a given
 * integer passed as argument
 */
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(apiUrl, (error, responds, data) => {
  if (error) {
    console.log(error);
  } else {
    const jsonObject = JSON.parse(data);
    console.log(jsonObject.title);
  }
});
