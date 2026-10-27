let str = "aßç🌟d", logs = [], re = /[a-zßç🌟]/gu;
function testChar(ch) {
  if (!re.test(ch)) { return false; }
  else { logs.push(re.lastIndex); re.lastIndex = 0; }
}
for (const c of str) testChar(c);
console.log(logs.join(","));
