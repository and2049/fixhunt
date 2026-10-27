
this.lastMatch = '';
const str = 'a1b2';
[...str].forEach(() => {
  const match = /\d/g.exec(str);
  this.lastMatch += match ? match[0] : '_';
});
console.log(this.lastMatch);
