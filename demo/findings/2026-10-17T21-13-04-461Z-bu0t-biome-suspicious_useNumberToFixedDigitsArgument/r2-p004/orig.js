const x = {
  valueOf: () => 2.5,
  toString: () => '2.5'
};
console.log(+x.toFixed());
console.log(`${x.toFixed()`);
