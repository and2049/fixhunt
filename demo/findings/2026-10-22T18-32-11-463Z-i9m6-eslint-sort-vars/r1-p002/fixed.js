function outer() {
  let x = 1;
  {
    let y = console.log(x) || 0, x = console.log('shadow') || 2;
    return x;
  }
}
console.log(outer());
