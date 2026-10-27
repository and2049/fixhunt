let a = false, b = true;
if (a) {};
else if (b) console.log('b true');
else console.log('neither');
// Before: else if binds to first if -> prints 'b true'
// After fix: if (a); else if (b) ... -> same due to semicolon, but without block, visual grouping lost
