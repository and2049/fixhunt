let result;
try {
  const fn = () => { console.log('side'); return 42; };
  // This pattern does NOT trigger no-unneeded-ternary because branches differ
  result = true ? fn() : 0;
  console.log('result:', result);
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
