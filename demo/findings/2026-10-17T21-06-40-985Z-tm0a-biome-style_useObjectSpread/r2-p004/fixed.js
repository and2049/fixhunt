let key = 'dynamic';
const obj = {
  [key]: ({a: 1,}) // triggers rule
};
console.log(obj.dynamic.a);
key = 'changed';
console.log(obj.changed === undefined ? 'not present' : 'present');
