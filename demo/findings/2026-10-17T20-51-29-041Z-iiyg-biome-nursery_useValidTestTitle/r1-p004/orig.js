let count = 0;
function getTitle() {
  count++;
  return 'test' + count;
}
function test(title, fn) {
  console.log('title:', title);
  fn();
}
test(getTitle(), () => { console.log('fn ran'); });
console.log('count:', count);
