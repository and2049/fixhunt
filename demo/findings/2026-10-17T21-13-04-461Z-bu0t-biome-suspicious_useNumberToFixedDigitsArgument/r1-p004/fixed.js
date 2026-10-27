function test() {
  console.log(typeof toFixedResult);
  let toFixedResult = (5.5).toFixed();
  return toFixedResult;
}
try { test(); } catch(e) { console.log(e.name + ': ' + e.message); }
