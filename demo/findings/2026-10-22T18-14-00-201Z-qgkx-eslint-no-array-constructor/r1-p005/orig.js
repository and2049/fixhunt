let results = [];
for (var i = 0; i < 2; i++) {
  var arr = Array(i);
  results.push(() => arr.length);
}
console.log(results[0](), results[1]());
