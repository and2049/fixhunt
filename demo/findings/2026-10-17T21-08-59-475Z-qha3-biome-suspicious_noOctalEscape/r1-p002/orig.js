{ let \251 = 1; } // invalid? No—simulate via dynamic eval context
try {
  eval('let str = "\251"; console.log(str.charCodeAt(0));');
} catch (e) { console.log(e.name + ': ' + e.message); }
// Now introduce shadowing
{ let str = "shadow"; try { eval('str = "\251"'); } catch(e){} }
