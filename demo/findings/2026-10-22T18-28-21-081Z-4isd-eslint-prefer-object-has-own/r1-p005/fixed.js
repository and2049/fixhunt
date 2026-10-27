outer: {
  let obj = { x: 1 };
  if (Object.hasOwn(obj, 'x')) {
    console.log('found');
    break outer;
  }
  console.log('missed');
}
console.log('done');
