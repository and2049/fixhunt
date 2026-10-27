let value = 1;
{
  const value = { toFixed: () => 'inner' };
  console.log(value.toFixed());
}
console.log(value.toFixed());
