#!/usr/bin/node

const len = process.argv.length;

if (len < 4) {
  console.log('0');
} else {
  const numbers = [];
  for (let i = 2; i < len; i++) {
    numbers[i - 2] = parseInt(process.argv[i]);
  }
  numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
