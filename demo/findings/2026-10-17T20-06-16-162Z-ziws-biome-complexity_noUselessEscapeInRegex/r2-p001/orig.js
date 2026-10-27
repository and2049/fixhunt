const re = /[\^abc]/;
let result = '';
for (const c of ['^', 'a', 'b', 'c']) {
  result += re.test(c) ? '1' : '0';
}
console.log(result);
