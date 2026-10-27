function mapper(a, b = 10, ...rest) {
  console.log('args.length:', arguments.length, 'b:', b, 'rest:', rest);
  return [a + b];
}
const arr = [5];
console.log('calling map:');
const result = arr.flatMap(mapper);
console.log('flat result:', result);
arr.flatMap(mapper); // expect_trigger
const flatMapResult = arr.map(mapper).flatMap(x => x);
console.log('flatMap result:', flatMapResult);
