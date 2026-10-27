function test(a, b, c) {
  console.log('args length:', arguments.length);
  const copied = Object.assign({}, arguments); // triggers rule
  console.log('copied 0:', copied[0]);
  return copied;
}
const result = test(10, 20, 30);
console.log('result 2:', result[2]);
