outer: {
  if (false) { break outer; }
  else {
    console.log('in else');
    break outer;
  }
}
console.log('reached');
