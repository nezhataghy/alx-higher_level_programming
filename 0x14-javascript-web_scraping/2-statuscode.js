#!/usr/bin/node

const request = require('request');
/* url : process.argv[2]; */

request(process.argv[2], function (err, data, body) {
    if (err) {
        console.log(err);
    } else {
        console.log('code: ' + data.statusCode);
    }
});
