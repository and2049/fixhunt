function f() {
  for (let i = 0; i < 2; i++) {
    var x = 1; // hoisted to function scope
    let obj = {prop: 10};
    if (x === 1) {
      var x = 20; // redeclaration, affects closure
      console.log('inner x:', x);
    }
    let val = obj[\'prop\'] + x; // rule may fire here
    console.log('val:', val);
  }
  console.log('final x:', x);
}
f();
