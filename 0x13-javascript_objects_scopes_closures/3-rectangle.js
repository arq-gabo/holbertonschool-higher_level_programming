#!/usr/bin/node
const Rectangle = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let txt = '';
    for (let i = 0; i < this.width; i++) {
      txt += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(txt);
    }
  }
};
module.exports = Rectangle;
