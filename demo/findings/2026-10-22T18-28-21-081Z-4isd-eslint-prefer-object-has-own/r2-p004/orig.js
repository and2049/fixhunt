function test() {
  let o = {x: 1};
  switch (o.x) {
    case 1:
      function inner() { return Object.prototype.hasOwnProperty.call(o, 'x'); }
      console.log(inner());
      break;
  }
  label: {
    if (Object.prototype.hasOwnProperty.call(o, 'x')) {
      break label;
    }
    console.log('should not reach');
  }
}
test();
