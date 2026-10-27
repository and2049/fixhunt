let x = {};
console.log(new Boolean(!!x));
x = null;
try { console.log(new Boolean(!!x)); } catch(e) { console.log(e.name + ': ' + e.message); }
x = undefined;
try { console.log(new Boolean(!!x)); } catch(e) { console.log(e.name + ': ' + e.message); }
