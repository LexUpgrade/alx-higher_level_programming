#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size')
} else {
  const x = parseInt(process.argv[2]);
  let i;
  for (i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
