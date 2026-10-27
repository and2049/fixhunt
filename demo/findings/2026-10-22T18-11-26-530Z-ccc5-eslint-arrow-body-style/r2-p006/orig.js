let x = 1;
(() => {
  let x = 2;
  return () => x;
})()();
console.log(x);
