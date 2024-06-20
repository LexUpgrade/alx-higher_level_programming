#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let s = '';
        for (let j = 0; j < this.height; j++) {
          s += c;
        }
        console.log(s);
      }
    }
  }
}

module.exports = Square;
