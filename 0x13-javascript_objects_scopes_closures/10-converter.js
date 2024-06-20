#!/usr/bin/node

exports.converter = function (base) {
  return (value) => {
    return value.toString(base);
  };
};
