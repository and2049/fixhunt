const a = [1, , 3];
const mapped = a.map(x => x === 2 ? [] : [x]);
console.log('mapped:', mapped);
const flatResult = mapped.flat();
console.log('flat():', flatResult, 'length:', flatResult.length);
a.map(x => x === 2 ? [] : [x]).flat(); // expect_trigger
const flatMapResult = a.map(x => x === 2 ? [] : [x]).flatMap(x => x);
console.log('flatMap():', flatMapResult, 'length:', flatMapResult.length);
