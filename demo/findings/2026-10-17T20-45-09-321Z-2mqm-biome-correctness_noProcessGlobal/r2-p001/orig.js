class C {
  static #p = process;
  static {
    console.log(C.#p === process ? 'same' : 'diff');
  }
}
