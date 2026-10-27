let obj = null;
console.log(obj?.m?.());
obj = { m: function() { return 'hit'; } };
console.log(obj?.m?.());
obj = { m: undefined };
console.log(obj?.m?.());
