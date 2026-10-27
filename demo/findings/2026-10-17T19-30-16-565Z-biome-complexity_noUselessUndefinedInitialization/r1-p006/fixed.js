var a ;
for (let i = 0; i < 1; i++) {
  var a = 1;
}
console.log('a after loop (var hoisted):', a);
try { console.log('a after fix:', ({ a }).a); } catch(e) { console.log('a after fix error:', e.message); }
