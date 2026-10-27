let maybe = undefined;
let obj = {maybe};
console.log(obj.maybe ?? 'default');
try {
  console.log(obj.nonexistent?.prop);
} catch (e) {
  console.log('caught:', e.name);
}
