let count = 0;
function side() {
  return ++count;
}
const obj = {x: side(), y: side()};
// If rewritten to {x, y} but only once evaluated? Not applicable.
// Instead: duplicate eval in explicit form
const obj2 = {a: side(), a: side()};
console.log(count); // Should be 2 if both sides evaluated
console.log(obj2.a); // Last wins: 2
