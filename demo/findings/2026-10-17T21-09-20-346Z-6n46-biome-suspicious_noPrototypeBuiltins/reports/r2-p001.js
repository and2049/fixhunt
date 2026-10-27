let obj = null;
try {
} catch (e) {
}
try {
  console.log(obj.hasOwnProperty('prop'));
} catch (e) {
  console.log('Direct call threw:', e.name, e.message);
}
