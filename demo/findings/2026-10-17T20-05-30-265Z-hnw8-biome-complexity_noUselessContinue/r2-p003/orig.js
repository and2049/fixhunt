loop: for (let i = 0; i < 1; i++) {
  function inner() { return 42; }
  continue loop;
  inner(); // unreachable
}
console.log(typeof inner); // Should error if hoisted wrongly
