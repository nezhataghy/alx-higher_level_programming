#!/usr/bin/node

let fs = require('fs');

fs.readFile(process.argv[2], function (err, data) {
    console.log(err || data.toString());
});
