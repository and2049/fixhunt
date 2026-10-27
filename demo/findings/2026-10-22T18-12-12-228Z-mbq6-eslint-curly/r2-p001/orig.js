// @ts-ignore
let x = 0;
function f() {
  // pre-directive-like comment
  if (x++ === 0)
    ; // <-- triggers curly: empty stmt
}
f();
f();
console.log(x);
