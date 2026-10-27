// Hazard 3
function f(dir = import.meta.dirname) {
  return dir.length;
}
console.log(f());
