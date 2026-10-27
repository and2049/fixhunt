let count = 0;
function logArg() {
  console.log('arg eval', ++count);
  return 'key';
}
const obj = {};
console.log('Before fix simulation:');
const prop = obj.hasOwnProperty;
prop.call(obj, logArg());
count = 0;
console.log('\nAfter fix (Biome rewrites):');
Object.hasOwn(obj, logArg());
