try { console.log(z); } catch(e) { console.log('TDZ:', e.name); }
let z = 1;
export {};
try { console.log(z); } catch(e) { console.log('After init:', z); }
