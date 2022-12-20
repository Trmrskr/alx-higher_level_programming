#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let symbol = 'X';
    for (let i = 0; i < this.width - 1; i++) {
      symbol += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(symbol);
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
