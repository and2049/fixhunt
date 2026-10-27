function* gen() {
  yield 1;
}
const g = gen();
console.log(g.next().value);
