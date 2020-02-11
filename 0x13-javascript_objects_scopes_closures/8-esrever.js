#!/usr/bin/node
exports.esrever = function (list) {
  let arr = [];
  for (let a = list.lenght - 1; a >= 0; a--){
    arr.push(list[a]);
  }
  return (arr);
};
