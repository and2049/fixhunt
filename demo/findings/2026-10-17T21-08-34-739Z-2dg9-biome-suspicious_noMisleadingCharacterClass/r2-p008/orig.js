function f() {
  const /^[Á]$/ = {}; // Invalid syntax — adjust to realistic case
  // Instead: use variable named like the regex pattern
  let Á = 1;
  const re = /^[Á]$/;
  if (re.test('Á')) {
    console.log(Á); // logs 1
  }
  let Á = 2; // shadowing
  if (re.test('Á')) {
    console.log(Á); // logs 2 — but if regex broken, condition fails
  }
}
