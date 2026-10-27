let called = false;
function fn() { called = true; return '.dynamic'; }
console.log('before:', called);
await page.locator(fn());
console.log('after:', called);
