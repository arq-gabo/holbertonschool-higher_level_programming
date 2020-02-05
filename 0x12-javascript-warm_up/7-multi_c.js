#!/usr/bin/node
const myVar = process.argv[2];
if (!myVar) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < myVar; a++) {
    console.log('C is fun');
  }
}
