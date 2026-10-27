function test() {
  let result = [];
  for (let i = 0; i;; break) {
    var x = 1;
    if (i === 0) { return x; } // Line A
    else {                     // Hazard: else with var decl
      console.log('else', x);
      var x = 99;              // Redeclaration - hoisted!
      x++;
    }
    result.push(x);
    if (result.length > 2) break;
    i++;
  }
  return result.join(',');
}
console.log(test());
