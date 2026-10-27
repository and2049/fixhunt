for (var i = 0; i < 2; i++) {
  var j = i;
  var k = {j};
}
console.log(typeof k === 'object' && k !== null ? k.j : 'null');
