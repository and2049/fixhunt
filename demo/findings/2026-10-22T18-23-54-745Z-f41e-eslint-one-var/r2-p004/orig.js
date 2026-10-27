function f() {
  let re1 = /a/g;
  let re2 = /b/g;
  re1.test('ab');
  console.log(re2.test('ab'));
}
f();
