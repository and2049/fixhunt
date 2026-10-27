function test(a, b = 0b10, ...rest) { // b initializer triggers rule: rewrite to 2
  console.log('a:', a, 'b:', b, 'rest.length:', rest.length, 'arguments.length:', arguments.length);
  return b;
}
console.log('Result:', test(1)); // a=1, b=2 (from fix), rest=[], args len=1
// Before fix: b would be parseInt('10',2)=2 -> same? Wait, need difference.
// Let's make b depend on something that changes if rewritten.
// Actually, the value is same. Need side effect in default param.
// Redo: make default param have observable effect if rewritten.
