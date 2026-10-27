let x = 1;
function test() {
  let x = 2;
  const inner = <span></span>;
  { let x = 3; console.log(x); }
  console.log(x);
}
test();
