function process(a, b = [], ...rest) {
  return arguments.flatMap(x => [x]);
}
const res = process(1, 2, 3);
console.log(res.length, res.join(','));
