function* g() {
  yield 1;
  return;
}
const it = g();
console.log(it.next().value); // 1
console.log(it.next().done, it.next().value); // true undefined
