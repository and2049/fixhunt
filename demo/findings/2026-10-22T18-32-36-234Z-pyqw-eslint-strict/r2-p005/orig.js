for (var i = 0; i < 2; i++) {
  var j = i;
  if (i === 0) {
    var j = 99; // re-declare in same block
  }
  console.log(j);
}
