let count = 0;
X: while (count < 3) {
  const re = /a/g;
  re.lastIndex = 0;
  const m = re.exec('baaab');
  if (!m) break X;
  count += m[0].length;
}
console.log(count);
