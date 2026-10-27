let threw = false;
try {
  const d = import.meta.dirname;
  if (d === undefined) throw new Error('unexpected');
} catch (e) {
  threw = true;
}
console.log('threw:', threw);
