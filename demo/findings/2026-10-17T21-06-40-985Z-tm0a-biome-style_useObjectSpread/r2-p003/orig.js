const assign = Object.assign;
const result = assign({}, {x: 1}); // not triggered by rule
console.log('result.x:', result.x);
// Biome will NOT suggest fix here because it's not direct Object.assign call
