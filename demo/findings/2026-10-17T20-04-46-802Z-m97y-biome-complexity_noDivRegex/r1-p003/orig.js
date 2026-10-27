async function* gen() {
  yield /=/.test('abc');
  await Promise.resolve();
  yield /=/.test('def');
}
gen().next().then(({value}) => console.log(value));
