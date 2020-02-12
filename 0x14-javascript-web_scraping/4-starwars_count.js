#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntilles = '/18/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const count = JSON.parse(response.body).count;
    const swJson = JSON.parse(response.body).results;
    let mvCount = 0;
    for (let a = 0; a < count; a++) {
      const characters = swJson[a].characters;
      for (const character of characters) {
        if (character.endsWith(wedgeAntilles)) {
          mvCount++;
        }
      }
    }
    console.log(mvCount);
  }
});
