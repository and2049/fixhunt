class C {
  static #x;
  static {
    try { process = { exit: () => {} }; } catch (e) {}
    C.#x = process;
  }
  constructor() { this.y = process.pid ?? 0; }
}
new C();
console.log(C.#x?.pid ?? 'null');
