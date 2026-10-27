let regex = /a/g;
function f() { regex.test('aa'); return; }
console.log(regex.lastIndex);
f();
console.log(regex.lastIndex);
