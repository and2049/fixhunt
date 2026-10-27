outer: {
  if (false) { break outer; }
  
    console.log('in else');
    break outer;
}
console.log('reached');
