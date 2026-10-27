let counter = 0;
const inc = () => ++counter;
[it('a', inc), it('b', inc)].map(([_, fn]) => fn());
console.log('final counter:', counter);
