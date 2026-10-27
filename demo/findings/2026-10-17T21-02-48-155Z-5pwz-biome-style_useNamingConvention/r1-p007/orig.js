let regex = /\\u{1F600}/gu;
regex.lastIndex = 0;
let match = regex.exec('😀');
console.log(match ? match[0] : null);
