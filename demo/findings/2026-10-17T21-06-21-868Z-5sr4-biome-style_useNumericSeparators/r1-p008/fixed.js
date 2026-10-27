async function* gen() {
  yield 12_345;
  yield await 67_890;
}
(async() => {
  for await (const v of gen()) console.log(v);
})();
