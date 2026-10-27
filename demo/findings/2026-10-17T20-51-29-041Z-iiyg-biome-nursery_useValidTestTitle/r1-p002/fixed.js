function test(a, b) {
  console.log(typeof a + ',' + typeof b);
}
test(() => { console.log('callback ran'); }, 'should be second');
