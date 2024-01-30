#!/usr/bin/node
let fs = require('fs');

/* filePath : process.argv[2]; */
/* content : process.argv[3]; */

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
    if (err) {
        console.log(err);
    }
});
