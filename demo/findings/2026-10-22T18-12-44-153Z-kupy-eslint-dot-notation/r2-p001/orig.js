"use strict";
function test(){let obj={eval:1};console.log(typeof obj.eval);return obj['eval'];}
try{test();}catch(e){console.log('Caught:', e.name+':'+e.message);}
