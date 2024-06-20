#!usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i++ < this.height) {
      let r = '';
      let j = 0;
      while (j++ < this.width) {
        r += 'X';
      }
      console.log(r);
    }
  }
}

module.exports = Rectangle;
