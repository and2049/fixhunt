for (var i = 0; i < 2; i++) {
  var arr = [i, i + 1];
  console.log(arr);
}
console.log('redeclare:', typeof arr);
var arr = [99];
console.log('after:', arr);
