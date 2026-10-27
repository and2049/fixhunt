class Test {
  #flag = false
  static get value() { return 1 }
  check() {
    if (!Test.value) {
      return this.#flag ? 'a' : 'b'
    } else {
      return this.#flag ? 'c' : 'd'
    }
  }
}
console.log(new Test().check())
