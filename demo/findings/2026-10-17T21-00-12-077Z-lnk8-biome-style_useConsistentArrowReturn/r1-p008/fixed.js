const makeObj = () => ({ __proto__: null, a: 1 });
const o = makeObj();
console.log(o.__proto__ === null && o.a === 1);
