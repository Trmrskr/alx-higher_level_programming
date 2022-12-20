#!/usr/bin/node
const Sqware = require('./5-square.js');

module.exports = class Square extends Sqware {
  charPrint (c) {
    super.print(c);
  }
};
