function test() {
  console.log(typeof x); // With var: undefined; with let: TDZ error
  var x = 1;
  return x;
}
try {
  console.log(test());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
