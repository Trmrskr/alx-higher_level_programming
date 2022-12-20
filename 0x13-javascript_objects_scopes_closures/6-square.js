#!/usr/bin/node
const Sqware = require('./5-square.js');

module.exports = class Square extends Sqware {
  constructor (size) {
    super(size);
  }

  charPrint(c) {
    super.print(c);
  }
};
