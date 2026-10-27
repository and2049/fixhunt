const dir = __dirname;
console.log('original:', typeof dir === 'string' ? dir : 'not string');
try {
  const fixed = import.meta.dirname;
  console.log('fixed:', typeof fixed === 'string' ? fixed : 'not string');
} catch (e) {
  console.log('error:', e.name, e.message);
}
