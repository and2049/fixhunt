function process(a, b = [], ...rest) {
  return arguments.map(x => [x]).flat();
}
const res = process(1, 2, 3);
