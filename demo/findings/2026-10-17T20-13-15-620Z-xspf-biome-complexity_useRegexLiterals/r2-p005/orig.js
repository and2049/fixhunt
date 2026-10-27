let count = 0;
function getPattern() {
  count++;
  return 'a';
}
function getFlags() {
  count++;
  return 'g';
}
try {
  console.log(new RegExp(getPattern(), getFlags()).test('a'));
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
console.log('count: ' + count);
