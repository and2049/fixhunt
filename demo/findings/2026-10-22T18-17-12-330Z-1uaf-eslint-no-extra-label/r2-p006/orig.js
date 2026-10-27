let out = 0;
D: for (let i=0; i<2; i++) {
  E: for (let j=0; j<2; j++) {
    if (j === 0) continue D;
    out += i + j;
  }
}
console.log(out);
