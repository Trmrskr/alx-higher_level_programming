#!/usr/bin/node

function factorial (n) {
  if (n === 1 || n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const x = process.argv[2];

if (isNaN(x) || x === undefined) {
  console.log(1);
} else {
  console.log(factorial(x));
}
