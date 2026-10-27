const obj = {
  get rx() { return /=/; },
  getArrow: () => /=/,
  getFn: function() { return /=;/ }
};
console.log(obj.getArrow().test('x'), obj.getFn().test('x'));
