#!/usr/bin/node
const numb = process.argv[2];
let n = 0;

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (n < numb) {
    console.log('C is fun');
    n++;
  }
}
