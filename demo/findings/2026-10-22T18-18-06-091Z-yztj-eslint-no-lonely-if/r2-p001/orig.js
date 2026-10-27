let x = { valueOf: () => 1 };
let y = { toString: () => '2' };
function test(a, b) {
  if (a == 0) {
    return String(a) + String(b);
  } else {
    if (b == '2') {
      return `${a}` + `${b}`;
    }
  }
}
console.log(test(0, y));
console.log(test(x, y));
