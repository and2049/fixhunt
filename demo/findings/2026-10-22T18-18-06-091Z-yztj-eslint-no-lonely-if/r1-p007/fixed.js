function* gen() {
  yield 1;
  if (false) {
    yield 2;
  } else if (true) {
      yield 3;
    }
  yield 4;
}
const it = gen();
console.log([...it].join(','));
