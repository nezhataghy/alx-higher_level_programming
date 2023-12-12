#!/usr/bin/node
const dict = require('./101-data.js').dict;
const my_Dict = {};
for (const key in dict) {
  if (my_Dict[dict[key]] === undefined) {
    my_Dict[dict[key]] = [key];
  } else {
    my_Dict[dict[key]].push(key);
  }
}
console.log(my_Dict);
