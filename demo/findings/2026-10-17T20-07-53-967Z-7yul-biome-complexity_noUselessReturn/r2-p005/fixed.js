function* f() {
  yield 1;
}
const it = f();
console.log(it.next().value);
console.log(it.next().done ? 'done' : it.next().value);
