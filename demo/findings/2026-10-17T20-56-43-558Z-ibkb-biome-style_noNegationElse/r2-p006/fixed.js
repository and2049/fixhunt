class Test {
  #flag = false
  static get value() { return 1 }
  check() {
    if (Test.value) {
      return this.#flag ? 'c' : 'd'
    } else {
      return this.#flag ? 'a' : 'b'
    }
  }
}
console.log(new Test().check())
