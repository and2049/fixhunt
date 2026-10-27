let self = this;
self.lastMatch = '';
const str = 'a1b2';
[...str].forEach(() => {
  const match = /\d/g.exec(str);
  self.lastMatch += match ? match[0] : '_';
});
console.log(self.lastMatch);
