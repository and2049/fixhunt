const obj = {};
let log = [], val = 10;
Object.defineProperty(obj, "prop", {
  get() { log.push("get"); return val; },
  set(v) { log.push("set:" + v); val = v; }
});
function test() {
  if (obj.prop > 5) { return obj.prop; }
  else { obj.prop = 20; }
}
test();
console.log(log.join("|") + "|" + val);
