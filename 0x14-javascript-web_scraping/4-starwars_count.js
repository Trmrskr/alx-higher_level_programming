#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
