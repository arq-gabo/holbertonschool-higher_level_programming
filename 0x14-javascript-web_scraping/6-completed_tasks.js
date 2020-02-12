#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {}
  const todoJSON = JSON.parse(response.body);
  const todoDict = {};
  for (const el of todoJSON) {
    if (el.completed) {
      if (typeof (todoDict[el.userId]) === 'undefined') {
        todoDict[el.userId] = 0;
      }
      todoDict[el.userId]++;
    }
  }
  console.log(todoDict);
});
