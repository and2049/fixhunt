const re1 = /a/g;
const re2 = /a/g;
re1.lastIndex = 1;
console.log(re1 == re2);
console.log(re1 === re2);
