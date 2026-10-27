function f() {
  switch (x) {
    case 1:
      var a = 1; // initialized in case 1
      break;
    case 2:
      var a = 2; // initialized in case 2
      console.log(a);
      break;
  }
}
f();
