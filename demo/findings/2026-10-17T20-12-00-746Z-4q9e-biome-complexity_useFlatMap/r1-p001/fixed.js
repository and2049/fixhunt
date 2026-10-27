for (var i = 0; i < 2; i++) {
  var data = [[i], [i+1]];
  var result = data.flatMap(x => x);
  console.log(result.length);
}
console.log(typeof data);
