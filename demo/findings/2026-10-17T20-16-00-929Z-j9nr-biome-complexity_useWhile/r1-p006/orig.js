let fns = [];
for (; fns.length < 2;) {
  function f() { return fns.length; }
  fns.push(f);
}
console.log(fns[0](), fns[1]());
