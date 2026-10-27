function f() {
  let flag = false;
  // outer-else-brace-comment
  if (!flag) {
    flag = true;
  } else {
    // inner-if-line-comment
    if (flag) {
      console.log('inner taken');
    }
  }
  console.log('flag:', flag);
}
f();
