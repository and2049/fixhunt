function test() {
  const obj = { valueOf: () => 1, toString: () => '2' };
  let sym = String(obj), num = Number(obj) + 1;
  return sym + '-' + num;
}
console.log(test());
