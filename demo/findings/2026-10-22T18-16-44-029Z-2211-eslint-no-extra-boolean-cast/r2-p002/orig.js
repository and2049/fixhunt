function getFlag() { return 1; }
function check() { return !!getFlag(); }
const r = check();
console.log(typeof r, r === true ? 'strict true' : 'not strict');
