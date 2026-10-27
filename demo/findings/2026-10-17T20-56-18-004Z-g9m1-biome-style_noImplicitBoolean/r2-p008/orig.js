// Hazard 8: Var hoisting and re-declaration in loop
for (var i = 0; i < 2; i++) {
  var disabled = i === 0; // hoisted, redeclared
  console.log('iteration', i, 'disabled:', disabled);
  // Rule fires here - uses loop-scoped var
  const el = <input disabled={disabled} />;
}
console.log('final disabled:', disabled);
