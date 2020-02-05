#!/usr/bin/node
const myVal = process.argv;
if (myVal.length > 3) {
  console.log(myVal.sort((a, b) => b - a).slice(3)[0]);
} else {
  console.log(0);
}
