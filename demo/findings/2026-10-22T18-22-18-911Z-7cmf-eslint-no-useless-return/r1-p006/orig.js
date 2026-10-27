outer: {
  function f() {
    console.log('in f');
    break outer; // jumps to after outer block
    return; // TRIGGER: but unreachable after break
  }
  f();
  console.log('after f call');
}
console.log('reached end');
// If return removed: same, because break outer still exits
// But to make return reachable: move break inside conditional
let flag = true;
outer2: {
  function g() {
    if (flag) {
      console.log('in g, breaking');
      break outer2;
    }
    console.log('in g, not breaking');
    return; // TRIGGER: only reached if !flag
  }
  g();
  console.log('after g');
}
flag = false;
g(); // now g runs full, returns, then logs 'after g'
console.log('final:');
