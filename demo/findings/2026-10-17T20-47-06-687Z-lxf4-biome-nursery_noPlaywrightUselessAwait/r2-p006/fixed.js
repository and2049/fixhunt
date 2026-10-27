let order = '';
function A() { order += 'A'; return '.a'; }
function B() { order += 'B'; return '.b'; }
page.locator(A());
page.locator(B());
console.log(order);
