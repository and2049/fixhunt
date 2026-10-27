let fails = 0;
try {
  [/start \t	 middle/].forEach(r => {
    if (!r.test('start\t\tmiddle')) throw new Error('no match');
  });
} catch (e) {
  fails++;
  console.log(e.name, e.message);
}
console.log(fails);
