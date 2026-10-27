function inner() {
  if (false) { return; }
  else { throw new Error('test'); }
}
function outer() {
  try { inner(); } catch (e) { console.log(e.stack.split('\n')[0]); }
}
outer();
