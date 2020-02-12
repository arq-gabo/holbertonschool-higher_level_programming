#!/usr/bin/node
const request = require('request');
const numberEp = process.argv[2];
const url = 'https://swapi.co/api/films/' + numberEp;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const swJson = JSON.parse(response.body);
    console.log(swJson.title);
  }
});
