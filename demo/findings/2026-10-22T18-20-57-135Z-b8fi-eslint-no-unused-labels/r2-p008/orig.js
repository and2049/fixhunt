LABEL:
{
  if (true) {
    function g() { return 'in-block'; }
    console.log(g()); // Should work: function decl in block
  }
  // Note: g is not accessible here in strict mode, but we're not using strict
}
console.log(typeof g); // undefined (not hoisted out of block)
