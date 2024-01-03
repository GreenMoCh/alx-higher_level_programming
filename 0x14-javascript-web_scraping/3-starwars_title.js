#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const movieID = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);

    if (movieData.title) {
      console.log(movieData.title);
    } else {
      console.error('Invalid movie ID');
    }
  }
});
