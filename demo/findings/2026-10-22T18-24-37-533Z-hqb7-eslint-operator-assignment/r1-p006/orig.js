function sum(a, b = 0, ...rest) {
  let total = a;
  total = total + b; // TRIGGER
  for (const v of rest) total = total + v; // TRIGGER
  console.log('args length:', arguments.length, 'total:', total);
  return total;
}
console.log(sum(1, 2, 3, 4));
