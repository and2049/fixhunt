let f = () => 'outer';
{
  let f = () => 'inner';
  console.log(f()); // inner
  console.log((() => f())()); // outer
}
