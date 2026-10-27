const arr = [, `hole`, `static`]; // index 0: hole, 1: 'hole', 2: 'static'
console.log(arr.length); // 3
arr.forEach((v, i) => {
  if (v === undefined) console.log('hole at', i);
  else console.log(i, v);
});
