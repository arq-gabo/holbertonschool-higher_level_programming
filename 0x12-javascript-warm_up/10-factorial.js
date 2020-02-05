#!/usr/bin/node
const myVal = parseInt(process.argv[2]);
function factorial (myVal) {
  if (myVal <= 1 || isNaN(myVal) === true) {
    return (1);
  }
  return (myVal * factorial(myVal - 1));
}
console.log(factorial(myVal));
