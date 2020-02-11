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

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
module.exports = Rectangle;
