#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let a = list.length - 1; a >= 0; a--) {
    arr.push(list[a]);
  }
  return (arr);
};
