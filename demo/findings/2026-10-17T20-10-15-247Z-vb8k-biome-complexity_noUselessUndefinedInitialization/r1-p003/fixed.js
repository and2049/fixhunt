const obj = {
  toString() { return 'obj'; },
  valueOf() { return 42; }
};

let u ; // Rule triggers
console.log('+ coercion:', String(u + obj));
console.log('template literal:', `${u}${obj}`);

// Change u via reassignment
test();
function test() { u = 'changed'; }
console.log('After reassignment +:', String(u + obj));
console.log('After reassignment template:', `${u}${obj}`);
