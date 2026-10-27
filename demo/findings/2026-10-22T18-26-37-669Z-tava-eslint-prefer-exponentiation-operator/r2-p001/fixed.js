let x = 0;
const inc = () => {
  x++;
  return x;
};
console.log(inc()**inc());
x = 0;
console.log(inc() ** inc());
