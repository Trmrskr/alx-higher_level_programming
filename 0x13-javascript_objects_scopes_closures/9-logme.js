#!/usr/bin/node

let counter = 0;

exports.logme = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
}
