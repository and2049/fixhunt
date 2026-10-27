const raw = /=test/;
const re1 = new RegExp(String(raw));
console.log(re1.test('xtest'));
const re2 = /=[=]test/;
console.log(re2.test('xtest'));
