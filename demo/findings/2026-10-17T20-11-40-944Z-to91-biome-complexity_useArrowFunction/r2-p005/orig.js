let count = 0;
const fact = function(n) {
  if (n <= 1) return 1;
  return n * arguments.callee(n - 1);
};
try {
  console.log(fact(4));
} catch (e) {
  console.log(e.name, e.message);
}
