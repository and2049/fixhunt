let str = 'abab';
let re = /ab/g;
let matches = 0;
for (; re.test(str);) {
  matches++;
}
console.log(matches);
