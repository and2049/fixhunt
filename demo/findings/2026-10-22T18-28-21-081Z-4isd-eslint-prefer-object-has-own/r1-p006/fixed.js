let obj = {};
let re = /a/g;
re.lastIndex = 0;
obj[re.exec('ba')] = true; // sets obj['a'] = true
if (Object.hasOwn(obj, re.exec('ba')[0])) {
  console.log('has');
} else {
  console.log('missing');
}
console.log(re.lastIndex); // should be 2 if two execs ran
