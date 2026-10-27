let -0 = 42;
function f() {
  let -0 = 99;
  if (-0 === -0) {
    console.log('inner:', -0);
  }
}
f();
console.log('outer:', -0);
