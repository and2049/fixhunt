for (var i = 0; i < 2; i++) {
  var msg = `count: ${i}`;
  console.log(msg);
}
console.log(typeof msg); // Should be 'string' due to hoisting
