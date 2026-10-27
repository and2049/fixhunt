let called = false;
function fn() { called = true; return '.dynamic'; }
console.log('before:', called);
page.locator(fn());
console.log('after:', called);
