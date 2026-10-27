outer: {
  if (false) { break outer; }
  else {
    console.log('in else');
    break outer; // label 'outer' must still be in scope
  }
}
console.log('after label');
