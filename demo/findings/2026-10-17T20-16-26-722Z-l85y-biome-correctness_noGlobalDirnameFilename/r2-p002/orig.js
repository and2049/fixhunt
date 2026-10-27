let threw = false;
try {
  const d = __dirname;
  if (d === undefined) throw new Error('unexpected');
} catch (e) {
  threw = true;
}
console.log('threw:', threw);
