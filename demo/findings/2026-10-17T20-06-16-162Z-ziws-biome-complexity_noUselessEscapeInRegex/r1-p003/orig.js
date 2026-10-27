const obj = { get re() { return /[\\]/; } };
try {
  const m = obj.re?.test('\\');
  console.log(m); // Should be true if \\ matches literal backslash
} catch (e) {
  console.log(e.name, e.message);
}
