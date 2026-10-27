var o = undefined;
console.log(String(o));
console.log(typeof o);
o = { toString: () => 'obj', valueOf: () => 99 };
console.log(o + '');
console.log(`${o}`);
