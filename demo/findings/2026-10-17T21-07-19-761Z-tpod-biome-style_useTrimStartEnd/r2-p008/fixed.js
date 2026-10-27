let count = 0;
function inc() { return ++count; }
const vals = [inc(), inc()].map(v => `${v}`.trimStart());
console.log(`count=${count}, vals=${vals}`);
