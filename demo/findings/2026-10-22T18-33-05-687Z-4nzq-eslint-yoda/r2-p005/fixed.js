function bad() { throw new Error('side effect'); }
let x = 1;
try {
  if (bad() == 0) { // triggers yoda: 0 == bad()
    console.log('unreachable');
  }
} catch (e) {
  console.log('caught:', e.name, e.message);
}
x = 0;
try {
  if (bad() == 0) { // would be fix: bad() == 0
    console.log('unreachable');
  }
} catch (e) {
  console.log('caught:', e.name, e.message);
}
