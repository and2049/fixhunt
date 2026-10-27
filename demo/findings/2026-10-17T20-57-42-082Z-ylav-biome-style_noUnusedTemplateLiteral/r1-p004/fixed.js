for (let i = 0; i < 2; i++) {
  var x = "loop" + i; // first iter: 'loop0', second: 'loop1'
  if (i === 0) {
    var x = "inner"; // re-declaration, same var, re-initialized
    console.log(x); // prints 'inner' then 'inner' again?
  }
  console.log(x); // after if: 'inner' both times due to hoisting
}
