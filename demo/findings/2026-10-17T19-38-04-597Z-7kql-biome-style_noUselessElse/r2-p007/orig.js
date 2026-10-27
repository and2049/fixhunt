function f(flag) {
  if (flag) return;
  // This comment explains why we decrement
  counter--;
}
let counter = 5;
f(true);
f(false);
console.log(counter);
