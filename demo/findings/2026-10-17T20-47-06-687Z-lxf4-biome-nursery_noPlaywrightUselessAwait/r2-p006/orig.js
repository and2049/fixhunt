let order = '';
function A() { order += 'A'; return '.a'; }
function B() { order += 'B'; return '.b'; }
await page.locator(A());
await page.locator(B());
console.log(order);
