#!/usr/bin/node

const dictionary = require('./101-data').dict;

const newDict = {};

for (const key in dictionary) {
  if (newDict[dictionary[key]] !== undefined) {
    newDict[dictionary[key]].push(key);
  } else {
    newDict[dictionary[key]] = [key];
  }
}

console.log(newDict);
