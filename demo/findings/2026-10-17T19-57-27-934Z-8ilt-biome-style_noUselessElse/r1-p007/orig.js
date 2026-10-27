try {
  if (false) { return; }
  else { throw x; }
} catch (e) {
  console.log(e.name);
}
let x = 42;
