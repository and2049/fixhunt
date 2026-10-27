function h() {
  console.log(arguments[0]); // captures !!x before change
  return !!x; // triggers rule
}
let x = 0;
h(x);
x = 1;
console.log(h(x));
