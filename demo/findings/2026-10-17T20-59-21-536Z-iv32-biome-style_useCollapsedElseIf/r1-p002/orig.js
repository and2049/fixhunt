let y = 0;
if (true) {} else {/* keep me */
  if (false) { y = 99; }
}
console.log(y); // Should stay 0 due to false condition
