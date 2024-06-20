#!/usr/bin/node
exports.esrever = function (list) {
  const esrever = [];
  let i, j;
  for (i = 0, j = list.length - 1; i < list.length && j >= 0; i++, j--) {
    esrever[i] = list[j];
  }
  return esrever;
};
