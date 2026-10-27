// Hazard 6: Var hoisting and re-declaration
if (true) {
  var x = 1;
}
import { x } from './mod'; // TRIGGER: may be moved into block scope? No — top-level only.
// But if moved before var x, it creates a TDZ-like error? Not in ES6.
// Instead: re-declaration via import binding
console.log(typeof x); // 'undefined' if import creates binding before var init
