let log = [];
function f() { log.push(1); return {}; }
<div {...f()}></div>
console.log(log.length);
