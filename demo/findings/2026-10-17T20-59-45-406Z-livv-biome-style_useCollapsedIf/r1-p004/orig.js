let str = 'abab';
let re = /a/g;
if (true) {
  if (re.test(str)) { console.log('1st:', re.lastIndex); }
  if (re.test(str)) { console.log('2nd:', re.lastIndex); }
}
console.log('Final lastIndex:', re.lastIndex);
