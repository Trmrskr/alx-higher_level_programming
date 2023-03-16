#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  const noOfTimes = parseInt(x);
  for (let i = 0; i < noOfTimes; i++) {
    console.log('C is fun');
  }
}
