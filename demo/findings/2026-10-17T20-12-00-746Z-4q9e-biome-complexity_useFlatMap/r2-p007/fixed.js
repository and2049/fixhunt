function test() {
  if (true) {
    function mapFn(x) { return [x, 0]; }
    const arr = [1, 2];
    console.log('mapped:', arr.map(mapFn));
    const flat = arr.flatMap(mapFn);
    console.log('flat:', flat);
    arr.flatMap(mapFn); // expect_trigger
  }
  switch (1) {
    case 1:
      function caseFn(x) { return [x * 2]; }
      break;
  }
}
test();
