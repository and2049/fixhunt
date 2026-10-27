const re = /\(foo\)/;
const str = 'foo';
const match = re.exec(str);
console.log(match ? match.length : 0);
