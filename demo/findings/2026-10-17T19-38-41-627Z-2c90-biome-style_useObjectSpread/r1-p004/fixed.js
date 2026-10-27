const regex = /a/g;
regex.lastIndex = 0;
const str = 'aa';
const match1 = regex.exec(str);
const obj = ({pattern: regex ,});
const match2 = regex.exec(str);
console.log('match1:', match1 ? match1[0] : null, 'match2:', match2 ? match2[0] : null);
