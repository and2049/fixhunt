const obj = {
  match: /^[Á]$/,
  check(s) { return this.match.test(s); }
};
const fn = obj.check;
console.log(fn.call(obj, 'Á')); // Should be true
// If fix breaks regex, this call returns false
