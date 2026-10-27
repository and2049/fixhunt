const rx = /^[\[\]]*$/u;
console.log(rx.test('[]'), rx.test('[[]]'), rx.test('][')); // true true false
// No multi-code-point in class, so rule should not fire
// Output remains stable regardless of fix attempt
