class Base {
  static baseProp = 'base'
}
class Derived extends Base {
  static staticProp = Object.assign({}, {derived: true})
  static {
    console.log(Base.baseProp, Derived.staticProp.derived)
  }
  #private = Object.assign({}, {secret: 42})
  constructor() {
    super()
    console.log(this.#private.secret)
  }
}
new Derived()
