let count = 0;
let obj = {};
Object.defineProperty(obj, 'x', {
  get(){ count++; return 5; }
});
console.log(+obj.x, count);
