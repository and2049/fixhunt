async function foo() {
  const x = await Math//no comment
              .pow(2, 3);
  return x;
}
foo().then(r => console.log('Async result:', r));

function* gen() {
  yield 2**3;
}
const g = gen();
console.log('Generator first yield:', g.next().value);
