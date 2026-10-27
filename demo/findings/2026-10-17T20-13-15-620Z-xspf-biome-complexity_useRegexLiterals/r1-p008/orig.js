var obj = {
  toString: function() { return '\\d+'; }
};
var re = new RegExp(obj, 'g');
console.log(re.test('123'));
