const weird = {
  valueOf() { return 42; },
  toString() { return 'hello'; }
};
const sym = Symbol('test');
const big = BigInt(123);
const arr = [weird, sym, big];
const mapped = arr.map(x => [x, String(x)]);
console.log('mapped:', mapped);
const flattened = mapped.flat();
console.log('flat result:', flattened);
arr.flatMap(x => [x, String(x)]); // expect_trigger
const flatMapped = arr.map(x => [x, String(x)]).flatMap(x => x);
console.log('flatMap result:', flatMapped);
