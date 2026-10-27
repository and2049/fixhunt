outer: {
  let obj = { x: 1 };
  if (Object.prototype.hasOwnProperty.call(obj, 'x')) {
    console.log('found');
    break outer;
  }
  console.log('missed');
}
console.log('done');
