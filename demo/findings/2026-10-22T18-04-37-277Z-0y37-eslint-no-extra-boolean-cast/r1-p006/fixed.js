{
  let flag = 0;
  if (flag) { // triggers rule
    let flag = 1; // shadowing
    console.log(flag);
  }
  console.log(flag);
}
