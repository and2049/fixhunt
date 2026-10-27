let result;
try {
  result = 0 + function() { return 1; }();
} catch (e) {
  result = e;
}
console.log(result);
