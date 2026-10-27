let o = {};
o['__proto__'] = { valueOf: () => 99 };
console.log(+o);
