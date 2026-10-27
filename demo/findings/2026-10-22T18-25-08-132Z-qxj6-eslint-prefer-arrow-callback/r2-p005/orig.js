function* gen() {
  yield [1,2].map(function*(v) { yield v * 2; });
}
const g = gen();
console.log(g.next().value);
