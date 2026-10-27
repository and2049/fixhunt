const obj = { value: 42, getValue: function() { return this.value } }
const fn = obj.getValue
console.log((fn() == undefined) ? 'undef' : 'defined')
console.log((fn.call(obj) == 42) ? 'match' : 'no match')
