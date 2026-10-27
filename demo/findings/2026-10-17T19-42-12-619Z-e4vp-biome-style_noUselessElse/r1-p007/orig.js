function main() {
  if (false) { return; }
  else { function f() { return 1; } }
  try { console.log(f()); } catch (e) { console.log(e.name); }
}
main();
