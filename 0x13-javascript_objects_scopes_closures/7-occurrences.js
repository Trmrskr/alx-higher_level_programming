#!/usr/bin/node

exports.occurrences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
