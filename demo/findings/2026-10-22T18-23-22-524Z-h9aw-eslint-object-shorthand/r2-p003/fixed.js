let a = 1;
{
  let a = 2;
  let o = {a}; // triggers rule, inner a=2
  console.log(o.a); // prints 2
}
console.log(a); // prints 1 (outer)
