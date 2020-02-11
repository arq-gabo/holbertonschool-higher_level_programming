#!/usr/bin/node
const Square2 = require('./5-square.js');
const Square = class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    let txt = '';
    for (let a = 0; a < this.width; a++) {
      txt += c;
    }
    for (let b = 0; b < this.width; b++) {
      console.log(txt);
    }
  }
};

module.exports = Square;
