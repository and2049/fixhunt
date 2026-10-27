const obj = { val: 42, method() { return this.val; }, arrow: () => this.val };
let logs = [];
function wrapper(fn) {
  if (typeof fn === "function") { return fn.call({val: 99}); }
  else { logs.push(fn()); }
}
wrapper(obj.method);
wrapper(obj.arrow);
console.log(logs.length ? logs[0] : "none");
