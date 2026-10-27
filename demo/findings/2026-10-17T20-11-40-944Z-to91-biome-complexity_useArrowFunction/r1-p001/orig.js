function test() {
  try { f(); } catch (e) { console.log(e.name + ': ' + e.message); }
  var f = function() { return 42; };
}
test();
