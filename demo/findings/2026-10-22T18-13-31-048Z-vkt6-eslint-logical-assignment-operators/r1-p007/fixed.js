let regex = /a/g;
let str = 'ab';
console.log(regex.test(str));
regex ||= /b/g;
console.log(regex.test(str));
console.log(regex.lastIndex);
