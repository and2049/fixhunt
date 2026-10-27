let x = { valueOf: () => { console.log('coerced'); return 0; } };
if (true) return;
else {
  console.log(+x);
}
console.log('end');
