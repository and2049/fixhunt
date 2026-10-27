function test() {
  try { f(); } catch (e) { console.log(e.name + ': ' + e.message); }
  var f = () => 42;
}
test();
