let a = false;
let bCalled = false;
async function b() { bCalled = true; return true; }
(async () => {
  if (a) { if (await b()) { console.log('inner'); } }
  console.log('bCalled:', bCalled);
})();
