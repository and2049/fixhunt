var obj = {
  getPattern: function() { return 'a'; },
  makeRE: function() { return new RegExp(this.getPattern(), ''); }
};
var fn = obj.makeRE;
console.log(fn().test('a')); // Should be false due to lost this
