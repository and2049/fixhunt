let threw = false;
try {
  const x = `${'ok'}${(function(){ throw new Error('side effect'); })()}${'fail'`;
} catch (e) {
  threw = true;
  console.log('Caught:', e.name, e.message);
}
console.log('Threw:', threw);
