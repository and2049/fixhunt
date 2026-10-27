function testVar() {
  switch(1) {
    case 1: {
      var scoped = 99;
      if (true) {
        var scoped = 88; // redeclaration ok in same function scope
      }
      console.log(scoped);
      break;
    }
  }
}
testVar();
