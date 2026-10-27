var result = [];
for (var i = 0; i < 2; i++) {
  let i ;
  result.push(i);
}
console.log(result); // Expected: [undefined, undefined]\nActual: [0, 1] (if fix drops init)
