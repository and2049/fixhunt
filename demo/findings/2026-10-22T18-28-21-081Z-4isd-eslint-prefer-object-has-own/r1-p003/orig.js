async function* gen() {
  let obj = {};
  obj[await Promise.resolve('key')] = 1;
  if (Object.prototype.hasOwnProperty.call(obj, await Promise.resolve('key'))) {
    yield 1;
  }
}
gen().next().then(({value}) => console.log(value));
