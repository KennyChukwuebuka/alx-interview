#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch data (status code: ${response.statusCode})`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Error: Unable to fetch data (status code: ${response.statusCode})`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
