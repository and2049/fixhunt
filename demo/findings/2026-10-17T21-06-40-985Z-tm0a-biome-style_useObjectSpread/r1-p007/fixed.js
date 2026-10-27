class Base {
  static baseProp = 'base'
}
class Derived extends Base {
  static staticProp = ({derived: true,})
  static {
    console.log(Base.baseProp, Derived.staticProp.derived)
  }
  #private = ({secret: 42,})
  constructor() {
    super()
    console.log(this.#private.secret)
  }
}
new Derived()
