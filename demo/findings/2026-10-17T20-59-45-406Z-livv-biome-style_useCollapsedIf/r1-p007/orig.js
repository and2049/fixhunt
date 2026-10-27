if (true) {
  if (false) {
    function inner() { return 1; }
    console.log(typeof inner); // 'function' due to hoisting
  }
}
console.log('inner after:', typeof inner); // 'function' due to hoisting to outer scope
