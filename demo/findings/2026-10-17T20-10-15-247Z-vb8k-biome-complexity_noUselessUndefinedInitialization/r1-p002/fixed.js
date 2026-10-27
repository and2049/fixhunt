function getValue(flag) {
  // Flag-controlled initialization
  let x ; /* important note */
  if (flag) x = 42;
  return x;
}

console.log('Flag false:', getValue(false));
console.log('Flag true:', getValue(true));
