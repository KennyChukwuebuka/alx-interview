#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      if (response.statusCode !== 200) {
        return reject(new Error(`Error: Unable to fetch data (status code: ${response.statusCode})`));
      }

      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(new Error(`Error: Unable to fetch data (status code: ${response.statusCode})`));
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const characterPromises = characters.map(url => getCharacterName(url));

  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});
