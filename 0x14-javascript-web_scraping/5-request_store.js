#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const nameFile = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(nameFile, response.body, 'utf8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
