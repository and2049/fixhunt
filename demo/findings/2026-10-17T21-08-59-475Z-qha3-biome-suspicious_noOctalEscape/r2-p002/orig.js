'use strict'; try { eval('"\251"'); console.log('should not reach'); } catch(e) { console.log(e.name, e.message); }
try { console.log('\251'.charCodeAt(0)); } catch(e) { console.log(e.name, e.message); }
