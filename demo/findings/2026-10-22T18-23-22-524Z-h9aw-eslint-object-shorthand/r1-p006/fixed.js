const obj = {
  *g() {
    yield 1;
    yield 2;
  }
};
const it = obj.g();
console.log(it.next().value, it.next().value, it.next().done);
