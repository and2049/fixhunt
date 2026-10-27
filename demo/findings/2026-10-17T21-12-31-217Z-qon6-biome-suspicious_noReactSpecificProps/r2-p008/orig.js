// Hazard 8: Var hoisting and re-declaration
for (var i = 0; i < 2; i++) {
  var className = `iter-${i}`; // hoisted, re-declared
  console.log(`i=${i}, className=${className}`);
  const el = `<div className=${className}></div>`;
  console.log(el);
}
console.log(`final: className=${className}`); // last value
