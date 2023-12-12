#!/usr/bin/node
const fs = require('fs');

const file1 = fs.readFileSync(process.argv[2], 'utf-8').toString();
const file2 = fs.readFileSync(process.argv[3], 'utf-8').toString();
fs.writeFileSync(process.argv[4], file1 + file2);
