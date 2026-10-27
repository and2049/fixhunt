function f(a='\a', ...rest) {
  return [arguments.length, arguments[0], f.length];
}
console.log(f());
