#!/usr/bin/node
const numb = process.argv[2];
let n = 0;

if (isNaN(numb)) {
  console.log('Missing size');
} else {
  while (n < numb) {
    let txt = '';
    for (let m = 0; m < numb; m++) {
      txt = txt + 'X';
    }
    console.log(txt);
    n++;
  }
}
