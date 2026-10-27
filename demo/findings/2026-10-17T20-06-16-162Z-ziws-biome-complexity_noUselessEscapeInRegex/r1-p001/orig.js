function test() {
  const re = /[a\-z]/;
  let result = '';
  for (const c of 'az-') {
    if (re.test(c)) result += c;
  }
  console.log(result); // Should be 'a-z' if literal hyphen preserved; becomes 'az' if range
}
test();
