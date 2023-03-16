#!/usr/bin/node
/* print the first argument passed else print No argument */

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
