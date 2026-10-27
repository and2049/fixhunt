function* gen() {
  if (true) {
    if (false) { yield 1; }
    yield 2;
  }
}
let g = gen();
console.log([...g]);
