let dirname = 'outer';
const dir = import.meta.dirname;
console.log('dirname:', dirname);
if (typeof dirname === 'string') {
  console.log('block dirname:', dirname);
}
