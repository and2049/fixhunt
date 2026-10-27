let str = 'a\nb';
let regex = /^.$/;
console.log(regex.test(str)); // dot doesn't match newline without s flag
regex.lastIndex = 0;
let match = regex.exec('aa');
console.log(match ? match.index : -1);
