let dirname = 'outer';
const dir = __dirname;
console.log('dirname:', dirname);
if (typeof dirname === 'string') {
  console.log('block dirname:', dirname);
}
