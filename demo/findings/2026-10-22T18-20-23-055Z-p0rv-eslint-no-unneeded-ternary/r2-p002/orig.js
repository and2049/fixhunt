let pattern = /a/g;
let str = 'aa';
let match1 = pattern.test(str) ? pattern : /b/g;
console.log('match1 lastIndex:', match1.lastIndex);
pattern.lastIndex = 0;
let match2 = pattern.test(str) ? pattern : /b/g;
console.log('match2 lastIndex:', match2.lastIndex);
if (match1.lastIndex !== match2.lastIndex) {
  throw new Error('lastIndex divergence');
}
