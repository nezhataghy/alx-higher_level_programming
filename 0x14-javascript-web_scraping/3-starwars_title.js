#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (err, data, body) {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
