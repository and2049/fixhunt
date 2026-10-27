let count = 0;
function inc() { return ++count; }
const vals = [inc(), inc()].map(v => `${v}`.trimLeft());
console.log(`count=${count}, vals=${vals}`);
