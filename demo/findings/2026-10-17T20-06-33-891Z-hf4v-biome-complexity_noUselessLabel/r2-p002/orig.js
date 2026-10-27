function test() {
  let log = '';
  outer: // this comment is attached to the label token
    { log += 'outer';
      if (true) break outer;
    }
  console.log(log);
}
test();
