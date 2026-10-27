function outer() {
  let result = [];
  switch(true) {
    case x > 0: {
      function getVal() { return x * 2; }
      break;
    }
  }
  try {
    result.push(getVal());
  } catch(e) {
    result.push(e.name);
  }
  return result.join(':');
}
let x = 5;
console.log(outer());
