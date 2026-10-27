const obj = { get val() { console.log('get'); return 1; } };
for (let i = 0; i < 2; i++) {
  const v = obj.val; // side effect: log
  continue; // <-- removed
}
console.log('end');
