#!/usr/bin/node
args = process.argv[2]
if (isNaN(parseInt(args))) {
    console.log('Not a number');
} else {
    console.log('My number: ' + parseInt(args));
}
