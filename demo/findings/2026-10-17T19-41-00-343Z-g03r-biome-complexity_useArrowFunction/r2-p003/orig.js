const obj = {
  fact: function fact(n) {
    return n <= 1 ? 1 : n * fact(n - 1);
  }
};
try {
  console.log(obj.fact(4));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
