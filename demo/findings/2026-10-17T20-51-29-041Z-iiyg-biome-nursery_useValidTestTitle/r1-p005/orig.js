let logs = [];
function side() {
  logs.push('side');
  return 'ok';
}
function test(title, fn) {
  console.log('got:', title);
  fn();
}
test(`${side()}`, () => { logs.push('fn'); });
console.log(logs.join(','));
