// Hazard 7: TDZ in block
(function() {
  if (true) {
    console.log(typeof x); // TDZ if let/const
    // Rule fires on next line:
    let x = {}.prop; // assume {}.prop is undefined
  }
  // hoisted? no - block scoped
})();
