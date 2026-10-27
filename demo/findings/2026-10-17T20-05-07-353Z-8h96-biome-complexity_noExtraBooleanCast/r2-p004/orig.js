const sym = Symbol('test');
const big = BigInt(42);
console.log(!!sym, !!big);
if (!!(sym || big)) {
  console.log('truthy');
}
