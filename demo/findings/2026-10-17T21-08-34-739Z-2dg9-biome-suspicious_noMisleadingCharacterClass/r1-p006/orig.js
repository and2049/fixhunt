try {
  const rx = /[\p{L}&&[^Á]]/u;
  console.log(rx.test('B'), rx.test('Á')); // true false
} catch (e) {
  console.log(e.name, e.message); // fallback if unsupported
}
// After fix: becomes [\p{L}&&[^A]] -> excludes 'A', not 'Á'
// So 'Á' would pass (since not 'A'), changing result
console.log(/[\p{L}&&[^A]]/u.test('Á')); // true -- would be wrong if we meant to exclude Á
