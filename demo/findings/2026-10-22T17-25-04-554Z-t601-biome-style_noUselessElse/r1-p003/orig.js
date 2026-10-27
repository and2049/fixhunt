let a = 0, b = 0;
if (++a) { return; } else {
  b = ++a;
  console.log(a + ',' + b);
}
console.log('done');
