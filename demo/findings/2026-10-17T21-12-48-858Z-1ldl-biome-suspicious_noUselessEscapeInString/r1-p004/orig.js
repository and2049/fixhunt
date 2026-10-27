const re = /\d/g;
re.lastIndex = 0;
console.log(re.exec('1\a2')[0]);
console.log(re.lastIndex);
