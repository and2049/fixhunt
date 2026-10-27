// Hazard 8: arguments and rest
function test(...args) {
  if (args.length > 0 && args[0] === 42) {
      return arguments[0];
    }
  return -1;
}
console.log('result:', test(42, 99));
