// Hazard 2: Order of evaluation - side effect duplication
let count = 0;
function inc() { return count++; }
const x = inc();
console.log('x:', x);
// Rule fires on minimized attribute below
const el = <button disabled={inc()} />;
console.log('count after:', count);
