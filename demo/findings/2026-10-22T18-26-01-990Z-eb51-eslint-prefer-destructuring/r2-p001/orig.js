// Hazard 1: __proto__ key
function test() {
  const obj = { __proto__: null, a: 1 };
  // Rule should fire on next line: const a = obj.__proto__;
  const a = obj.__proto__; /* keep */
  console.log(a === null ? 'null-proto' : 'has-proto');
}
test();
