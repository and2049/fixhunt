function main() {
  let out = '';
  L: for (let i = 0; i < 2; i++) {
    try {
      if (i === 0) { break L; }
      else { out += i; }
    } finally { out += 'f'; }
  }
  console.log(out);
}
main();
