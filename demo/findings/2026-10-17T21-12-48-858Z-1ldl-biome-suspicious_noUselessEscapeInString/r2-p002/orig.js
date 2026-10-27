let val = '';
Object.defineProperty({}, 'x', {
  get() { return val += '\\a'; }
});
try { 
  ({}.x); 
} catch(e) {}
console.log(val);
