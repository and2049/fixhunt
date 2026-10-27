// @ts-check
const f = function(): number {
  return 42;
};
console.log(typeof f === 'function' && f());
