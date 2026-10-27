let x = 1;
A: for (; ;) {
  let x = 2;
  if (x === 2) break;
}
console.log(x);
