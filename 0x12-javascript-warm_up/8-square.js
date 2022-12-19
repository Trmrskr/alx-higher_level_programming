#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x) || x === undefined) {
  console.log('Missing size');
}
let pstr = 'X';
for (let i = 0; i < x - 1; i++) {
  pstr += 'X';
}
for (let j = 0; j < x; j++) {
  console.log(pstr);
}
