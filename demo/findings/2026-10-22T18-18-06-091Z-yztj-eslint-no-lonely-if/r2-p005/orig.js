function test() {
  if (false) {
    let x = 1;
  } else {
    if (true) {
      console.log(typeof x);
      let x = 2;
    }
  }
}
try {
  test();
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
