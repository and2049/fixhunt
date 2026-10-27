const fakeArray = (...args) => ['called', ...args];
let Array = fakeArray;
try { console.log(Array(1, 2)[0]); }
catch (e) { console.log(e); }
try { console.log([...[]][0]); }
catch (e) { console.log(e); }
