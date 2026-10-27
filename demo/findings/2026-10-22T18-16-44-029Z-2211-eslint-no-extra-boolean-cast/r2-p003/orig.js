const re = /\u{61}/gu;
re.lastIndex = 0;
const str = 'a';
const match = re.exec(str);
console.log(match ? !!match[0] : null, match ? match.index : -1);
