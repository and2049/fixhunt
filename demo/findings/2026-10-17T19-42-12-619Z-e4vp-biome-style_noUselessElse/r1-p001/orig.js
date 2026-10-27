function main() {
  let out = '';
  L1: for (let i = 0; i < 2; i++) {
    for (let j = 0; j < 2; j++) {
      if (j === 0) { continue L1; }
      else { out += i + ',' + j + '|'; }
    }
  }
  console.log(out);
}
main();
