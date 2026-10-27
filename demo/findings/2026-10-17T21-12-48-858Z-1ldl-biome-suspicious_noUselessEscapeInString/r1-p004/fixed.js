const re = /\d/g;
re.lastIndex = 0;
console.log(re.exec('1a2')[0]);
console.log(re.lastIndex);
