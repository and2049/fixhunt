function* gen() { yield undefined; }
const g = gen();
console.log(g.next().value);
console.log(g.next().value);
