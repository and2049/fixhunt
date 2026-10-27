const obj = {};
let log = '';
Y: while (!obj.prop) {
  Object.defineProperty(obj, 'prop', {
    get() { log += 'get'; return 1; }
  });
  if (obj.prop) break;
}
console.log(log);
