#!/usr/bin/node
let nOfJobs = 0;

exports.logMe = function (item) {
  console.log(`${nOfJobs}: ${item}`);
  nOfJobs++;
};
