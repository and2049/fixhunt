let calls = 0;
function getStr() { return `str${++calls}`; }
const str = getStr();
const re = /foo {2}${getStr()}bar/;
console.log(calls, re.test(str));
