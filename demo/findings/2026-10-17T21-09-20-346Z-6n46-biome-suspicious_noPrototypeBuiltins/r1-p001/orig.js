let counter = 0;
function getKey() {
  return ++counter;
}
const obj = {};
try {
  console.log(obj[getKey()] = 'first', obj.hasOwnProperty(getKey()));
} catch (e) {
  console.log(e.name, e.message);
}
