const factorial = function(n) {
  return n <= 1 ? 1 : n * arguments.callee(n - 1);
};
try {
  console.log(factorial(4));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
