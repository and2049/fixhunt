const args = { 0: 'a', 1: 'b', length: 2 };
try { console.log(Array(...args).length); }
catch (e) { console.log('A:', e.name); }
try { console.log([...args].length); }
catch (e) { console.log('B:', e.name); }
