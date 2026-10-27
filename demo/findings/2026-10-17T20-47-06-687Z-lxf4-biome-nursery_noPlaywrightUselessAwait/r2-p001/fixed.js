let logged = '';
function log(msg) { logged += msg + '|'; }
page.locator('.elem');
log('done');
console.log(logged);
