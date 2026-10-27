// Hazard 4: var hoisting with re-declaration
for (let i = 0; i < 2; i++) {
  var loc = { click: () => console.log('iter', i) }; // hoisted, redeclared
  await loc.click(); // rule fires here
}
console.log('After loop:', typeof loc); // loc exists due to hoisting
