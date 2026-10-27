let out = '';
outer: for (let i = 0; i < 2; i++) {
  inner: for (let j = 0; j < 2; j++) {
    if (i === 0) {
      continue outer; /* else block */
    } else {
      out += j;
    }
  }
}
console.log(out);
