const obj = { x: 1, y: 2, z: 3 };
const { x: x, ...rest } = obj;
console.log(x + Object.values(rest).reduce((a, b) => a + b, 0));
