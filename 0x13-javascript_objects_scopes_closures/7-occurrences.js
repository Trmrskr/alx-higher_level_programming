#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => {
  return list.filter(x => x === searchElement).length;
};
