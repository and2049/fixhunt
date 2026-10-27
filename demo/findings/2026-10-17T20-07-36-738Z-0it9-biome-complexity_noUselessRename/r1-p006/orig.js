let seq = 0;
function inc() { return ++seq; }
let { b: b } = { b: inc() };
console.log(seq, b);
