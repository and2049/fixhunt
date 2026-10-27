let obj = {x: undefined};
try {
  let {x: x = throw new Error('bad')} = obj;
  console.log('unreachable');
} catch (e) {
  console.log('caught:', e.constructor.name, e.message);
}
console.log('done')
