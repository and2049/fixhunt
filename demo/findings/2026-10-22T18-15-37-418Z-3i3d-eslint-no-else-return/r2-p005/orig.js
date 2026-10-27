let log = "";
function check(val) {
  if (val < 0) { log += "neg"; return; }
  else { debugger; log += "pos"; }
}
check(-1);
check(1);
console.log(log);
