#!/usr/bin/node
const myVal = parseInt(process.argv[2]);
if (isNaN(myVal) !== true) {
  for (let a = 0; a < myVal; a++) {
    let txt = '';
    for (let b = 0; b < myVal; b++) {
      txt += 'X';
    }
    console.log(txt);
  }
} else {
  console.log('Missing size');
}
