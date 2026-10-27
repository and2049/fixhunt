async function* gen() {
  yield {}
  yield 1;
}
gen().next().then(r => console.log(r.value));
