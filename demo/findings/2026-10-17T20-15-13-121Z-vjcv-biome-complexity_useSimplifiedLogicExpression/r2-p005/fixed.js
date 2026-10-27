let called = 0;
const f = () => { called++; return 99; };
let result = f();
console.log('result=' + result + ', called=' + called);
