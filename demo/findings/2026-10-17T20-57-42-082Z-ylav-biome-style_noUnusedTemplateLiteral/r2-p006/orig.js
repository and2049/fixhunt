let x = 1;
if (true) {
  const x = `inner: ${x}`; // Rule triggers here
  console.log(x);
}
console.log(x); // Should print 1
