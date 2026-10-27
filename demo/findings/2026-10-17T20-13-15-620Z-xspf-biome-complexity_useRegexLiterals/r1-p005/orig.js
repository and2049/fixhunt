function getPattern() { return null; }
var re = new RegExp(getPattern(), '');
console.log(re === null ? 'null' : typeof re);
