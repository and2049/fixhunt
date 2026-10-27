function main() {
  let out = '';
  L: for (let i = 0; i < 2; i++) {
    if (i === 0) { continue; }
    else { L: out += i; break L; }
  }
  console.log(out);
}
main();
