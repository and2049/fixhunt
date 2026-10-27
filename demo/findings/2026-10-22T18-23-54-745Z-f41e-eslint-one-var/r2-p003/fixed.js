function outer() {
  switch (x) {
    case 1:
      var a = 1;
      function inner() { return a; }
      break;
    case 2:
      var a = 2;
      console.log(inner());
      break;
  }
}
outer();
