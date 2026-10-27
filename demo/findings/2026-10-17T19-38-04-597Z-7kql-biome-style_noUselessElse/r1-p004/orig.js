let regex = /a/g;
let str = 'aa';
if (false) { return; }
else { regex.exec(str); }
console.log(regex.lastIndex);
