function f() {
  let x = 1;
  if (true) { return x; }
  else {
    let x = 2;
    console.log(x);
  }
}
f();
