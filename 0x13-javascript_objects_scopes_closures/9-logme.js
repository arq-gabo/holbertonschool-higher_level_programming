#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  if (typeof (count) !== 'undefined') {
    console.log(count + ': ' + item);
    count++;
  } else {
    count = 0;
  }
};
