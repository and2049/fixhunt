for (var i = 0; i < 2; i++) {
  var x = i;
  if (i === 0) {
    console.log(x); // first iteration
  } else {
    console.log(x); // second iteration - should be 1 but may be affected
  }
  console.log(<input key={i} disabled />);
}
