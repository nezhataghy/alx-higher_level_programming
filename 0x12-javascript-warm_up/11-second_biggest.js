#!/usr/bin/node
const list = process.argv.slice(2);

if (list.length === 0 | list.length === 1) {
  console.log(0);
} else {
  list.sort(function (a, b) {
    return a - b;
  });

  for (let i = 0; list.length > i; i++) {
    list[i] = parseInt(list[i], 10);
  }
  console.log(list[list.length - 2]);
}
