function test() {
  let o = {x: 1};
  switch (o.x) {
    case 1:
      function inner() { return Object.hasOwn(o, 'x'); }
      console.log(inner());
      break;
  }
  label: {
    if (Object.hasOwn(o, 'x')) {
      break label;
    }
    console.log('should not reach');
  }
}
test();
