let callCount = 0;
function f() { return ++callCount; }
if (f() > 0) { console.log('yes'); }
else { console.log('no', f()); }
