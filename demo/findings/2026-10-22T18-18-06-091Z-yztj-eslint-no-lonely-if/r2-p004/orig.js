const f = (a, b) =>
  a > 0
    ? a + b
    : (() => {
        if (b === 0) return 0;
        if (b > 0) return b;
      })();
try {
  console.log(f(-1, 5));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
