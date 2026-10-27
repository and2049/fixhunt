function main() {
  let x = 0;
  if (false) { return; }
  /* keep-me */
  else { x = 1; /* inner */ }
  console.log(x);
}
main();
