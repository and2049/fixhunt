const obj = {};
let log = '';
Object.defineProperty(obj, 'prop', {
  set(v) { log += v; }
});
obj.prop = `side` + `effect`; // first: template with interpolation? No -> 'sideeffect' is two statics
// Actually: `side` + `effect` -> two template literals, both trigger rule
// After fix: becomes 'side' + 'effect' -> same value
// But we want one static template
let captured = `static`; // triggers
obj.prop = captured;
console.log(log); // should be 'static'
