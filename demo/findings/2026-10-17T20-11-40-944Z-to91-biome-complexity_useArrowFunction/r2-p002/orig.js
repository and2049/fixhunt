const [
  a,
  { b: function() { return 1; } }
] = [0, { b: () => {} }];
console.log(a, typeof b);
