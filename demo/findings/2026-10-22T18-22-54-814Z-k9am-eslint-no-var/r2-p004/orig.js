function f(a, b = 2) {
  var argumentsLength = arguments.length;
  if (typeof arguments === 'object' && !(arguments instanceof Array)) {
    return argumentsLength + (b || 0);
  }
  return -1;
}
console.log(f(1, 3) + ',' + f(1));
