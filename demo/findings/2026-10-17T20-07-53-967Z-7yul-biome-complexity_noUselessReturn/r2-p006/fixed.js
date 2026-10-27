let regex = /a/g;
function f() { regex.test('aa'); }
console.log(regex.lastIndex);
f();
console.log(regex.lastIndex);
