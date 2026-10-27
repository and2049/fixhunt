async function* gen() {
  yield 12345;
  yield await 67890;
}
(async() => {
  for await (const v of gen()) console.log(v);
})();
