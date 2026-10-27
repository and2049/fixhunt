function f() {
  console.log(x); // ReferenceError due to TDZ
  const x = obj.a;
  return x;
}
const obj = { a: 42 };
try { f(); } catch (e) { console.log('TDZ:', e.name); }
