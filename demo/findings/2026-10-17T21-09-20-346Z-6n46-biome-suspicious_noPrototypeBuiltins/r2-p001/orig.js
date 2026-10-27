let obj = null;
console.log('obj == null:', obj == null);
console.log('obj === null:', obj === null);
try {
  console.log(obj?.hasOwnProperty('prop'));
} catch (e) {
  console.log('Optional chain threw:', e.name, e.message);
}
try {
  console.log(obj.hasOwnProperty('prop'));
} catch (e) {
  console.log('Direct call threw:', e.name, e.message);
}
