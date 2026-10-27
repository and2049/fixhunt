function test() {
  console.log(typeof this);
  return this.value;
}
try {
  console.log(test.call({value: 'ok'}));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
