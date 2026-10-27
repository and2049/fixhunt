function F(a, b = 5, ...rest) {
  return a + b + rest.length;
}
export { F };
console.log(F(1, 2, 3, 4)); // 1+2+2=5
