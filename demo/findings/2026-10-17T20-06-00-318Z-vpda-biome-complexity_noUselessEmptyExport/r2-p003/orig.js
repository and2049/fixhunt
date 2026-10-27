function f(a, b = 1, ...rest) {
  return { args: arguments.length, len: f.length, rest };
}
export {};
console.log(JSON.stringify(f(5)));
