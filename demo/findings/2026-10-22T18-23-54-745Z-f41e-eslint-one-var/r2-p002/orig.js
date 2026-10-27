function f() {
  let [x = y, y] = [];
  console.log(x, y);
}
try { f(); } catch (e) { console.log(e.name + ': ' + e.message); }
