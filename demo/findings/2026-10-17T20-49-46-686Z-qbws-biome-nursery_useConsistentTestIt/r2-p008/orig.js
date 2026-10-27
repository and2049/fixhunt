let counter = 0;
const inc = () => ++counter;
[test('a', inc), test('b', inc)].map(([_, fn]) => fn());
console.log('final counter:', counter);
