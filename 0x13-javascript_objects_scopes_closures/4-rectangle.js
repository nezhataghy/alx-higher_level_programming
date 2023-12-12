#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let ligne = '';
      for (let j = 0; j < this.width; j++) {
        ligne += 'X';
      }
      console.log(ligne);
    }
  }

  rotate () {
    const variable = this.height;
    this.height = this.width;
    this.width = variable;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
