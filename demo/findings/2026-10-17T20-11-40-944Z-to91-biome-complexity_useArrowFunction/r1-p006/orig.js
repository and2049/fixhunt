let f = function() { return 'outer'; };
{
  let f = function() { return 'inner'; };
  console.log(f()); // inner
  console.log((function() { return f(); })()); // outer
}
