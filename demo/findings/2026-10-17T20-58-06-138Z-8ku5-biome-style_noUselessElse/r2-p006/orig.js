function f() {
  for (let i = 0; i < 2; i++) {
    if (i === 0) {
      continue;
    } else {
      var x = i;
    }
    console.log(x); // Hazard: x from previous iteration
  }
}
f();
