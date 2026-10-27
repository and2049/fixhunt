G: {
  function f() { return 1; }
  if (f() === 1) break G;
}
console.log(typeof f);
