try { console.log('y before declaration:', y); } catch(e) { console.log('y before declaration error:', e.name + ': ' + e.message); }
let y = undefined;
console.log('y after declaration:', y);
try { console.log('y after fix:', ({ y }).y); } catch(e) { console.log('y after fix error:', e.name + ': ' + e.message); }
