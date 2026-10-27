function f(a = "\251", b) { return [a, b, arguments.length]; }
console.log(f().join('|'));
console.log(f(undefined, 'x').join('|'));
