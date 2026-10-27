// Hazard 2: Side effect order matters; removal may reorder
let log = '';
const sideEffect = (msg) => { log += msg; return { click: () => {} } };
// Simulate two locator-like calls with side effects in args
{ const temp = sideEffect('A'); await temp.click(); }
{ const temp = sideEffect('B'); await temp.click(); }
console.log('Log:', log);
