const o = { valueOf: () => 2, toString: () => 'x' };
let acc = '';
acc = acc + o; // TRIGGER
console.log(typeof acc, acc);
try {
  acc = acc + Symbol('foo'); // TRIGGER? No, Symbol + string throws
} catch (e) {
  console.log(e.name, e.message);
}
console.log('final:', acc);
