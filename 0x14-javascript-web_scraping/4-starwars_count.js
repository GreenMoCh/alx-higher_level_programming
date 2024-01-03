#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body);
    const filmsWithWedge = filmsData.results.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18')
    );
    console.log(filmsWithWedge.length);
  }
});
