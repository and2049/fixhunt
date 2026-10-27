class Base {
  constructor() { this.public = 1; }
}
class Derived extends Base {
  #private = 2;
  static staticField = 3;
  constructor() {
    super();
    console.log('super.public:', Object.assign({}, super).public);
    console.log('super.public:', ({ ...super }).public);
  }
}
new Derived();
