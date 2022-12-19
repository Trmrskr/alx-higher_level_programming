#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const len = process.argv.length;

if (len < 4) {
  console.log('NaN');
} else if (isNaN(a) || isNaN(b) || a === undefined || b === undefined) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
