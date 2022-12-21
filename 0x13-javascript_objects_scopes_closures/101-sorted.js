#!/usr/bin/node

const dictionary = require('./101-data').dict;

let new_dict = {};

for (const key in dictionary) {
  if (new_dict[dictionary[key]] != undefined) {
    new_dict[dictionary[key]].push(key);
  } else {
    new_dict[dictionary[key]] = [key];
  }
}

console.log(new_dict);
