const obj = { valueOf() { return 2; }, toString() { return "2" } };
let results = [];
function add(x) {
  if (x === 2) { return x + 3; }
  else { results.push(String(x) + 3); }
}
results.push(add(2));
add(obj);
console.log(results.join(""));
