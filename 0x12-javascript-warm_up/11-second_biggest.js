#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const numbers = [];
  for (let i = 2; i < size; i++) {
    numbers[i - 2] = parseInt(process.argv[i]);
  }
  numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
