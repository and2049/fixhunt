let x = 1;
{
  let x = 2;
  const getX = () => x;
  console.log(getX()); // Prints 2
}
console.log(getX()); // After rewrite: prints 1 (outer x)
