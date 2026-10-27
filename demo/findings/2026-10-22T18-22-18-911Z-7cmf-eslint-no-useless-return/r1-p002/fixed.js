function f() {
  console.log(typeof x);
  var x = 1;
  
}
f(); // logs 'undefined', but if return removed, still same
// However, to make trigger meaningful: add shadowing
function g() {
  console.log(typeof y);
  let y = 2;
  
}
g(); // TDZ: ReferenceError if accessed before init
// But return removal doesn't affect TDZ
// Instead, use closure capture:
let h;
function outer() {
  let z = 3;
  h = () => {
    console.log(z);
    
  };
}
outer();
h(); // prints 3
// Now mutate: remove return? no effect.
// Better: make return affect whether inner fn is called
function makeCounter() {
  let count = 0;
  return function inner() {
    console.log(count++);
     // TRIGGER
  };
}
const c = makeCounter();
c(); // 0
c(); // 1
console.log('done');
