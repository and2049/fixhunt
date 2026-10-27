let counter = 0;
function getKey() {
  return ++counter;
}
const obj = {};
try {
  console.log(obj[getKey()] = 'first', Object.hasOwn(obj, getKey()));
} catch (e) {
  console.log(e.name, e.message);
}
