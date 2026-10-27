function test() {
  try {
    var lbl = { toString: () => 'L' }, i;
    lbl: {
      console.log('enter');
      break lbl;
    }
    return 'ok';
  } catch (e) {
    return e.name + ': ' + e.message;
  }
}
console.log(test());
