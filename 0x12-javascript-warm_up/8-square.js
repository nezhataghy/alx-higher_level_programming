#!/usr/bin/node
const numb = process.argv[2];
let n = 0; let m = 0;

if (isNaN(parseInt(numb))) {
  console.log('Missing number of occurrences');
} else {
  while (n < numb) {
    let txt = '';
    while (m < numb) {
      txt = txt + 'X';
      m++;
    }
    console.log('X');
    n++;
  }
}
