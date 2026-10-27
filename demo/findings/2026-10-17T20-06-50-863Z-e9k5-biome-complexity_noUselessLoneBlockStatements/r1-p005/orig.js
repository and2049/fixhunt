const o = { valueOf: () => 42, toString: () => 'obj' };
console.log(+{}, +o);
console.log(`${{}}`, `${o}`);
