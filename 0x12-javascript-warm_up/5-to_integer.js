#!/usr/bin/node
const myVal = parseInt(process.argv[2]);
if (isNaN(myVal) !== true) {
  console.log(`My number: ${myVal}`);
} else {
  console.log('Not a number');
}
