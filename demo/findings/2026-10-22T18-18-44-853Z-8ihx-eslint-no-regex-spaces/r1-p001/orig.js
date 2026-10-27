if (true) {
  let count = 0;
  function f() { return /a  b/.test('a b'); }
  do {
    if (f()) count++;
  } while (count < 2);
}
console.log(count);
