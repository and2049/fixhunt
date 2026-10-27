class TestSuite {
  static #count = 0;
  static {
    test('static init', () => { TestSuite.#count++; });
  }
  constructor() {
    test('instance', () => { this.value = TestSuite.#count; });
  }
  get value() { return this._value; }
  set value(v) { this._value = v; }
}
const s = new TestSuite();
console.log(s.value, TestSuite.#count);
