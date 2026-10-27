let y = 0;
try {
  y ||= (() => { throw new Error('side effect'); })();
  console.log('assigned:', y);
} catch (e) {
  console.log('caught:', e.name, e.message);
}
y = 0;
try {
  y ||= (() => { throw new Error('side effect'); })();
  console.log('assigned:', y);
} catch (e) {
  console.log('caught:', e.name, e.message);
}
